# Database Security: Password Hashing and Salting

TUMBUH menyimpan password dalam bentuk bcrypt hash, bukan plaintext.

## Source

Implementasi utama berada di `be-web/app/services/auth_service.py`:

```python
@staticmethod
def hash_password(password: str) -> str:
    return _bcrypt.hashpw(password.encode("utf-8"), _bcrypt.gensalt()).decode("utf-8")

@staticmethod
def verify_password(plain: str, hashed: str) -> bool:
    return _bcrypt.checkpw(plain.encode("utf-8"), hashed.encode("utf-8"))
```

## Mekanisme

- `bcrypt.gensalt()` membuat salt acak untuk setiap password.
- `bcrypt.hashpw()` menghasilkan hash yang sudah menyertakan metadata algorithm, cost, dan salt.
- `bcrypt.checkpw()` memverifikasi password login tanpa mendekripsi hash.

## Alur Register dan Login

| Alur | Langkah keamanan |
|---|---|
| Register | Password dari request tidak disimpan langsung. Backend menyimpan `hashed_password`. |
| Login | Password input dibandingkan dengan `hashed_password` memakai bcrypt. |
| Password reset | Password baru kembali di-hash sebelum disimpan. |

## Catatan Keamanan

- Hash bcrypt bukan enkripsi dan tidak dapat didekripsi.
- Salt tidak perlu disimpan terpisah karena sudah berada di string hash bcrypt.
- Password plaintext tidak boleh masuk log, response API, atau dokumen deliverable.
