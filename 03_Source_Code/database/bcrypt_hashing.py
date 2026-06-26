"""Sanitized bcrypt password hashing excerpt from TUMBUH AuthService.

This file is included for the KOM1315 source-code deliverable. It contains no
passwords, tokens, or environment-specific secret values.
"""

import bcrypt as _bcrypt


def hash_password(password: str) -> str:
    """Hash a plaintext password with bcrypt and an automatically generated salt."""
    return _bcrypt.hashpw(password.encode("utf-8"), _bcrypt.gensalt()).decode("utf-8")


def verify_password(plain: str, hashed: str) -> bool:
    """Verify a plaintext password against a stored bcrypt hash."""
    return _bcrypt.checkpw(plain.encode("utf-8"), hashed.encode("utf-8"))
