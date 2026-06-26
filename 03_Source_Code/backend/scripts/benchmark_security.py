"""Benchmark biaya operasi keamanan TUMBUH.

Jalankan dari folder `03_Source_Code/backend`:

    python scripts/benchmark_security.py

Benchmark ini sengaja tidak mengakses database dan tidak melakukan network
call. Tujuannya adalah mengukur overhead lokal dari operasi keamanan inti:
bcrypt, JWT, Fernet field encryption, dan tanda tangan digital Ed25519.
Baseline "before" bersifat sintetis: plaintext password compare, plaintext
cover letter, tanpa JWT, tanpa Fernet, dan tanpa Ed25519.
"""

from __future__ import annotations

import argparse
import json
import statistics
import sys
import time
from dataclasses import dataclass
from pathlib import Path
from typing import Callable

from cryptography.fernet import Fernet
from cryptography.hazmat.primitives.asymmetric.ed25519 import Ed25519PrivateKey

BACKEND_ROOT = Path(__file__).resolve().parents[1]
if str(BACKEND_ROOT) not in sys.path:
    sys.path.insert(0, str(BACKEND_ROOT))

from app.services.auth_service import AuthService


PASSWORD = "benchmark-password-123"
COVER_LETTER = (
    "Saya tertarik mengikuti program ini karena pengalaman akademik dan proyek "
    "saya relevan dengan kebutuhan posisi. "
    * 9
).strip()


@dataclass(frozen=True)
class BenchmarkResult:
    name: str
    iterations: int
    mean_ms: float
    median_ms: float
    p95_ms: float
    min_ms: float
    max_ms: float


@dataclass(frozen=True)
class ComparisonResult:
    name: str
    before: BenchmarkResult
    after: BenchmarkResult


def percentile(values: list[float], pct: float) -> float:
    if not values:
        return 0.0
    ordered = sorted(values)
    index = int(round((len(ordered) - 1) * pct))
    return ordered[index]


def time_operation(name: str, iterations: int, fn: Callable[[], None]) -> BenchmarkResult:
    durations: list[float] = []
    for _ in range(iterations):
        start = time.perf_counter_ns()
        fn()
        elapsed_ms = (time.perf_counter_ns() - start) / 1_000_000
        durations.append(elapsed_ms)

    return BenchmarkResult(
        name=name,
        iterations=iterations,
        mean_ms=statistics.fmean(durations),
        median_ms=statistics.median(durations),
        p95_ms=percentile(durations, 0.95),
        min_ms=min(durations),
        max_ms=max(durations),
    )


def canonical_json(payload: dict) -> bytes:
    return json.dumps(payload, sort_keys=True, separators=(",", ":")).encode("utf-8")


def ratio_text(after: float, before: float) -> str:
    if before <= 0:
        return "n/a"
    return f"{after / before:.1f}x"


def print_comparison_table(results: list[ComparisonResult]) -> None:
    headers = ("Use case", "Before mean ms", "After mean ms", "Delta ms", "Ratio")
    rows = []
    for result in results:
        delta = result.after.mean_ms - result.before.mean_ms
        rows.append(
            (
                result.name,
                f"{result.before.mean_ms:.4f}",
                f"{result.after.mean_ms:.4f}",
                f"{delta:.4f}",
                ratio_text(result.after.mean_ms, result.before.mean_ms),
            )
        )
    print_rows(headers, rows)


def print_table(results: list[BenchmarkResult]) -> None:
    headers = ("Operation", "n", "mean ms", "median ms", "p95 ms", "min ms", "max ms")
    rows = [
        (
            result.name,
            str(result.iterations),
            f"{result.mean_ms:.3f}",
            f"{result.median_ms:.3f}",
            f"{result.p95_ms:.3f}",
            f"{result.min_ms:.3f}",
            f"{result.max_ms:.3f}",
        )
        for result in results
    ]
    print_rows(headers, rows)


def print_rows(headers: tuple[str, ...], rows: list[tuple[str, ...]]) -> None:
    widths = [
        max(len(headers[index]), *(len(row[index]) for row in rows))
        for index in range(len(headers))
    ]

    def fmt_row(row: tuple[str, ...]) -> str:
        return "  ".join(value.ljust(widths[index]) for index, value in enumerate(row))

    print(fmt_row(headers))
    print(fmt_row(tuple("-" * width for width in widths)))
    for row in rows:
        print(fmt_row(row))


def main() -> None:
    parser = argparse.ArgumentParser(description="Benchmark operasi keamanan TUMBUH.")
    parser.add_argument("--fast-iterations", type=int, default=1000)
    parser.add_argument("--bcrypt-iterations", type=int, default=10)
    parser.add_argument("--warmup", type=int, default=5)
    args = parser.parse_args()

    token_data = {"sub": "1", "role": "student"}
    access_token = AuthService.create_access_token(token_data)
    password_hash = AuthService.hash_password(PASSWORD)

    fernet = Fernet(Fernet.generate_key())
    encrypted_letter = fernet.encrypt(COVER_LETTER.encode("utf-8"))
    stored_encrypted_letter = b"enc:v1:" + encrypted_letter
    private_key = Ed25519PrivateKey.generate()
    public_key = private_key.public_key()
    signature_payload = {
        "action": "APPLICATION_SUBMIT",
        "actor_id": 1,
        "student_id": 1,
        "opportunity_id": 7,
        "status": "Applied",
        "timestamp": "2026-06-26T00:00:00+07:00",
    }
    signature = private_key.sign(canonical_json(signature_payload))

    def jwt_encode_pair() -> None:
        AuthService.create_access_token(token_data)
        AuthService.create_refresh_token(token_data)

    def jwt_decode_access() -> None:
        AuthService.decode_token(access_token)

    def bcrypt_verify() -> None:
        AuthService.verify_password(PASSWORD, password_hash)

    def fernet_encrypt() -> None:
        fernet.encrypt(COVER_LETTER.encode("utf-8"))

    def fernet_decrypt() -> None:
        fernet.decrypt(encrypted_letter)

    def ed25519_sign() -> None:
        private_key.sign(canonical_json(signature_payload))

    def ed25519_verify() -> None:
        public_key.verify(signature, canonical_json(signature_payload))

    def before_login_path() -> None:
        if PASSWORD != "benchmark-password-123":
            raise RuntimeError("unexpected password mismatch")
        {"access_token": "access", "refresh_token": "refresh"}

    def login_crypto_path() -> None:
        AuthService.verify_password(PASSWORD, password_hash)
        AuthService.create_access_token(token_data)
        AuthService.create_refresh_token(token_data)

    def before_submit_path() -> None:
        {
            "cover_letter": COVER_LETTER,
            "signature_payload": None,
            "digital_signature": None,
        }

    def submit_crypto_path() -> None:
        AuthService.decode_token(access_token)
        fernet.encrypt(COVER_LETTER.encode("utf-8"))
        private_key.sign(canonical_json(signature_payload))

    def before_read_path() -> None:
        str(COVER_LETTER)

    def read_crypto_path() -> None:
        AuthService.decode_token(access_token)
        fernet.decrypt(encrypted_letter)

    for _ in range(args.warmup):
        before_login_path()
        before_submit_path()
        before_read_path()
        jwt_encode_pair()
        jwt_decode_access()
        bcrypt_verify()
        fernet_encrypt()
        fernet_decrypt()
        ed25519_sign()
        ed25519_verify()
        submit_crypto_path()
        read_crypto_path()

    comparisons = [
        ComparisonResult(
            "Login path",
            time_operation("Before login path", args.fast_iterations, before_login_path),
            time_operation("After login path", args.bcrypt_iterations, login_crypto_path),
        ),
        ComparisonResult(
            "Submit path",
            time_operation("Before submit path", args.fast_iterations, before_submit_path),
            time_operation("After submit path", args.fast_iterations, submit_crypto_path),
        ),
        ComparisonResult(
            "Read path",
            time_operation("Before read path", args.fast_iterations, before_read_path),
            time_operation("After read path", args.fast_iterations, read_crypto_path),
        ),
    ]
    component_results = [
        time_operation("bcrypt verify", args.bcrypt_iterations, bcrypt_verify),
        time_operation("JWT encode access+refresh", args.fast_iterations, jwt_encode_pair),
        time_operation("JWT decode access", args.fast_iterations, jwt_decode_access),
        time_operation("Fernet encrypt cover letter", args.fast_iterations, fernet_encrypt),
        time_operation("Fernet decrypt cover letter", args.fast_iterations, fernet_decrypt),
        time_operation("Ed25519 sign payload", args.fast_iterations, ed25519_sign),
        time_operation("Ed25519 verify payload", args.fast_iterations, ed25519_verify),
        time_operation("Login crypto path", args.bcrypt_iterations, login_crypto_path),
        time_operation("Submit crypto path", args.fast_iterations, submit_crypto_path),
        time_operation("Read crypto path", args.fast_iterations, read_crypto_path),
    ]

    raw_bytes = len(COVER_LETTER.encode("utf-8"))
    encrypted_bytes = len(stored_encrypted_letter)

    print("TUMBUH security benchmark")
    print("Before baseline: plaintext password compare, plaintext cover letter, no JWT, no Fernet, no Ed25519.")
    print("After baseline: current security operations only, without database or network calls.")
    print()
    print(f"Cover letter raw bytes:       {raw_bytes}")
    print(f"Cover letter encrypted bytes: {encrypted_bytes}")
    print(f"Encryption size overhead:     {encrypted_bytes - raw_bytes} bytes ({encrypted_bytes / raw_bytes:.2f}x)")
    print()
    print("Before vs after")
    print_comparison_table(comparisons)
    print()
    print("After component breakdown")
    print_table(component_results)


if __name__ == "__main__":
    main()
