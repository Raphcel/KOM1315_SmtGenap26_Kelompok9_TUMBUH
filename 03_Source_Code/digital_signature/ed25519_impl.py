"""Sanitized Ed25519 signing excerpt from TUMBUH SecurityService.

This file is included for the KOM1315 source-code deliverable. It contains no
private key material. Callers must provide key objects from a secure source.
"""

from __future__ import annotations

import base64
import json
from typing import Any

from cryptography.hazmat.primitives.asymmetric.ed25519 import Ed25519PrivateKey, Ed25519PublicKey


SIGNATURE_ALGORITHM = "Ed25519"


def canonical_json(payload: dict[str, Any]) -> str:
    """Return a stable JSON representation for signing and verification."""
    return json.dumps(payload, sort_keys=True, separators=(",", ":"), default=str)


def sign_payload(payload: dict[str, Any], private_key: Ed25519PrivateKey) -> str:
    """Sign a payload and return a URL-safe base64 signature string."""
    canonical = canonical_json(payload).encode("utf-8")
    signature = private_key.sign(canonical)
    return base64.urlsafe_b64encode(signature).decode("ascii")


def verify_signature(payload: dict[str, Any], signature: str, public_key: Ed25519PublicKey) -> bool:
    """Return True when the signature matches the canonical payload."""
    try:
        raw_signature = base64.urlsafe_b64decode(signature.encode("ascii"))
        public_key.verify(raw_signature, canonical_json(payload).encode("utf-8"))
        return True
    except Exception:
        return False


def build_application_signature_payload(
    *,
    action: str,
    student_id: int,
    opportunity_id: int,
    status: str,
    timestamp: str,
    actor_id: int | None = None,
) -> dict[str, Any]:
    """Build the application event payload signed by the backend."""
    return {
        "action": action,
        "actor_id": actor_id,
        "student_id": student_id,
        "opportunity_id": opportunity_id,
        "status": status,
        "timestamp": timestamp,
    }
