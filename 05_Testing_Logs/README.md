# 05 Testing Logs

Folder ini berisi bukti pengujian keamanan untuk implementasi TUMBUH. Luaran ini terutama mendukung target minggu 11-12, yaitu finalisasi protokol AAA dan pengujian end-to-end.

## Bukti Pengujian yang Diharapkan

- Pengujian Authentication: login berhasil, login gagal, token tidak valid, dan token kedaluwarsa.
- Pengujian Authorization: pengguna tanpa hak akses gagal mengakses data atau endpoint terlarang.
- Pengujian Accounting: aktivitas penting tercatat pada audit log.
- Pengujian password hashing dan salting.
- Pengujian enkripsi dan dekripsi data sensitif.
- Pengujian digital signature dan verifikasi tanda tangan.
- Pengujian end-to-end alur utama aplikasi setelah integrasi AAA.

## Bukti hasil testing

File-file berikut memuat bukti pengujian yang telah selesai dilakukan (hasil test, snippet code, dll.):
- [security_test_log.md](./security_test_log.md)
- [unit_test_results.md](./unit_test_results.md)
- [auth_test_log.md](./auth_test_log.md)
- [authorization_test_log.md](./authorization_test_log.md)
- [accounting_test_log.md](./accounting_test_log.md)

## Referensi

Test otomatis backend tersedia di `be-web/tests/`.
