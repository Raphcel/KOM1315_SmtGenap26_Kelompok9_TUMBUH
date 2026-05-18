# KOM1315_SmtGenap26_Kelompok9_TUMBUH

Repositori ini digunakan untuk pengelolaan progres Proyek PBL mata kuliah **KOM1315 Keamanan Informasi**. Sistem yang digunakan adalah **TUMBUH**, yaitu aplikasi web *Career & Internship Tracker* untuk mahasiswa IPB, HR perusahaan, dan admin platform.

Repositori ini disusun untuk mendokumentasikan proses analisis, perancangan, implementasi, pengujian, dan pelaporan integrasi keamanan informasi pada sistem TUMBUH, khususnya penerapan **AAA Security**:

- **Authentication**: verifikasi identitas pengguna.
- **Authorization**: pembatasan akses berdasarkan peran dan kepemilikan data.
- **Accounting**: pencatatan aktivitas pengguna sebagai audit trail.

## Identitas Proyek

| Komponen | Keterangan |
|---|---|
| Mata kuliah | KOM1315 Keamanan Informasi |
| Semester | Semester Genap 2026 |
| Kelompok | Kelompok 9 |
| Nama sistem | TUMBUH |
| Format nama repositori | `KOM1315_SmtGenap26_Kelompok9_TUMBUH` |
| Fokus keamanan | AAA Security, password hashing, enkripsi data sensitif, digital signature, dan security testing |

## Akses Dosen

Setelah repositori dibuat di GitHub atau GitLab, dosen pengajar perlu ditambahkan sebagai **Collaborator** atau **Maintainer**:

- `shelvie.neyman@gmail.com` - Dr. Shelvie Nidya Neyman
- `endang.p.giri@gmail.com` - Endang P. Giri, S.Kom, M.Kom

## Struktur Folder Repositori

Struktur folder mengikuti instruksi pengelolaan repositori Git untuk Proyek PBL:

```text
.
├── 01_Proposal_&_Analisis/
│   ├── Proposal_Teknis.md
│   ├── Proposal_Teknis_TUMBUH.pdf
│   ├── Threat_Modeling.md
│   └── Threat_Modeling_TUMBUH.pdf
├── 02_Design_Documents/
│   ├── ERD_Modified.png
│   ├── Architecture_Diagram.pdf
│   └── Testing_Plan.pdf
├── 03_Source_Code/
│   ├── backend/
│   ├── database/
│   ├── digital_signature/
│   └── src/
│       └── auth/
├── 04_Reports_&_Paper/
│   ├── Monitoring_P7/
│   ├── Final_Technical_Report/
│   └── Scientific_Paper/
├── 05_Testing_Logs/
└── README.md
```

## Deskripsi Folder

| Folder | Isi utama |
|---|---|
| `01_Proposal_&_Analisis/` | Proposal teknis, deskripsi sistem TUMBUH, identifikasi aset data, threat modeling, dan analisis risiko awal |
| `02_Design_Documents/` | Dokumen rancangan keamanan, ERD yang dimodifikasi, diagram arsitektur, dan rencana pengujian AAA |
| `03_Source_Code/` | Implementasi modul keamanan, termasuk authentication, authorization, accounting, kriptografi, dan digital signature |
| `04_Reports_&_Paper/` | Laporan monitoring, laporan teknis akhir, user manual, paper ilmiah, dan bukti submit/LoA jika ada |
| `05_Testing_Logs/` | Bukti pengujian keamanan, unit test, integration test, dan log pengujian end-to-end |

## Sinkronisasi Tahapan PBL

| Minggu | Aktivitas Git | Target luaran |
|---|---|---|
| Minggu 2 | Init repository | Upload proposal dan existing system analysis |
| Minggu 5 | Coding sprint | Integrasi fungsi `encrypt()` dan `decrypt()` pada backend |
| Minggu 7 | Monitoring | Push laporan kemajuan Bab 1-3 dan bukti demo |
| Minggu 10 | Security update | Implementasi password hashing dan digital signature |
| Minggu 12 | Integration | Finalisasi protokol AAA dan log pengujian end-to-end |
| Minggu 15 | Final release | Upload paper ilmiah format JIKA dan versi aplikasi stabil |

## Strategi Catch-up

Karena repositori dibuat setelah minggu awal perkuliahan, progres minggu 1-7 dilakukan dengan strategi **retroactive upload**:

1. Mengunggah seluruh dokumen yang sudah dikerjakan ke folder yang sesuai.
2. Menjadikan commit awal sebagai baseline proyek.
3. Melanjutkan aktivitas commit secara progresif mulai minggu berikutnya.
4. Setiap anggota kelompok melakukan commit sesuai bagian pekerjaannya agar kontribusi individu terlihat.

## Fokus Implementasi Keamanan

Implementasi keamanan pada TUMBUH diarahkan pada:

- Pemisahan yang jelas antara Authentication, Authorization, dan Accounting.
- Penyimpanan password menggunakan hashing dan salting.
- Pembatasan akses berbasis role: mahasiswa, HR, dan admin.
- Pencatatan aktivitas penting pengguna melalui audit log.
- Perlindungan data sensitif menggunakan enkripsi.
- Penerapan digital signature untuk menjaga integritas dan non-repudiation pada aksi penting.
- Pengujian keamanan yang terdokumentasi di folder `05_Testing_Logs/`.

## Catatan Keamanan

- Jangan pernah melakukan commit kunci kriptografi asli.
- Jangan melakukan commit file `.env` yang berisi secret.
- Jangan menyimpan private key, JWT secret, database password, atau credential lain di source code.
- Gunakan file konfigurasi lokal yang masuk `.gitignore`.
- Gunakan contoh konfigurasi yang sudah disanitasi apabila perlu dokumentasi.

## Tenggat Akhir

Seluruh artefak akhir, termasuk laporan, paper ilmiah, bukti submit/LoA jika ada, dan versi aplikasi stabil, harus sudah tersedia di repositori paling lambat **26 Juni 2026**.
