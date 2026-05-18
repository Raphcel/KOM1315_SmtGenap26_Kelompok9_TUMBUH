# Auth Source

Folder ini digunakan untuk modul autentikasi dan otorisasi yang mendukung implementasi AAA Security pada TUMBUH.

## Cakupan

- Authentication: login, validasi kredensial, token/session, dan proteksi endpoint.
- Authorization: role-based access control dan ownership check.
- Accounting hook: pemanggilan audit log untuk aktivitas penting.
- Integrasi digital signature jika aksi autentikasi atau perubahan data membutuhkan non-repudiation.

## Prinsip Implementasi

- Role pengguna tidak boleh dipercaya hanya dari input client.
- Setiap endpoint sensitif harus melakukan validasi token dan permission.
- Refresh token atau session harus memiliki masa berlaku dan validasi yang jelas.
- Error autentikasi tidak boleh membocorkan detail sensitif.
- Password tidak boleh disimpan atau dicatat dalam bentuk plaintext.

## Catatan

Modul pada folder ini harus mendukung pemisahan tanggung jawab antara Authentication, Authorization, dan Accounting agar sesuai dengan tujuan tugas Keamanan Informasi.
