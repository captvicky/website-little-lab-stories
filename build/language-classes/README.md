# Language Classes — generator halaman

Halaman ini **dibangun dari satu generator**, bukan diedit satu per satu, supaya tiga bahasa
(EN / ID / RU) selalu punya struktur yang sama.

## Cara mengubah isi
1. Buka `build.py`.
2. Teks tiap bahasa ada di kamus `C["en"]`, `C["id"]`, `C["ru"]`. Ubah teksnya di sana
   (jangan mengedit file HTML hasil generate — akan tertimpa).
3. Jalankan:
   ```bash
   cd build/language-classes
   python3 build.py
   ```
4. Hasilnya ditulis ke `Little lab stories/`:
   - `language-classes.html` (English, default)
   - `language-classes-id.html` (Bahasa Indonesia)
   - `language-classes-ru.html` (Русский)
5. Commit + push ke `main` → Vercel auto-deploy.

## Catatan
- Halaman memakai satu stylesheet bersama: `Little lab stories/language-classes.css`.
- Bagian promo di homepage (`index.html`) memakai `Little lab stories/language-promo.css`
  dan **tidak** dihasilkan oleh generator ini (diedit langsung di `index.html`).
- Gambar ada di `Little lab stories/images/lang/` (hero + 3 landmark dari brosur,
  2 foto pengajar dari website lama).
- Nomor WhatsApp tujuan ada di konstanta `WA_NUMBER` (build.py).
