# AAA Integration

Dokumen ini menjelaskan pemisahan Authentication, Authorization, dan Accounting pada backend TUMBUH.

## Authentication

Authentication berada di `be-web/app/services/auth_service.py`.

Implementasi utama:

- `hash_password()` membuat bcrypt hash dengan salt otomatis dari `bcrypt.gensalt()`.
- `verify_password()` membandingkan plaintext password dengan hash yang tersimpan.
- `login()` memvalidasi kredensial, status verifikasi email, dan status aktif akun.
- `create_access_token()` dan `create_refresh_token()` menerbitkan JWT bertipe berbeda.
- `get_current_user()` menolak refresh token untuk akses route biasa dan mengambil user aktif berdasarkan `sub`.

Failure behavior:

- Kredensial salah: `401 Unauthorized`.
- Email belum diverifikasi: `403 Forbidden`.
- Akun nonaktif: `403 Forbidden`.

## Authorization

Authorization berada di `be-web/app/api/dependencies.py`.

Implementasi utama:

- `get_current_user()` membaca token bearer dan mengembalikan user aktif.
- `require_role(required_role)` membuat FastAPI dependency untuk role-based access control.
- Route admin menggunakan `Depends(require_role("admin"))`.
- Route HR menggunakan `Depends(require_role("hr"))`.
- Route student menggunakan `Depends(require_role("student"))`.

Contoh route yang memakai RBAC:

- `be-web/app/api/routes/admin.py`
- `be-web/app/api/routes/applications.py`
- `be-web/app/api/routes/opportunities.py`
- `be-web/app/api/routes/logbooks.py`

## Accounting

Accounting berada di `be-web/app/services/audit_service.py` dan `audit-log/`.

Implementasi utama:

- `audit_log()` membentuk payload event berisi action, level, user, resource, detail, dan status sukses/gagal.
- Payload dikirim ke audit-log service menggunakan request HTTP background thread.
- Kegagalan audit service tidak menggagalkan request utama, tetapi dicatat di log backend.

Event yang sudah dicatat di backend antara lain:

- `AUTH_REGISTER`
- `AUTH_REGISTER_DUPLICATE`
- `AUTH_LOGIN_SUCCESS`
- `AUTH_LOGIN_FAILURE`
- `AUTH_LOGIN_BLOCKED`
- `AUTH_EMAIL_VERIFY`

## Kesimpulan

TUMBUH memisahkan AAA sebagai berikut:

| Layer | Lokasi | Tanggung jawab |
|---|---|---|
| Authentication | `auth_service.py` | Identitas user, password, token, status akun. |
| Authorization | `dependencies.py` + route modules | Pembatasan akses berdasarkan role. |
| Accounting | `audit_service.py` + `audit-log/` | Pencatatan aktivitas keamanan dan audit trail. |
