# Performance Benchmark Results

Dokumen ini mencatat benchmark kuantitatif untuk mengukur overhead kontrol
keamanan TUMBUH. Benchmark ini melengkapi bukti unit test dengan data kinerja
sebelum dan sesudah operasi keamanan inti.

## Command

```bash
cd 03_Source_Code/backend
uv run --with-requirements requirements.txt python scripts/benchmark_security.py --fast-iterations 1000 --bcrypt-iterations 10
```

## Method

Benchmark mengukur operasi keamanan tanpa akses database dan tanpa network call
agar biaya yang terlihat berfokus pada operasi kriptografi dan validasi token.

Baseline **before** bersifat sintetis:

- login menggunakan perbandingan password plaintext;
- submit lamaran menyimpan cover letter plaintext;
- read lamaran membaca cover letter plaintext;
- tidak ada JWT, Fernet, atau Ed25519.

Baseline **after** mengukur operasi keamanan yang digunakan dalam desain akhir:

- login: bcrypt password verification dan penerbitan JWT access/refresh token;
- submit lamaran: JWT decode, Fernet encryption, dan Ed25519 signing;
- read lamaran: JWT decode dan Fernet decryption.

Audit logging tidak dihitung karena event audit dikirim secara asynchronous.
Benchmark ini bukan pengganti load test end-to-end karena database, jaringan,
reverse proxy, dan frontend tidak ikut diukur.

## Result

Tanggal pengukuran: 2026-06-26

| Use case | Before mean ms | After mean ms | Delta ms | Ratio |
|---|---:|---:|---:|---:|
| Login path | 0.0002 | 276.4189 | 276.4187 | 1511567.9x |
| Submit path | 0.0002 | 0.1224 | 0.1222 | 814.9x |
| Read path | 0.0001 | 0.0625 | 0.0624 | 622.3x |

## Component Breakdown

| Operation | n | Mean ms | Median ms | P95 ms | Min ms | Max ms |
|---|---:|---:|---:|---:|---:|---:|
| bcrypt verify | 10 | 273.085 | 272.612 | 277.061 | 272.162 | 277.061 |
| JWT encode access+refresh | 1000 | 0.037 | 0.033 | 0.055 | 0.031 | 0.182 |
| JWT decode access | 1000 | 0.034 | 0.033 | 0.045 | 0.031 | 0.101 |
| Fernet encrypt cover letter | 1000 | 0.021 | 0.020 | 0.028 | 0.019 | 0.091 |
| Fernet decrypt cover letter | 1000 | 0.019 | 0.018 | 0.024 | 0.018 | 0.040 |
| Ed25519 sign payload | 1000 | 0.041 | 0.040 | 0.046 | 0.040 | 0.079 |
| Ed25519 verify payload | 1000 | 0.123 | 0.122 | 0.128 | 0.121 | 0.153 |
| Login crypto path | 10 | 273.509 | 273.091 | 276.400 | 272.488 | 276.400 |
| Submit crypto path | 1000 | 0.118 | 0.115 | 0.132 | 0.112 | 0.232 |
| Read crypto path | 1000 | 0.061 | 0.059 | 0.075 | 0.057 | 0.108 |

## Storage Overhead

| Field sample | Plaintext bytes | Encrypted bytes | Overhead |
|---|---:|---:|---:|
| Cover letter | 1007 | 1427 | +420 bytes / 1.42x |

## Interpretation

Biaya terbesar berada pada login karena bcrypt sengaja dibuat mahal secara
komputasi untuk memperlambat brute force. Overhead submit dan read tetap di
bawah 1 ms pada benchmark lokal, sehingga operasi Fernet, JWT decode, dan
Ed25519 signing tidak menjadi bottleneck utama. Overhead ukuran 1.42x masih
wajar untuk field teks pendek seperti cover letter, tetapi tetap perlu
diperhitungkan bila enkripsi diperluas ke field berukuran besar.
