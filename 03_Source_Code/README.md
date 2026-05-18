# 03 Source Code

Folder ini berisi implementasi teknis keamanan informasi pada sistem TUMBUH. Source code yang ditempatkan di sini harus menunjukkan bahwa modul keamanan sudah terintegrasi ke alur utama aplikasi, bukan hanya berupa skrip terpisah.

## Fokus Implementasi

- Authentication untuk memastikan identitas pengguna.
- Authorization untuk membatasi akses berdasarkan role dan ownership.
- Accounting untuk mencatat aktivitas penting sebagai audit trail.
- Enkripsi dan dekripsi data sensitif.
- Password hashing dan salting.
- Digital signature untuk integritas dan non-repudiation.

## Struktur

| Folder | Keterangan |
|---|---|
| `backend/` | Integrasi keamanan pada backend dan workflow utama aplikasi |
| `database/` | Skema database, catatan kolom sensitif, hashing/salting, dan migrasi keamanan |
| `digital_signature/` | Implementasi kriptografi asimetris dan tanda tangan digital |
| `src/auth/` | Modul autentikasi, otorisasi, dan integrasi non-repudiation |
