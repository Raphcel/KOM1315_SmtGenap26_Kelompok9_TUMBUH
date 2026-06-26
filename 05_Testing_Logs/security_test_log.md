# Security Test Log

Ringkasan pengujian keamanan sistem TUMBUH untuk deliverable Minggu 12.

## Test Results Summary

| Area | Expected Result | Status | Source / Bukti |
|---|---|---|---|
| Field encryption | Data sensitif tersimpan dengan prefix `enc:v1:` dan dapat didekripsi oleh service | ✅ PASSED | `test_security_service.py::test_encrypt_decrypt_text_roundtrip` |
| Signature verification — valid payload | Payload asli terverifikasi dengan signature | ✅ PASSED | `test_security_service.py::test_digital_signature_detects_tampering` |
| Signature verification — tampered payload | Payload yang diubah gagal verifikasi | ✅ PASSED | `test_security_service.py::test_digital_signature_detects_tampering` |
| Authentication failure — wrong password | Login password salah mengembalikan `401` | ✅ PASSED | `test_account_security.py` + `auth_service.py` |
| Authentication failure — inactive account | Akun nonaktif mengembalikan `403` | ✅ PASSED | `test_account_security.py::test_deactivate_account_blocks_future_login` |
| Authorization failure — wrong role | User dengan role salah mengembalikan `403` | ✅ PASSED | `test_logbooks.py::test_logbook_endpoints_are_student_only` |
| Authorization failure — wrong owner | HR mengakses data perusahaan lain → `403` | ✅ PASSED | `test_organizations.py::test_recruiter_can_manage_only_their_own_opportunity` |
| Accounting | Event auth dan aktivitas penting masuk audit log dengan hash chain | ✅ VERIFIED | `accounting_test_log.md` + `audit-log/logs/` |
| Password hashing | Password tersimpan sebagai bcrypt hash, bukan plaintext | ✅ PASSED | `test_account_security.py::test_password_reset_email_allows_password_change` |
| Password reset flow | Token reset ter-hash di DB, dihapus setelah digunakan | ✅ PASSED | `test_account_security.py::test_password_reset_email_allows_password_change` |
| Account deletion | Penghapusan akun menghapus semua data terkait (notifikasi, draft) | ✅ PASSED | `test_account_security.py::test_delete_account_requires_matching_email_and_removes_owned_rows` |

## Automated Test Coverage

```
be-web/tests/test_security_service.py   — 2 tests  (encryption + digital signature)
be-web/tests/test_account_security.py  — 3 tests  (password reset, deactivation, deletion)
be-web/tests/test_alembic_migrations.py— 1 test   (migration graph)
be-web/tests/test_logbooks.py          — 6 tests  (authorization, ownership)
be-web/tests/test_notifications.py     — 18 tests (RBAC, notification workflows)
be-web/tests/test_organizations.py     — 5 tests  (HR permissions, org management)
be-web/tests/test_user_schema.py       — 4 tests  (schema validation)

Total: 39 tests — ALL PASSED (2026-06-26)
```

## Encryption Implementation Evidence

```python
# be-web/app/services/security_service.py
def encrypt_text(self, plaintext: str) -> str:
    token = self.fernet.encrypt(plaintext.encode())
    return ENCRYPTED_PREFIX + token.decode()  # "enc:v1:..."

def decrypt_text(self, ciphertext: str) -> str:
    if not ciphertext.startswith(ENCRYPTED_PREFIX):
        return ciphertext
    token = ciphertext[len(ENCRYPTED_PREFIX):]
    return self.fernet.decrypt(token.encode()).decode()
```

Fernet menggunakan AES-128 dalam mode CBC + HMAC-SHA256 untuk authenticated encryption.

## Digital Signature Evidence

```python
# be-web/app/services/security_service.py
def sign_payload(self, payload: dict) -> str:
    message = json.dumps(payload, sort_keys=True).encode()
    return base64.b64encode(self.private_key.sign(message)).decode()

def verify_signature(self, payload: dict, signature: str) -> bool:
    message = json.dumps(payload, sort_keys=True).encode()
    sig_bytes = base64.b64decode(signature)
    self.public_key.verify(sig_bytes, message)  # raises on failure
    return True
```

Algoritma: **Ed25519** (EdDSA) — digunakan untuk menandatangani event `APPLICATION_SUBMIT` dan `APPLICATION_STATUS_UPDATE`.
