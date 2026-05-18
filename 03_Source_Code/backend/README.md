# Backend Security Integration

Folder ini digunakan untuk kode atau dokumentasi implementasi keamanan pada sisi backend TUMBUH.

## Cakupan

- Alur login dan validasi identitas pengguna.
- Penerbitan dan validasi token autentikasi.
- Role-based access control untuk mahasiswa, HR, dan admin.
- Ownership check untuk data profil, lowongan, perusahaan, dan lamaran.
- Audit logging untuk aktivitas penting.
- Integrasi fungsi `encrypt()` dan `decrypt()` pada workflow utama aplikasi.

## Bukti yang Diharapkan

- Kode backend yang menunjukkan pemisahan Authentication, Authorization, dan Accounting.
- Contoh konfigurasi yang aman dan tidak berisi secret asli.
- Catatan integrasi keamanan dengan endpoint atau service utama.
- Referensi ke hasil pengujian pada folder `05_Testing_Logs/`.
