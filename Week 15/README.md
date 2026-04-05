# Week 15: Aturan Dasar HTML & CSS yang Benar

## 📋 Deskripsi

Materi ini mengajarkan **aturan dasar penulisan HTML dan CSS yang benar**, termasuk struktur optimal, best practices, dan kesalahan umum yang harus dihindari. Dirancang khusus untuk siswa SMP kelas 7-9 dengan durasi pembelajaran 1 jam.

---

## 📂 File-file dalam Folder Ini

| File                | Deskripsi                                                          |
| ------------------- | ------------------------------------------------------------------ |
| `Week15.md`         | **Materi utama** - Panduan lengkap dengan penjelasan dan contoh    |
| `contoh-baik.html`  | Contoh HTML dengan struktur yang **BENAR** ✅                      |
| `style-baik.css`    | Contoh CSS dengan penulisan yang **BAIK** ✅                       |
| `contoh-buruk.html` | Contoh HTML dengan struktur yang **SALAH** ❌ (untuk perbandingan) |
| `README.md`         | File ini - Panduan untuk guru                                      |

---

## 🎯 Tujuan Pembelajaran

Setelah mengikuti materi ini, siswa mampu:

1. ✅ Menulis struktur HTML yang lengkap dan benar
2. ✅ Memahami pentingnya penutupan tag dan nesting yang rapi
3. ✅ Menggunakan indentasi untuk kode yang mudah dibaca
4. ✅ Menulis CSS dengan selector yang tepat (class vs ID)
5. ✅ Memahami external, internal, dan inline CSS
6. ✅ Menerapkan naming convention yang baik
7. ✅ Menghindari kesalahan umum dalam HTML & CSS

---

## ⏱️ Alokasi Waktu (Total: 60 menit)

| Bagian             | Durasi   | Aktivitas                             |
| ------------------ | -------- | ------------------------------------- |
| **Pembuka**        | 5 menit  | Review Week 14, pengenalan topik      |
| **HTML Rules**     | 20 menit | Struktur, tag, nesting, indentasi     |
| **CSS Rules**      | 20 menit | Selector, syntax, external CSS        |
| **Best Practices** | 10 menit | Do's & Don'ts, checklist              |
| **Demo & QA**      | 5 menit  | Tunjukkan contoh-buruk vs contoh-baik |

---

## 📚 Cara Mengajar (untuk Guru)

### **1. Pembukaan (5 menit)**

Mulai dengan pertanyaan:

- "Kalian pernah lihat website yang berantakan? Tampilannya aneh?"
- "Bagaimana caranya supaya kode kita rapi dan mudah dipahami?"

Jelaskan bahwa hari ini fokus pada **ATURAN** bukan styling. Seperti belajar tata bahasa sebelum menulis karangan.

---

### **2. Bagian 1: HTML Rules (20 menit)**

#### **a. Struktur HTML Wajib (5 menit)**

- Tunjukkan struktur minimal HTML5
- Jelaskan fungsi setiap bagian (`<!DOCTYPE>`, `<head>`, `<body>`)
- **Visual**: Gambar di papan/slide struktur HTML sebagai "kerangka rumah"

#### **b. Penutupan Tag & Nesting (7 menit)**

- Demo: Buka `contoh-buruk.html` di browser
- Tunjukkan masalah: tag tidak tertutup, nesting berantakan
- Buka code-nya, circle kesalahan-kesalahan
- Bandingkan dengan `contoh-baik.html`

#### **c. Indentasi & Naming (8 menit)**

- Jelaskan mengapa indentasi penting (analogi: paragraf di buku)
- Tunjukkan contoh class yang bermakna vs tidak bermakna
- **Aktivitas kecil**: Minta siswa tebak apa fungsi class `.a` vs `.kartu-skill`

---

### **3. Bagian 2: CSS Rules (20 menit)**

#### **a. Syntax & Selector (7 menit)**

- Jelaskan 3 jenis selector: element, class, ID
- Kapan pakai masing-masing
- Demo di `style-baik.css`: tunjukkan struktur yang rapi

#### **b. External vs Internal vs Inline (7 menit)**

- Buka `contoh-buruk.html`: tunjukkan inline CSS di mana-mana
- Buka `contoh-baik.html` + `style-baik.css`: terpisah dan rapi
- **Aktivitas**: Hitung berapa kali harus edit jika warna merah di inline CSS (banyak!) vs external (1 kali saja!)

#### **c. Specificity (6 menit)**

- Jelaskan urutan prioritas: Inline > ID > Class > Element
- Demo sederhana dengan warna yang berbeda-beda

---

### **4. Bagian 3: Best Practices (10 menit)**

#### **a. Do's & Don'ts (5 menit)**

- Baca bersama-sama bagian ini di `Week15.md`
- Tekankan: nama yang jelas, komentar, tidak duplikasi

#### **b. Kesalahan Umum (5 menit)**

- Review 4 kesalahan umum
- **Challenge**: Tampilkan code dengan error, minta siswa temukan

#### **c. Checklist (bonus)**

- Berikan printout checklist
- Jelaskan: gunakan ini sebelum submit tugas!

---

### **5. Demo & Penutup (5 menit)**

1. **Side-by-side comparison**:
   - Buka `contoh-buruk.html` di browser (tab 1)
   - Buka `contoh-baik.html` di browser (tab 2)
   - Tanya: "Mana yang lebih rapi?"
   - Buka code kedua file, tanya lagi: "Mana yang lebih mudah dipahami?"

2. **Key Takeaways**:
   - Kode yang rapi = profesional
   - Ikuti aturan = mudah di-maintain
   - External CSS > Internal > Inline

3. **Tugas**:
   - Buat halaman "Tentang Saya" dengan aturan yang benar
   - Cek dengan checklist sebelum submit

---

## 💡 Tips untuk Guru

### **Jika Siswa Cepat Tangkap (Waktu Lebih)**

- Ajarkan: validator online (validator.w3.org)
- Live coding: perbaiki `contoh-buruk.html` bersama-sama
- Buat kompetisi: siapa yang bisa temukan error paling banyak?

### **Jika Siswa Lambat (Waktu Kurang)**

- Skip bagian specificity (terlalu advanced)
- Fokus pada: struktur dasar, external CSS, dan indentasi
- Simpan best practices untuk review singkat saja

### **Troubleshooting**

- **"Kenapa harus rapi? Toh jalan juga?"**  
  Jawab: "Coba kamu baca buku tanpa spasi dan paragraf. Susah kan? Sama halnya dengan code."
- **"ID dan Class apa bedanya?"**  
  Analogi: ID = Nama lengkap (unik), Class = Seragam (banyak orang pakai sama)

---

## 📝 Tugas untuk Siswa

**Buat halaman HTML tentang diri kamu dengan syarat:**

✅ **Wajib:**

1. Struktur HTML lengkap (`<!DOCTYPE>`, dll)
2. CSS di file terpisah (external)
3. Minimal ada: heading, paragraf, list, 3 section
4. Indentasi rapi
5. Nama class bermakna (bukan .a, .b, .box1, dll)

✅ **Bonus (nilai tambahan):**

1. Ada gambar dengan atribut `alt`
2. Ada hover effect di CSS
3. Pakai CSS variable (`:root`)
4. Responsive (gunakan `max-width`)

**Submit:** File .html dan .css (zip jadi 1)

---

## 🔗 Resource Tambahan

### **Untuk Siswa:**

- [W3Schools HTML](https://www.w3schools.com/html/)
- [W3Schools CSS](https://www.w3schools.com/css/)
- [HTML Validator](https://validator.w3.org/)
- [CSS Validator](https://jigsaw.w3.org/css-validator/)

### **Untuk Guru:**

- [MDN Web Docs](https://developer.mozilla.org/)
- [CSS Tricks](https://css-tricks.com/)
- [Can I Use](https://caniuse.com/) - Cek browser support

---

## 📊 Kriteria Penilaian Tugas

| Aspek             | Poin | Kriteria                                   |
| ----------------- | ---- | ------------------------------------------ |
| **Struktur HTML** | 30   | Lengkap, semua tag tertutup, nesting benar |
| **External CSS**  | 20   | CSS terpisah, tidak ada inline style       |
| **Naming**        | 15   | Class/ID bermakna, konsisten huruf kecil   |
| **Indentasi**     | 15   | Rapi, konsisten (2 atau 4 spasi)           |
| **Konten**        | 10   | Sesuai syarat (heading, paragraf, list)    |
| **Kreativitas**   | 10   | Desain menarik, ada usaha lebih            |
| **Bonus**         | +10  | Fitur tambahan (gambar, hover, etc)        |
| **Total**         | 100  |                                            |

**Pengurangan:**

- -5: Lupa `<!DOCTYPE html>`
- -5: Tag tidak ditutup
- -10: Pakai inline CSS
- -10: Indentasi berantakan
- -5: Nama class tidak bermakna (a, b, box1, dll)

---

## 🎓 Kompetensi yang Diuji

Sesuai dengan kurikulum teknologi SMP:

1. **K3 (Kreativitas, Kolaborasi, Komunikasi)**
   - Menulis code yang komunikatif (mudah dipahami orang lain)
2. **Computational Thinking**
   - Dekomposisi: Memecah website jadi section-section
   - Pattern Recognition: Mengenali struktur HTML yang benar
   - Abstraction: Memahami konsep class vs ID
3. **Problem Solving**
   - Debugging: Menemukan dan memperbaiki error
   - Best Practices: Menerapkan solusi optimal

---

## ❓ FAQ

**Q: Apakah harus pakai external CSS?**  
A: Untuk project serius, YA. Tapi untuk latihan 1 file HTML boleh internal CSS.

**Q: Boleh pakai ID untuk styling?**  
A: Bisa, tapi lebih baik pakai class. ID lebih untuk JavaScript nanti.

**Q: Harus pakai Bahasa Inggris untuk nama class?**  
A: Best practice pakai Bahasa Inggris, tapi untuk belajar boleh Bahasa Indonesia dulu.

**Q: Indentasi 2 spasi atau 4 spasi?**  
A: Bebas, yang penting KONSISTEN. Pilih salah satu dan pakai terus.

---

## 🔄 Update Log

| Tanggal     | Versi | Perubahan          |
| ----------- | ----- | ------------------ |
| 23 Feb 2026 | 1.0   | Materi awal dibuat |

---

**Selamat mengajar! 🎉**

Jika ada pertanyaan atau saran, silakan diskusi dengan tim pengajar lain.
