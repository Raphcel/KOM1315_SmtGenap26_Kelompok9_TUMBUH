# Digital Signature: Ed25519

TUMBUH menggunakan Ed25519 untuk tanda tangan digital pada event aplikasi, sehingga perubahan status aplikasi dapat diverifikasi kembali.

## Source

Implementasi utama berada di `be-web/app/services/security_service.py`.

Bagian penting:

- `sign_payload(payload)` membuat canonical JSON lalu menandatanganinya dengan private key Ed25519.
- `verify_signature(payload, signature)` memverifikasi signature memakai public key.
- `build_application_signature_payload()` membentuk payload standar untuk event aplikasi.
- `public_key_pem()` menyediakan public key untuk verifikasi.

## Alur Implementasi

1. Backend membuat payload dengan field `action`, `actor_id`, `student_id`, `opportunity_id`, `status`, dan `timestamp`.
2. Payload diubah menjadi canonical JSON dengan urutan key stabil.
3. Private key Ed25519 menandatangani canonical JSON.
4. Signature disimpan bersama payload dan nama algorithm.
5. Admin verification membaca payload tersimpan dan memanggil `verify_signature()`.

## File Terkait

| File | Peran |
|---|---|
| `be-web/app/services/security_service.py` | Implementasi sign/verify dan key loading. |
| `be-web/app/services/application_service.py` | Membuat signature saat event aplikasi. |
| `be-web/app/services/admin_service.py` | Verifikasi signature aplikasi. |
| `be-web/tests/test_security_service.py` | Test signature valid dan deteksi tampering. |

## Catatan Keamanan

- Private key tidak boleh dikomit ke Git.
- `DIGITAL_SIGNATURE_PRIVATE_KEY` harus berasal dari environment untuk deployment.
- File deliverable ini hanya berisi logic dan dokumentasi, bukan nilai key.
