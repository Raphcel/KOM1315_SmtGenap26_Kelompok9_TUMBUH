# Accounting Test Log

Bukti pengujian fitur Accounting / Audit Logging pada sistem TUMBUH.

## Arsitektur Accounting

Sistem TUMBUH menggunakan layanan audit terpisah (`audit-log/`) yang menerima event dari backend FastAPI secara asynchronous. Setiap event memiliki SHA-256 hash chain untuk tamper detection.

## Event Types Tercatat

| Event | Trigger | Status | Contoh dari Log |
|---|---|---|---|
| `AUDIT_SERVER_START` | Audit service startup | ✅ VERIFIED | Lihat `audit-log/logs/audit-2026-06-04.log` |
| `AUTH_LOGIN_SUCCESS` | Login berhasil | ✅ IMPLEMENTED | `be-web/app/services/auth_service.py` |
| `AUTH_LOGIN_FAILURE` | Password salah atau akun nonaktif | ✅ IMPLEMENTED | `be-web/app/services/auth_service.py` |
| `AUTH_REGISTER` | Registrasi user baru | ✅ IMPLEMENTED | `be-web/app/services/auth_service.py` |
| `AUTH_EMAIL_VERIFY` | Verifikasi email berhasil | ✅ IMPLEMENTED | `be-web/app/services/auth_service.py` |
| `APPLICATION_SUBMIT` | Student submit lamaran | ✅ IMPLEMENTED + SIGNED | `be-web/app/services/application_service.py` |
| `APPLICATION_STATUS_UPDATE` | HR update status lamaran | ✅ IMPLEMENTED + SIGNED | `be-web/app/services/application_service.py` |
| `PROFILE_UPDATE` | User update profil | ✅ IMPLEMENTED | `be-web/app/services/user_service.py` |
| `COMPANY_UPDATE` | HR update profil perusahaan | ✅ IMPLEMENTED | `be-web/app/services/company_service.py` |
| `OPPORTUNITY_CREATE` | HR buat lowongan baru | ✅ IMPLEMENTED | `be-web/app/services/opportunity_service.py` |
| `NOTIFICATION_CREATE` | Notifikasi dikirim ke user | ✅ IMPLEMENTED | `be-web/app/services/notification_service.py` |

## Hash Chain Evidence

Setiap audit log entry memiliki SHA-256 hash chain untuk tamper evidence:

```json
{
  "action": "AUDIT_SERVER_START",
  "eventHash": "82697240b950ef12f65029be6022f65259ddf65297d31c0c7fd17589fc4764d6",
  "previousHash": "859b0b9c957712947b22b1a273b0c617a80ebed516d361b7d526ee304f720d86",
  "integrityAlgorithm": "SHA-256 hash chain",
  "service": "tumbuh-audit",
  "timestamp": "2026-06-04 00:08:41.451",
  "userRole": "system",
  "success": true
}
```

Source: `audit-log/logs/audit-2026-06-04.log`

## Audit Log Fields

Setiap entry mengandung:
- `action` — jenis event
- `userId`, `userEmail`, `userRole` — identitas aktor
- `resource`, `resourceId` — objek yang dipengaruhi
- `success` — apakah operasi berhasil
- `timestamp` — waktu dalam format WIB 24 jam
- `previousHash` + `eventHash` — SHA-256 hash chain untuk tamper evidence
- `ip` — IP address request (jika tersedia)

## Source

- `be-web/app/services/audit_service.py`
- `audit-log/server.js`
- `audit-log/logs/`
