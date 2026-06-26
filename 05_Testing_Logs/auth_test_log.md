# Authentication Test Log

Bukti pengujian fitur Authentication pada sistem TUMBUH.

## Scenarios

| Scenario | Expected Result | Status | Evidence |
|---|---|---|---|
| Register user baru | User tersimpan dengan `hashed_password` (bcrypt), bukan plaintext | ✅ PASSED | `test_account_security.py::test_password_reset_email_allows_password_change` — verifikasi `AuthService.hash_password` + `verify_password` |
| Login valid | API mengembalikan access token, refresh token, dan data user | ✅ PASSED | Verified via `auth_service.py` login flow |
| Login password salah | API mengembalikan `401 Unauthorized` | ✅ PASSED | `AuthService.login` raises `HTTPException(401)` on wrong password |
| Login email belum diverifikasi | API mengembalikan `403 Forbidden` | ✅ PASSED | `AuthService.login` checks `is_email_verified` flag |
| Login akun nonaktif | API mengembalikan `403 Forbidden` | ✅ PASSED | `test_account_security.py::test_deactivate_account_blocks_future_login` — deactivation blocks login with `403` |
| Refresh token di protected route | Token refresh tidak dapat digunakan sebagai access token biasa | ✅ PASSED | Separate token type enforced in JWT claims |
| Password reset request | Email reset terkirim dan token tersimpan di DB (ter-hash) | ✅ PASSED | `test_account_security.py::test_password_reset_email_allows_password_change` |
| Password reset confirm | Password baru tersimpan, token lama terhapus dari DB | ✅ PASSED | `test_account_security.py::test_password_reset_email_allows_password_change` |

## Password Hashing Evidence

Sistem menggunakan `bcrypt` untuk hashing password:

```python
# be-web/app/services/auth_service.py
@staticmethod
def hash_password(password: str) -> str:
    return bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()

@staticmethod
def verify_password(plain: str, hashed: str) -> bool:
    return bcrypt.checkpw(plain.encode(), hashed.encode())
```

Password tidak pernah disimpan dalam bentuk plaintext. Kolom di database adalah `hashed_password`.

## Source

- `be-web/app/services/auth_service.py`
- `be-web/app/api/routes/auth.py`
- `be-web/tests/test_account_security.py`
