# Week 11: Membuat Website Storytelling Liburan dengan HTML & CSS

## 🎯 Tujuan Pembelajaran

Pada minggu ini, kamu akan belajar membuat website sederhana menggunakan HTML dan CSS dengan cara yang menyenangkan - menceritakan pengalaman liburanmu!

## 📚 Pengenalan HTML dan CSS

### Apa itu HTML?

**HTML (HyperText Markup Language)** adalah bahasa markup yang digunakan untuk membuat struktur halaman web. Bayangkan HTML seperti kerangka rumah - dia yang menentukan di mana letak pintu, jendela, ruangan, dll.

#### Konsep Tag Pembuka dan Tag Penutup

Sebagian besar tag HTML memiliki **tag pembuka** dan **tag penutup**. Ini seperti membuka dan menutup kotak - kamu harus memberitahu browser di mana konten dimulai dan di mana berakhir.

**Format:**

- Tag pembuka: `<namatag>`
- Tag penutup: `</namatag>` (perhatikan ada garis miring `/`)

**Contoh:**

```html
<head>
  <title>Judul Website</title>
</head>
```

**Mengapa harus ada penutup?**

1. **Memberitahu browser kapan elemen selesai** - Browser perlu tahu di mana konten dalam tag tersebut berakhir
2. **Mencegah error** - Tanpa penutup, browser bingung dan tampilan bisa berantakan
3. **Nested tags** - Memungkinkan tag di dalam tag (seperti kotak dalam kotak)

**Contoh jika tidak ada penutup (SALAH):**

```html
❌
<head>
  <title>Judul Website</title>
  <!-- Browser bingung: head-nya sampai mana? -->
  <body></body>
</head>
```

**Contoh yang benar:**

```html
✅
<head>
  <title>Judul Website</title>
</head>
<!-- Jelas: head selesai di sini -->
<body></body>
```

**Catatan:** Ada beberapa tag yang tidak memerlukan penutup (self-closing tags), seperti:

- `<img>` - untuk gambar
- `<br>` - untuk line break
- `<hr>` - untuk garis horizontal
- `<input>` - untuk form input

#### Struktur HTML Lengkap

```html
<!DOCTYPE html>
<html>
  <head>
    <title>Judul Website</title>
  </head>
  <body>
    <h1>Ini adalah heading</h1>
    <p>Ini adalah paragraf</p>
  </body>
</html>
```

#### Perbedaan `<head>` vs `<header>`: Kenapa Ada Dua yang Mirip?

Ini pertanyaan yang sering bikin bingung! Mari kita jelaskan perbedaannya:

##### 1. `<head>` (Di luar body)

**Lokasi:** Di luar `<body>`, sejajar dengan `<body>`
**Fungsi:** Berisi **metadata** dan informasi untuk browser/mesin pencari

```html
<html>
  <head>
    <!-- Ini TIDAK terlihat di halaman -->
    <title>Judul di Tab Browser</title>
    <meta charset="UTF-8" />
    <link rel="stylesheet" href="style.css" />
    <script src="script.js"></script>
  </head>
  <body>
    <!-- Konten yang terlihat ada di sini -->
  </body>
</html>
```

**Isi dari `<head>`:**

- `<title>` - Judul yang muncul di tab browser
- `<meta>` - Informasi meta (charset, description, keywords)
- `<link>` - Link ke CSS atau favicon
- `<script>` - Link ke JavaScript
- `<style>` - CSS internal

**Karakteristik:**

- ❌ Tidak terlihat di halaman web
- ✅ Dibaca oleh browser dan search engine
- 📋 Bersifat teknis/konfigurasi

##### 2. `<header>` (Di dalam body)

**Lokasi:** Di dalam `<body>`, bagian dari konten yang terlihat
**Fungsi:** Bagian **header/kepala** dari konten (yang terlihat pengunjung)

```html
<html>
  <head>
    <title>Website Liburan</title>
  </head>
  <body>
    <!-- Ini TERLIHAT di halaman -->
    <header>
      <h1>Liburanku di Bali 🏖️</h1>
      <nav>
        <a href="#hari1">Hari 1</a>
        <a href="#hari2">Hari 2</a>
      </nav>
    </header>

    <main>
      <p>Cerita liburan...</p>
    </main>
  </body>
</html>
```

**Isi dari `<header>`:**

- Logo website
- Judul halaman utama
- Menu navigasi
- Tagline atau slogan
- Banner

**Karakteristik:**

- ✅ Terlihat oleh pengunjung
- 🎨 Bisa di-styling dengan CSS
- 📝 Berisi konten visual

##### Perbandingan Visual

```html
<!DOCTYPE html>
<html>
  <!-- ============ HEAD ============ -->
  <head>
    <!-- Bagian "otak" website -->
    <!-- TIDAK TERLIHAT di layar -->
    <title>Tab Browser</title>
    <link rel="stylesheet" href="style.css" />
  </head>
  <!-- ============================== -->

  <body>
    <!-- ========== HEADER ========== -->
    <header>
      <!-- Bagian atas konten -->
      <!-- TERLIHAT di layar -->
      <h1>Judul Website Besar</h1>
      <nav>Menu navigasi</nav>
    </header>
    <!-- ============================ -->

    <main>
      <p>Konten utama di sini...</p>
    </main>

    <footer>
      <p>Footer di bawah</p>
    </footer>
  </body>
</html>
```

##### Analogi Rumah

Bayangkan website seperti rumah:

```
🏠 <html> = Seluruh rumah

   📋 <head> = Dokumen rumah (IMB, sertifikat)
      - Tidak terlihat tamu
      - Penting untuk legalitas
      - Berisi informasi teknis

   🏡 <body> = Bagian rumah yang bisa dilihat

      🚪 <header> = Teras/pintu depan rumah
         - Terlihat oleh tamu
         - Ada nama rumah, nomor
         - Kesan pertama

      🛋️ <main> = Ruang tamu
         - Konten utama

      🚪 <footer> = Halaman belakang
         - Informasi tambahan
```

##### Tabel Perbandingan

| Aspek         | `<head>`                  | `<header>`                    |
| ------------- | ------------------------- | ----------------------------- |
| **Lokasi**    | Di luar `<body>`          | Di dalam `<body>`             |
| **Terlihat?** | ❌ Tidak                  | ✅ Ya                         |
| **Fungsi**    | Metadata & config         | Konten kepala halaman         |
| **Isi**       | title, meta, link, script | h1, nav, logo, banner         |
| **Wajib?**    | ✅ Wajib ada              | ⚠️ Opsional (tapi disarankan) |
| **Jumlah**    | Hanya 1 per halaman       | Bisa banyak (per section)     |
| **Styling**   | ❌ Tidak perlu            | ✅ Perlu di-styling CSS       |

##### Contoh Lengkap dalam Konteks

```html
<!DOCTYPE html>
<html>
  <!-- INI <HEAD> -->
  <head>
    <title>Liburan Seru di Bali - Website Pribadi</title>
    <meta charset="UTF-8" />
    <meta name="description" content="Cerita liburan saya di Bali" />
    <link rel="stylesheet" href="style.css" />
  </head>

  <body>
    <!-- INI <HEADER> -->
    <header class="main-header">
      <h1>🏖️ Liburanku di Bali</h1>
      <p class="subtitle">21-25 Desember 2025</p>
      <nav>
        <a href="#hari1">Hari 1</a> | <a href="#hari2">Hari 2</a> |
        <a href="#galeri">Galeri</a>
      </nav>
    </header>

    <main>
      <section id="hari1">
        <!-- Bisa juga ada header untuk section -->
        <header>
          <h2>Hari 1: Tiba di Bali</h2>
          <p class="tanggal">21 Desember 2025</p>
        </header>
        <p>Hari ini kami tiba di Bali...</p>
      </section>
    </main>

    <footer>
      <p>© 2025 - Cerita Liburanku</p>
    </footer>
  </body>
</html>
```

**Kesimpulan:**

- `<head>` = Bagian teknis yang tidak terlihat (untuk browser)
- `<header>` = Bagian visual yang terlihat (untuk pengunjung)
- Keduanya punya peran berbeda dan TIDAK saling menggantikan!

### Apa itu CSS?

**CSS (Cascading Style Sheets)** adalah bahasa yang digunakan untuk mendesain tampilan website. Jika HTML adalah kerangka rumah, maka CSS adalah cat, wallpaper, dan dekorasi yang membuat rumah jadi cantik!

### Teknik Penerapan CSS

Ada dua teknik utama untuk menerapkan CSS ke dalam HTML:

#### 1. Internal CSS (Inline/Embedded CSS)

CSS ditulis langsung di dalam file HTML menggunakan tag `<style>` di bagian `<head>`.

**Contoh Internal CSS:**

```html
<!DOCTYPE html>
<html>
  <head>
    <title>Website Saya</title>
    <style>
      body {
        background-color: #f0f0f0;
        font-family: Arial, sans-serif;
      }

      h1 {
        color: blue;
        text-align: center;
      }

      p {
        color: #333;
        line-height: 1.6;
      }
    </style>
  </head>
  <body>
    <h1>Selamat Datang</h1>
    <p>Ini adalah paragraf</p>
  </body>
</html>
```

**Kelebihan Internal CSS:**

- ✅ Semua kode ada dalam satu file (praktis untuk project kecil)
- ✅ Tidak perlu file terpisah
- ✅ Loading lebih cepat karena tidak ada request file eksternal

**Kekurangan Internal CSS:**

- ❌ File HTML jadi panjang dan susah dibaca
- ❌ CSS tidak bisa digunakan ulang di halaman lain
- ❌ Sulit untuk maintenance project besar

#### 2. External CSS (CSS Eksternal)

CSS ditulis di file terpisah dengan ekstensi `.css`, lalu dihubungkan ke HTML menggunakan tag `<link>`.

**Contoh External CSS:**

File `index.html`:

```html
<!DOCTYPE html>
<html>
  <head>
    <title>Website Saya</title>
    <link rel="stylesheet" href="style.css" />
  </head>
  <body>
    <h1>Selamat Datang</h1>
    <p>Ini adalah paragraf</p>
  </body>
</html>
```

File `style.css`:

```css
body {
  background-color: #f0f0f0;
  font-family: Arial, sans-serif;
}

h1 {
  color: blue;
  text-align: center;
}

p {
  color: #333;
  line-height: 1.6;
}
```

**Kelebihan External CSS:**

- ✅ Kode lebih terorganisir dan mudah dibaca
- ✅ CSS bisa digunakan di banyak halaman HTML (reusable)
- ✅ Mudah untuk maintenance dan update
- ✅ File CSS bisa di-cache oleh browser (loading lebih cepat)
- ✅ Kolaborasi tim lebih mudah (designer bisa fokus ke CSS)

**Kekurangan External CSS:**

- ❌ Perlu file tambahan
- ❌ Butuh satu request HTTP tambahan (minimal impact)

### Perbandingan Skalabilitas

| Aspek                | Internal CSS           | External CSS              |
| -------------------- | ---------------------- | ------------------------- |
| **Project Kecil**    | ✅ Cocok (1-2 halaman) | ⚠️ Overkill tapi tetap OK |
| **Project Menengah** | ❌ Mulai ribet         | ✅ Sangat cocok           |
| **Project Besar**    | ❌ Tidak scalable      | ✅ **Wajib digunakan**    |
| **Reusability**      | ❌ Rendah              | ✅ Tinggi                 |
| **Maintenance**      | ❌ Sulit               | ✅ Mudah                  |
| **Kolaborasi Tim**   | ❌ Sulit               | ✅ Mudah                  |
| **Loading Speed**    | ✅ Cepat (1 file)      | ✅ Cepat (cached)         |

### 💡 Rekomendasi untuk Project Ini

**Untuk tugas storytelling liburan ini, gunakan External CSS** karena:

1. Kamu akan belajar praktek industry standard
2. Lebih mudah untuk bereksperimen dengan styling
3. Kode lebih rapi dan profesional
4. Jika nanti mau bikin halaman kedua (misal: About Me), CSS bisa langsung dipakai ulang!

**Contoh struktur folder yang baik:**

```
liburan-kamu/
├── index.html          (atau liburan.html)
├── style.css          (semua styling di sini)
└── images/            (folder untuk gambar)
    ├── foto1.jpg
    ├── foto2.jpg
    └── foto3.jpg
```

## 🏖️ Project: "Kemarin Liburan Ngapain Aja?"

### Konsep Project

Kamu akan membuat website yang menceritakan pengalaman liburanmu! Website ini akan berisi:

- Judul cerita liburan
- Tempat yang dikunjungi
- Kegiatan yang dilakukan
- Foto-foto (boleh pakai placeholder dulu)
- Kesan dan pesan dari liburan

### Struktur Website yang Akan Dibuat

1. **Header/Judul** - Judul cerita liburanmu
2. **Intro** - Pembukaan singkat tentang liburanmu
3. **Bagian Hari 1, 2, 3, dst** - Cerita per hari
4. **Galeri Foto** - Koleksi foto (atau placeholder)
5. **Penutup** - Kesan dan pesan

## 🛠️ Tag-Tag HTML yang Akan Digunakan

### Tag Struktur Dasar

- `<!DOCTYPE html>` - Deklarasi tipe dokumen
- `<html>` - Tag pembungkus seluruh dokumen
- `<head>` - Informasi meta tentang halaman
- `<body>` - Konten yang terlihat di halaman

### Tag Konten

- `<h1>`, `<h2>`, `<h3>` - Heading (judul)
- `<p>` - Paragraf
- `<img>` - Gambar
- `<a>` - Link
- `<div>` - Container/pembungkus
- `<ul>`, `<ol>`, `<li>` - List (daftar)
- `<br>` - Line break (pindah baris)
- `<hr>` - Horizontal rule (garis pemisah)

### Tag Semantic (Opsional)

- `<header>` - Bagian header
- `<main>` - Konten utama
- `<section>` - Bagian/seksi
- `<footer>` - Bagian footer

## 🎨 Properti CSS yang Akan Digunakan

### Warna dan Background

```css
color: blue; /* Warna teks */
background-color: #ffcccc; /* Warna latar belakang */
background-image: url("foto.jpg"); /* Gambar latar belakang */
```

### Font dan Teks

```css
font-family: Arial, sans-serif; /* Jenis font */
font-size: 16px; /* Ukuran font */
font-weight: bold; /* Ketebalan font */
text-align: center; /* Perataan teks */
line-height: 1.5; /* Jarak antar baris */
```

### Spacing (Jarak)

```css
margin: 20px; /* Jarak luar */
padding: 10px; /* Jarak dalam */
```

### Border dan Dimensi

```css
border: 2px solid black; /* Garis tepi */
border-radius: 10px; /* Sudut melengkung */
width: 300px; /* Lebar */
height: 200px; /* Tinggi */
```

## 📝 Tugas: Buat Website Storytelling Liburanmu!

### Tugas 1: Buat File HTML

Buat file baru bernama `liburan.html` dan isi dengan struktur dasar HTML yang menceritakan liburanmu.

**Minimal Requirements:**

- [ ] Judul website yang menarik
- [ ] Minimal 3 paragraf cerita
- [ ] Minimal 2 heading berbeda (h1, h2, atau h3)
- [ ] Minimal 3 gambar (boleh pakai placeholder dari https://picsum.photos/)
- [ ] List kegiatan yang dilakukan (minimal 5 item)
- [ ] Link ke tempat yang dikunjungi (bisa ke Google Maps)

**Contoh Struktur:**

```html
<!DOCTYPE html>
<html>
  <head>
    <title>Liburan Seru di Bali</title>
    <link rel="stylesheet" href="style.css" />
  </head>
  <body>
    <header>
      <h1>Liburanku di Bali! 🏖️</h1>
      <p>21-25 Desember 2025</p>
    </header>

    <main>
      <section class="intro">
        <h2>Perjalanan Dimulai...</h2>
        <p>Cerita pembuka liburanmu...</p>
      </section>

      <section class="hari-1">
        <h2>Hari 1: Tiba di Bali</h2>
        <img src="foto-hari1.jpg" alt="Sampai di Bali" />
        <p>Cerita hari pertama...</p>
      </section>

      <!-- Tambahkan hari-hari lainnya -->
    </main>
  </body>
</html>
```

```html
<section class="galeri">
        <h2>Galeri Foto</h2>
        <!-- Tambahkan foto-foto -->
      </section>

      <section class="penutup">
        <h2>Kesan dan Pesan</h2>
        <p>Kesimpulan dari liburanmu...</p>
      </section>
    </main>

    <footer>
      <p>© 2025 - Cerita Liburanku</p>
    </footer>
  </body>
</html>
```

### Tugas 2: Buat File CSS

Buat file baru bernama `style.css` untuk memperindah website liburanmu.

**Minimal Requirements:**

- [ ] Ubah warna background
- [ ] Ubah font family
- [ ] Atur ukuran dan alignment untuk heading
- [ ] Beri styling pada gambar (border, border-radius, dll)
- [ ] Atur spacing (margin dan padding)
- [ ] Buat hover effect pada gambar (opsional)

**Contoh CSS:**

```css
/* Reset dan Styling Dasar */
* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

body {
  font-family: "Segoe UI", Tahoma, Geneva, Verdana, sans-serif;
  background-color: #f5f5f5;
  line-height: 1.6;
  color: #333;
}

/* Header */
header {
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  color: white;
  text-align: center;
  padding: 40px 20px;
}

h2 {
  color: #667eea;
  margin-bottom: 15px;
  border-bottom: 2px solid #667eea;
  padding-bottom: 10px;
}
```

```css
header h1 {
  font-size: 2.5em;
  margin-bottom: 10px;
}

/* Main Content */
main {
  max-width: 800px;
  margin: 30px auto;
  background-color: white;
  padding: 30px;
  border-radius: 10px;
  box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
}

/* Sections */
section {
  margin-bottom: 40px;
}
```

```css
/* Images */
img {
  max-width: 100%;
  height: auto;
  border-radius: 10px;
  margin: 15px 0;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
}

img:hover {
  transform: scale(1.05);
  transition: transform 0.3s ease;
}

/* Footer */
footer {
  text-align: center;
  padding: 20px;
  background-color: #333;
  color: white;
  margin-top: 40px;
}
```

## 🎁 Bonus Challenge!

Jika kamu sudah selesai dengan tugas dasar, coba tambahkan fitur-fitur berikut:

1. **Animasi** - Tambahkan animasi CSS (fade in, slide, dll)
2. **Responsive Design** - Buat website terlihat bagus di mobile
3. **Navigation Menu** - Buat menu navigasi untuk loncat ke section tertentu
4. **Gallery Grid** - Buat galeri foto dengan layout grid
5. **Smooth Scroll** - Tambahkan smooth scrolling
6. **Dark Mode Toggle** - Buat tombol untuk switch ke dark mode

## 💡 Tips untuk Sukses

1. **Mulai dari yang sederhana** - Buat struktur HTML dulu, baru styling CSS
2. **Test sering-sering** - Buka file HTML di browser untuk melihat hasilnya
3. **Gunakan DevTools** - Tekan F12 di browser untuk inspect element
4. **Cari inspirasi** - Lihat website lain untuk mendapat ide desain
5. **Jangan takut salah** - Coding adalah proses trial and error!

## 📖 Resources Tambahan

### Website untuk Belajar:

- [W3Schools HTML](https://www.w3schools.com/html/)
- [W3Schools CSS](https://www.w3schools.com/css/)
- [MDN Web Docs](https://developer.mozilla.org/)

### Tools yang Berguna:

- [Google Fonts](https://fonts.google.com/) - Font gratis
- [Coolors](https://coolors.co/) - Color palette generator
- [Picsum Photos](https://picsum.photos/) - Placeholder images
- [Unsplash](https://unsplash.com/) - Foto gratis berkualitas tinggi

### Contoh Warna yang Bagus:

```css
/* Pastel Theme */
--color-1: #ffe5e5; /* Pink muda */
--color-2: #fff5e1; /* Cream */
--color-3: #e1f5ff; /* Biru muda */

/* Ocean Theme */
--color-1: #0077be; /* Biru laut */
--color-2: #00a8e8; /* Biru cerah */
--color-3: #76e5fc; /* Cyan */

/* Nature Theme */
--color-1: #2d6a4f; /* Hijau gelap */
--color-2: #52b788; /* Hijau sedang */
--color-3: #b7e4c7; /* Hijau muda */
```

## 🎯 Kriteria Penilaian

### HTML (50%)

- ✅ Struktur HTML lengkap dan valid
- ✅ Penggunaan tag yang tepat dan semantic
- ✅ Konten cerita yang menarik dan lengkap
- ✅ Minimal requirements terpenuhi

### CSS (40%)

- ✅ Styling yang menarik dan konsisten
- ✅ Layout yang rapi dan mudah dibaca
- ✅ Penggunaan warna yang harmonis
- ✅ Responsive (bonus points!)

### Kreativitas (10%)

- ✅ Desain yang unik dan original
- ✅ Cerita yang menarik
- ✅ Fitur tambahan/bonus

## 📤 Cara Mengumpulkan Tugas

1. Buat folder dengan nama `liburan-[namamu]`
2. Masukkan file `liburan.html` dan `style.css`
3. Jika ada gambar, masukkan juga dalam folder tersebut
4. Zip folder tersebut
5. Upload ke platform yang ditentukan

## ❓ FAQ (Pertanyaan yang Sering Ditanya)

**Q: Saya tidak punya foto liburan, gimana?**  
A: Pakai foto placeholder dari Picsum atau Unsplash, atau bisa juga pakai gambar dari internet (jangan lupa cantumkan sumber!)

**Q: Boleh pakai template dari internet?**  
A: Boleh untuk inspirasi, tapi harus dibuat sendiri. Copy-paste langsung tidak diperbolehkan!

**Q: Cara buka file HTML di browser?**  
A: Double click file HTML, atau klik kanan → Open with → Browser pilihan kamu

**Q: CSS saya tidak muncul, kenapa?**  
A: Pastikan link ke CSS di HTML sudah benar: `<link rel="stylesheet" href="style.css">`

**Q: Bisa pakai framework CSS seperti Bootstrap?**  
A: Untuk tugas ini, coba buat manual dulu supaya paham dasarnya. Framework bisa dipelajari nanti!

---

## 🚀 Selamat Belajar dan Berkreasi!

Ingat, website pertama tidak harus sempurna. Yang penting adalah kamu belajar dan mencoba! Happy coding! 💻✨

**Deadline:** [Sesuaikan dengan jadwal]

**Ada pertanyaan?** Jangan ragu untuk bertanya di grup atau saat pertemuan!
