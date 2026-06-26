# 03 Source Code

Folder ini berisi ringkasan dan cuplikan implementasi source code yang relevan dengan deliverable keamanan KOM1315.

## Struktur

| Folder | Isi |
|---|---|
| `backend/` | Dokumentasi modul keamanan backend dan integrasi AAA. |
| `database/` | Dokumentasi hashing/salting password dan cuplikan bcrypt. |
| `digital_signature/` | Dokumentasi tanda tangan digital Ed25519 dan cuplikan sign/verify. |

## Referensi Source Utama

| Area | File sumber |
|---|---|
| Backend API | `be-web/app/main.py`, `be-web/app/api/` |
| Authentication | `be-web/app/services/auth_service.py` |
| Authorization | `be-web/app/api/dependencies.py` |
| Accounting / audit log | `be-web/app/services/audit_service.py`, `audit-log/server.js` |
| Field encryption and signatures | `be-web/app/services/security_service.py` |
| Frontend | `fe-web/src/` |

## Batasan Keamanan

File di folder ini hanya berisi dokumentasi dan cuplikan kode aman. Jangan menambahkan `.env`, private key, token, database URL produksi, atau nilai `FIELD_ENCRYPTION_KEY` / `DIGITAL_SIGNATURE_PRIVATE_KEY`.
