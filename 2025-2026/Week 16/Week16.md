# Week 16: Kesalahan Umum HTML & CSS + Format File yang Benar

---

## 🎯 Tujuan Pembelajaran (< 1 jam)

Setelah belajar hari ini, kalian akan paham:

1. ✅ Kesalahan umum yang sering dilakukan pemula
2. ✅ Perbedaan format file (.html, .css, .txt)
3. ✅ Cara menghindari kesalahan tersebut
4. ✅ Best practices dalam membuat website

**Durasi:** 45-60 menit

---

## 📋 Rangkuman Kesalahan dari Submission Minggu Lalu

Setelah memeriksa hasil submission kalian, ini kesalahan umum yang ditemukan:

### ❌ Kesalahan #1: Nama File Tidak Profesional

**Contoh Salah:**

```
uhhhhhhhhh.html
filebaru.html
cobacoba.html
```

**Kenapa Salah?**

- Sulit dicari nanti
- Tidak menjelaskan isi file
- Tidak profesional

**✅ Cara yang Benar:**

```
index.html          ← Untuk halaman utama
data-diri.html      ← Nama jelas, pakai tanda hubung
tentang-saya.html
hobi-saya.html
```

**Aturan Penamaan File:**

1. Gunakan huruf kecil semua
2. Pakai tanda hubung `-` untuk spasi (BUKAN spasi atau underscore)
3. Nama harus menjelaskan isi
4. Jangan pakai karakter aneh (!@#$%^&\*)

---

### ❌ Kesalahan #2: Lupa Mengganti Title Default

**Contoh Salah:**

```html
<title>Document</title> ← Masih default!
```

**✅ Cara yang Benar:**

```html
<title>Data Diri - Justin Arland</title>
<title>Tentang Saya - Jonathan</title>
<title>Hobi Saya - Nathan</title>
```

**Mengapa Penting?**

- Title muncul di tab browser
- Muncul di hasil pencarian Google
- Membantu orang tahu isi halaman

---

### ❌ Kesalahan #3: Style Inline Berlebihan

**Contoh Salah:**

```html
<h1 style="text-align: center; font-family: Arial; color: white;">Judul</h1>
<p style="color: white;">Paragraf 1</p>
<p style="color: white;">Paragraf 2</p>
<p style="color: white;">Paragraf 3</p>
```

**Masalah:**

- Kode sulit dibaca
- Kalau mau ubah warna, harus ubah satu-satu
- File HTML jadi berantakan

**✅ Cara yang Benar:**

**File HTML: (index.html)**

```html
<h1 class="judul">Judul</h1>
<p class="paragraf">Paragraf 1</p>
<p class="paragraf">Paragraf 2</p>
<p class="paragraf">Paragraf 3</p>
```

**File CSS: (style.css)**

```css
.judul {
  text-align: center;
  font-family: Arial;
  color: white;
}

.paragraf {
  color: white;
}
```

**Keuntungan:**

- Ubah 1 tempat di CSS, semua paragraf ikut berubah
- Kode lebih rapi
- Lebih mudah maintenance

---

### ❌ Kesalahan #4: Lang Tidak Sesuai Konten

**Contoh Salah:**

```html
<html lang="en">
  ← Bahasa Inggris
  <body>
    <p>Halo nama saya Budi</p>
    ← Konten Bahasa Indonesia
  </body>
</html>
```

**✅ Cara yang Benar:**

```html
<html lang="id">
  ← "id" untuk Bahasa Indonesia
  <body>
    <p>Halo nama saya Budi</p>
  </body>
</html>
```

**Pilihan Lang:**

- `lang="id"` → Bahasa Indonesia
- `lang="en"` → English
- `lang="zh"` → Chinese

---

### ❌ Kesalahan #5: Emoji Berlebihan

**Contoh Salah:**

```html
<p>Aku suka masak🥰🥰🥰🥰🥰🥰🥰</p>
```

**✅ Cara yang Benar:**

```html
<p>Aku suka masak 🥰</p>
← Cukup 1-2 emoji saja
```

**Tips:**

- Emoji boleh dipakai, tapi jangan berlebihan
- Maksimal 1-2 emoji per kalimat
- Jangan emoji di judul penting

---

### ❌ Kesalahan #6: Gambar dengan URL Terlalu Panjang

**Contoh Salah:**

```html
<img src="data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAAAQABAAD/2wCEAAkGB..." />
<!-- URL panjang 10,000+ karakter! -->
```

**Masalah:**

- Kode jadi sangat panjang dan susah dibaca
- File HTML jadi besar
- Sulit di-maintain

**✅ Cara yang Benar:**

**Opsi 1: Pakai Gambar Lokal**

```
📁 folder-project/
  ├── index.html
  ├── style.css
  └── 📁 images/
      ├── foto-saya.jpg
      └── hobi-masak.jpg
```

```html
<img src="images/foto-saya.jpg" alt="Foto Saya" width="200" />
<img src="images/hobi-masak.jpg" alt="Hobi Masak" width="200" />
```

**Opsi 2: Pakai URL Pendek**

```html
<img src="https://i.imgur.com/abc123.jpg" alt="Gambar" width="200" />
```

**Aturan Gambar yang Baik:**

1. Selalu pakai atribut `alt` (untuk accessibility)
2. Tentukan `width` atau `height`
3. Pakai gambar lokal kalau bisa
4. Nama file gambar harus jelas: `foto-profil.jpg`, bukan `IMG_001.jpg`

---

### ❌ Kesalahan #7: Struktur List Tidak Rapi

**Contoh Salah:**

```html
<ul>
  <li>Main Game</li>
  <img src="game.jpg" />
  <p>Paragraf tentang game</p>
  <li>Menulis</li>
  <img src="menulis.jpg" />
</ul>
```

**Masalah:** Gambar dan paragraf di luar `<li>`

**✅ Cara yang Benar:**

```html
<ul>
  <li>
    <strong>Main Game</strong>
    <img src="game.jpg" alt="Game" width="200" />
    <p>Paragraf tentang game</p>
  </li>
  <li>
    <strong>Menulis</strong>
    <img src="menulis.jpg" alt="Menulis" width="200" />
    <p>Paragraf tentang menulis</p>
  </li>
</ul>
```

**Atau Lebih Rapi Lagi:**

```html
<div class="hobi-section">
  <h3>Main Game</h3>
  <img src="game.jpg" alt="Game" class="hobi-img" />
  <p>Paragraf tentang game</p>
</div>

<div class="hobi-section">
  <h3>Menulis</h3>
  <img src="menulis.jpg" alt="Menulis" class="hobi-img" />
  <p>Paragraf tentang menulis</p>
</div>
```

---

### ❌ Kesalahan #8: Spacing Tidak Konsisten

**Contoh Salah:**

```html
<meta charset="UTF-8" />
<meta name="viewport" content="width=device-width, initial-scale=1.0" />
```

**✅ Cara yang Benar:**

```html
<meta charset="UTF-8" />
<meta name="viewport" content="width=device-width, initial-scale=1.0" />
```

**Aturan:**

- 1 spasi antara atribut
- Konsisten di semua kode

---

## 🚨 PENTING: Format File yang Benar!

### Masalah: Ada yang Kirim File `indexhtml.txt`

**❌ SALAH:**

```
indexhtml.txt      ← Ini file TEXT, bukan HTML!
style.txt          ← Ini file TEXT, bukan CSS!
index.HTML         ← Huruf besar semua
Index.html         ← Huruf besar di awal
```

**✅ BENAR:**

```
index.html         ← Huruf kecil, ekstensi .html
style.css          ← Huruf kecil, ekstensi .css
script.js          ← Huruf kecil, ekstensi .js
```

---

### 📝 Apa itu Format File (Extension)?

**Format file** adalah akhiran nama file yang memberitahu komputer/browser apa isi file tersebut.

| Format  | Untuk Apa?        | Contoh Nama File |
| ------- | ----------------- | ---------------- |
| `.html` | File website HTML | `index.html`     |
| `.css`  | File styling CSS  | `style.css`      |
| `.js`   | File JavaScript   | `script.js`      |
| `.txt`  | File teks biasa   | `catatan.txt`    |
| `.jpg`  | Gambar JPEG       | `foto.jpg`       |
| `.png`  | Gambar PNG        | `logo.png`       |
| `.pdf`  | Dokumen PDF       | `laporan.pdf`    |

---

### ⚠️ Mengapa `indexhtml.txt` SALAH?

```
indexhtml.txt
          ^^^
          └── Ini memberitahu komputer: "Saya file TEXT biasa"
```

**Akibatnya:**

1. Browser TIDAK akan menampilkan sebagai website
2. Kalau dibuka, cuma muncul kode HTML mentah
3. CSS tidak akan bekerja
4. Gambar tidak akan muncul

**Yang Benar:**

```
index.html
     ^^^^^
     └── Ini memberitahu komputer: "Saya file HTML, tampilkan sebagai website"
```

---

### 🔧 Cara Melihat & Mengubah Format File

#### **Windows:**

**1. Tampilkan Extension File:**

- Buka **File Explorer**
- Klik tab **View** (atau **Tampilan**)
- Centang **"File name extensions"** (atau **"Ekstensi nama file"**)

**Sebelum:**

```
index       ← Tidak tahu formatnya apa
style
```

**Sesudah:**

```
index.html  ← Jelas ini file HTML
style.css   ← Jelas ini file CSS
```

**2. Membuat File HTML Baru yang Benar:**

**Cara 1: Pakai Text Editor (VS Code/Notepad++)**

- Buka VS Code/Notepad++
- File → New File
- Ketik kode HTML
- File → Save As
- Ketik nama: `index.html` (BUKAN index.txt)
- Save

**Cara 2: Rename File**

- Klik kanan file `indexhtml.txt`
- Pilih **Rename**
- Ubah jadi `index.html`
- Klik Yes kalau ada peringatan

---

### 🎯 Cara Membuat File HTML dengan Benar (Step by Step)

**Langkah 1: Buat Folder Project**

```
📁 website-saya/
```

**Langkah 2: Buka Folder di VS Code**

- Klik kanan folder
- Pilih "Open with Code"

**Langkah 3: Buat File HTML**

- Di VS Code, klik icon **New File** ➕
- Ketik nama: `index.html`
- Tekan Enter

**Langkah 4: Ketik Kode HTML**

```html
<!DOCTYPE html>
<html lang="id">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Website Saya</title>
    <link rel="stylesheet" href="style.css" />
  </head>
  <body>
    <h1>Halo Dunia!</h1>
  </body>
</html>
```

**Langkah 5: Buat File CSS**

- Buat file baru: `style.css`

```css
body {
  font-family: Arial;
  background-color: #f0f0f0;
}

h1 {
  color: blue;
  text-align: center;
}
```

**Langkah 6: Buka di Browser**

- Klik kanan `index.html`
- Pilih "Open with Live Server" (kalau ada extension)
- Atau "Open with" → Browser pilihan

---

## ✅ Checklist Sebelum Submit Tugas

Sebelum mengumpulkan tugas, cek ini dulu:

- [ ] Nama file pakai huruf kecil dan tanda hubung: `data-diri.html` ✓
- [ ] Format file sudah benar (`.html`, `.css`, bukan `.txt`) ✓
- [ ] Sudah ganti `<title>` dari "Document" ✓
- [ ] `lang` sesuai bahasa konten (`lang="id"` untuk Indonesia) ✓
- [ ] CSS dipisah ke file `.css`, bukan inline style berlebihan ✓
- [ ] Emoji tidak berlebihan (max 1-2 per kalimat) ✓
- [ ] Gambar pakai file lokal atau URL pendek ✓
- [ ] Semua gambar punya atribut `alt` ✓
- [ ] Struktur HTML rapi dan tag ditutup dengan benar ✓
- [ ] Tidak ada typo atau kesalahan ejaan ✓
- [ ] Spacing konsisten ✓
- [ ] Sudah dicoba buka di browser dan tampilan OK ✓

---

## 🏋️ Latihan (15 menit)

### Latihan 1: Perbaiki Kesalahan Ini

**File: `tugas.txt`** ← Kesalahan pertama!

```html
<html lang="en">
  <head>
    <title>Document</title>
  </head>
  <body style="background-color: blue;">
    <h1 style="color: white; text-align: center; font-family: Arial;">
      Tugas Saya🥰🥰🥰🥰
    </h1>
    <p style="color: white;">Ini paragraf</p>
    <p style="color: white;">Ini paragraf 2</p>
  </body>
</html>
```

**Tugas Kalian:**

1. Ubah nama file jadi benar
2. Perbaiki semua kesalahan
3. Pisahkan CSS ke file terpisah

<details>
<summary>Lihat Jawaban</summary>

**File: `tugas-saya.html`**

```html
<!DOCTYPE html>
<html lang="id">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Tugas Saya - Nama Kamu</title>
    <link rel="stylesheet" href="style.css" />
  </head>
  <body>
    <h1>Tugas Saya 🥰</h1>
    <p>Ini paragraf</p>
    <p>Ini paragraf 2</p>
  </body>
</html>
```

**File: `style.css`**

```css
body {
  background-color: blue;
  color: white;
  font-family: Arial;
}

h1 {
  text-align: center;
}
```

</details>

---

### Latihan 2: Buat Website Data Diri yang Benar

**Requirement:**

1. Nama file: `data-diri.html` dan `style.css`
2. Struktur HTML lengkap (DOCTYPE, html, head, body)
3. Title yang sesuai
4. Konten:
   - Nama
   - Kelas
   - 3 Hobi (pakai unordered list)
   - 1 Gambar (pakai file lokal atau URL pendek)
5. CSS terpisah dengan minimal 5 styling rules
6. Tidak ada emoji berlebihan
7. Semua gambar punya atribut `alt`

**Contoh Jawaban:**

**File: `data-diri.html`**

```html
<!DOCTYPE html>
<html lang="id">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Data Diri - Nama Kamu</title>
    <link rel="stylesheet" href="style.css" />
  </head>
  <body>
    <div class="container">
      <h1>Data Diri Saya</h1>

      <div class="section">
        <h2>Tentang Saya</h2>
        <p>Nama: <strong>Nama Kamu</strong></p>
        <p>Kelas: <strong>7 SMP</strong></p>
      </div>

      <div class="section">
        <h2>Hobi Saya</h2>
        <ul>
          <li>Bermain sepak bola</li>
          <li>Membaca komik</li>
          <li>Menggambar</li>
        </ul>
      </div>

      <div class="section">
        <h2>Foto Saya</h2>
        <img
          src="images/foto-saya.jpg"
          alt="Foto Profil Saya"
          class="foto-profil"
        />
      </div>
    </div>
  </body>
</html>
```

**File: `style.css`**

```css
body {
  font-family: Arial, sans-serif;
  background-color: #f5f5f5;
  margin: 0;
  padding: 20px;
}

.container {
  max-width: 800px;
  margin: 0 auto;
  background-color: white;
  padding: 30px;
  border-radius: 10px;
  box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
}

h1 {
  color: #2c3e50;
  text-align: center;
  border-bottom: 3px solid #3498db;
  padding-bottom: 10px;
}

h2 {
  color: #3498db;
  margin-top: 20px;
}

.section {
  margin: 20px 0;
  padding: 15px;
  background-color: #ecf0f1;
  border-radius: 5px;
}

ul {
  line-height: 1.8;
}

li {
  margin: 5px 0;
}

.foto-profil {
  width: 200px;
  border-radius: 10px;
  box-shadow: 0 2px 5px rgba(0, 0, 0, 0.2);
}
```

---

## 📚 Rangkuman

**3 Hal Terpenting Hari Ini:**

1. **Format File Harus Benar!**
   - `.html` untuk HTML
   - `.css` untuk CSS
   - BUKAN `.txt`

2. **Kesalahan Umum yang Harus Dihindari:**
   - Nama file tidak profesional
   - Lupa ganti title
   - Style inline berlebihan
   - Format file salah

3. **Checklist Sebelum Submit:**
   - Cek nama file
   - Cek format file
   - Cek struktur HTML
   - Cek di browser

---

## 🎯 Tugas Minggu Ini

**Buat website "Liburan Favorit Saya"** dengan syarat:

✅ **File yang Harus Dibuat:**

1. `mapel.html`
2. `style.css`
3. Folder `images/` dengan minimal 2 gambar

✅ **Konten Minimal:**

- Judul: "Mata Pelajaran yang Sulit untuk saya"
- Nama & Kelas
- Ceritakan setiap 3 mata pelajaran (minimal 3 paragraf)
- 2-3 Gambar mata pelajaran

✅ **Syarat Teknis:**

- Struktur HTML lengkap & benar
- Title sesuai
- Lang="id"
- CSS terpisah (minimal 8 styling rules)
- Gambar ada atribut alt
- Tidak ada style inline
- Emoji maksimal 3 total

✅ **Cara Submit:**

- Zip folder project kalian
- Nama zip: `NamaKamu-Week16.zip`

**Deadline:** Rabu, 4 Maret 2026 Jam 19.00. kumpul lebih dari jam ini akan di tolak.

---

**Selamat Belajar! 🚀**

Kalau ada pertanyaan, jangan ragu tanya di group atau saat kelas!
