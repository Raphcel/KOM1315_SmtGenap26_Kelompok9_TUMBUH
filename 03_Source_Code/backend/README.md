# Backend Security Modules

Backend TUMBUH berada di `be-web/` dan menggunakan FastAPI sebagai API boundary.

## Modul Utama

| Modul | Fungsi |
|---|---|
| `be-web/app/services/auth_service.py` | Register, login, JWT access/refresh token, bcrypt password hashing, email verification, password reset. |
| `be-web/app/api/dependencies.py` | Dependency injection, current-user resolution, dan role-based access control. |
| `be-web/app/services/security_service.py` | Fernet field encryption dan Ed25519 digital signatures. |
| `be-web/app/services/audit_service.py` | Pengiriman event accounting ke audit-log service. |
| `audit-log/server.js` | Winston audit-log server untuk menyimpan event keamanan. |

## Enkripsi Field

`SecurityService.encrypt_text()` mengenkripsi data sensitif sebelum disimpan. Saat data dibaca, `SecurityService.decrypt_text()` mengembalikan plaintext untuk response API.

Contoh penggunaan ada di `be-web/app/services/application_service.py`, tempat `cover_letter` aplikasi mahasiswa dienkripsi sebelum persist dan didekripsi saat response dibuat.

## Authentication

Authentication dilakukan di `AuthService`:

- Password disimpan sebagai bcrypt hash.
- Login gagal mengembalikan `401`.
- Akun yang belum verifikasi email atau nonaktif mengembalikan `403`.
- JWT access token membawa `sub`, `role`, `exp`, dan `type`.
- Refresh token tidak boleh dipakai sebagai token request API biasa.

## Authorization

Role check dilakukan di backend melalui `require_role(required_role)` pada `be-web/app/api/dependencies.py`. Route student, HR, dan admin menggunakan dependency ini agar proteksi tidak bergantung pada frontend saja.

## Accounting

Aktivitas penting seperti register, login, perubahan aplikasi, dan operasi admin memanggil `audit_log()`. Event dikirim ke audit-log service secara background agar request API tidak tertahan ketika audit service sedang tidak tersedia.
