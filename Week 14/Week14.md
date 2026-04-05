# Week 14: HTML & CSS Dasar

---

## 📝 Bagian 1: Pengenalan HTML (15 menit)

### Apa itu HTML?

HTML adalah bahasa untuk membuat halaman web. Seperti kerangka rumah yang menentukan struktur website.

### Struktur Dasar HTML

```html
<!DOCTYPE html>
<html>
  <head>
    <title>Website Pertamaku</title>
  </head>
  <body>
    <h1>Halo Dunia!</h1>
    <p>Ini website pertama saya</p>
  </body>
</html>
```

**Penjelasan Cepat:**

- `<!DOCTYPE html>` - Memberitahu browser ini file HTML
- `<html>` - Pembungkus semua kode
- `<head>` - Informasi website (tidak terlihat di halaman)
- `<title>` - Judul di tab browser
- `<body>` - Konten yang terlihat di halaman

---

## 🏷️ Bagian 2: Tag HTML Penting (15 menit)

### Tag Teks

```html
<h1>Judul Besar</h1>
<h2>Judul Sedang</h2>
<h3>Judul Kecil</h3>
<p>Ini paragraf biasa</p>
<b>Teks tebal</b>
<i>Teks miring</i>
<br />
<!-- Pindah baris -->
<hr />
<!-- Garis horizontal -->
```

### Tag Gambar dan Link

```html
<!-- Gambar -->
<img src="gambar.jpg" alt="Deskripsi gambar" />

<!-- Link -->
<a href="https://google.com">Klik di sini</a>
```

### Tag List

```html
<!-- List bernomor -->
<ol>
  <li>Item pertama</li>
  <li>Item kedua</li>
</ol>

<!-- List tanpa nomor -->
<ul>
  <li>Apel</li>
  <li>Jeruk</li>
</ul>
```

### Tag Wadah (Container)

```html
<div>Wadah untuk mengelompokkan konten</div>
```

---

## 🎨 Bagian 3: Inline CSS (20 menit)

### Apa itu Inline CSS?

CSS inline ditulis **langsung di dalam tag HTML** menggunakan atribut `style`.

**Format:**

```html
<tag style="properti: nilai;">Konten</tag>
```

### CSS untuk Warna

```html
<!-- Warna teks -->
<h1 style="color: blue;">Judul Biru</h1>
<p style="color: red;">Paragraf merah</p>

<!-- Warna background -->
<div style="background-color: yellow;">Kotak kuning</div>
```

**Warna populer:** red, blue, green, yellow, orange, purple, pink, black, white, gray

### CSS untuk Ukuran dan Font

```html
<!-- Ukuran font -->
<p style="font-size: 20px;">Teks besar</p>
<p style="font-size: 12px;">Teks kecil</p>

<!-- Jenis font -->
<p style="font-family: Arial;">Font Arial</p>
<p style="font-family: Courier;">Font Courier</p>

<!-- Tebal dan miring -->
<p style="font-weight: bold;">Teks tebal</p>
<p style="font-style: italic;">Teks miring</p>
```

### CSS untuk Ukuran dan Jarak

```html
<!-- Lebar dan tinggi -->
<div style="width: 300px; height: 100px; background-color: lightblue;">
  Kotak 300x100 pixel
</div>

<!-- Padding (jarak dalam) -->
<div style="padding: 20px; background-color: lightgreen;">
  Teks dengan ruang di dalam
</div>

<!-- Margin (jarak luar) -->
<p style="margin: 30px; background-color: pink;">
  Paragraf dengan jarak ke luar
</p>
```

### CSS untuk Border (Garis Tepi)

```html
<!-- Border dasar -->
<div style="border: 2px solid black;">Kotak dengan garis hitam</div>

<!-- Border berwarna -->
<div style="border: 3px solid red; padding: 10px;">Kotak garis merah</div>

<!-- Border rounded -->
<div style="border: 2px solid blue; border-radius: 10px; padding: 15px;">
  Kotak dengan sudut melengkung
</div>
```

### CSS untuk Perataan Teks

```html
<p style="text-align: left;">Teks kiri</p>
<p style="text-align: center;">Teks tengah</p>
<p style="text-align: right;">Teks kanan</p>
```

### Menggabungkan Beberapa Style

Pisahkan dengan titik koma (`;`)

```html
<h1
  style="color: white; background-color: blue; padding: 20px; text-align: center;"
>
  Judul Cantik
</h1>

<div
  style="width: 400px; background-color: lightgray; padding: 20px; border: 3px solid darkgray; border-radius: 15px;"
>
  <h2 style="color: navy;">Kartu Profil</h2>
  <p style="font-size: 16px;">Ini adalah contoh kartu dengan styling lengkap</p>
</div>
```

---

## ✏️ Bagian 4: Praktek - Buat Halaman Profil (10 menit)

### Tugas: Buat halaman profil diri sendiri!

**File: profil.html**

```html
<!DOCTYPE html>
<html>
  <head>
    <title>Profil Saya</title>
  </head>
  <body style="background-color: #f0f0f0; font-family: Arial; padding: 20px;">
    <!-- Header -->
    <div
      style="background-color: #4CAF50; color: white; padding: 30px; text-align: center; border-radius: 10px;"
    >
      <h1 style="margin: 0;">Nama Kamu</h1>
      <p style="margin: 5px 0 0 0;">Siswa SMP</p>
    </div>

    <!-- Foto (opsional) -->
    <div style="text-align: center; margin: 20px 0;">
      <img
        src="foto.jpg"
        alt="Foto saya"
        style="width: 150px; height: 150px; border-radius: 50%; border: 5px solid #4CAF50;"
      />
    </div>

    <!-- Tentang Saya -->
    <div
      style="background-color: white; padding: 20px; margin: 20px 0; border-radius: 10px; border: 2px solid #ddd;"
    >
      <h2 style="color: #4CAF50;">Tentang Saya</h2>
      <p style="line-height: 1.6;">
        Halo! Nama saya [Nama]. Saya suka [hobi]. Cita-cita saya adalah
        [cita-cita].
      </p>
    </div>

    <!-- Hobi -->
    <div
      style="background-color: white; padding: 20px; margin: 20px 0; border-radius: 10px; border: 2px solid #ddd;"
    >
      <h2 style="color: #4CAF50;">Hobi Saya</h2>
      <ul style="line-height: 1.8;">
        <li>Hobi 1</li>
        <li>Hobi 2</li>
        <li>Hobi 3</li>
      </ul>
    </div>

    <!-- Kontak -->
    <div
      style="background-color: #333; color: white; padding: 20px; text-align: center; border-radius: 10px; margin-top: 20px;"
    >
      <p style="margin: 0;">Email: email@example.com</p>
      <p style="margin: 10px 0 0 0;">Instagram: @username</p>
    </div>
  </body>
</html>
```

---

## 📋 Cheatsheet CSS Inline Penting

| Properti           | Fungsi           | Contoh                      |
| ------------------ | ---------------- | --------------------------- |
| `color`            | Warna teks       | `color: red;`               |
| `background-color` | Warna latar      | `background-color: yellow;` |
| `font-size`        | Ukuran huruf     | `font-size: 20px;`          |
| `font-family`      | Jenis huruf      | `font-family: Arial;`       |
| `text-align`       | Perataan teks    | `text-align: center;`       |
| `width`            | Lebar            | `width: 300px;`             |
| `height`           | Tinggi           | `height: 100px;`            |
| `padding`          | Jarak dalam      | `padding: 20px;`            |
| `margin`           | Jarak luar       | `margin: 10px;`             |
| `border`           | Garis tepi       | `border: 2px solid black;`  |
| `border-radius`    | Sudut melengkung | `border-radius: 10px;`      |

---

## 🎯 Tips Penting

### ✅ DO (Lakukan)

- Tutup semua tag yang dibuka
- Gunakan nama warna yang jelas
- Beri jarak dengan padding/margin
- Uji coba di browser

### ❌ DON'T (Jangan)

- Lupa tutup tag
- Terlalu banyak warna (pilih 2-3 warna saja)
- Ukuran font terlalu kecil atau besar
- Copy-paste tanpa memahami

---

## 🏆 Challenge (Tantangan)

Modifikasi halaman profil kamu dengan:

1. Ganti warna tema (bukan hijau)
2. Tambah section "Pelajaran Favorit"
3. Tambah 1 gambar (bisa dari internet)
4. Buat tombol "Hubungi Saya" dengan styling menarik

**Contoh Tombol:**

```html
<a
  href="#"
  style="display: inline-block; background-color: #008CBA; color: white; padding: 15px 30px; text-decoration: none; border-radius: 5px; font-weight: bold;"
>
  Hubungi Saya
</a>
```

---

## 💡 Kelebihan dan Kekurangan Inline CSS

### ✅ Kelebihan

- Cepat untuk belajar
- Langsung terlihat hasilnya
- Tidak perlu file CSS terpisah
- Cocok untuk styling satu elemen

### ❌ Kekurangan

- Kode jadi panjang dan sulit dibaca
- Tidak efisien untuk website besar
- Sulit diubah jika banyak elemen
- Tidak bisa dipakai ulang

**Next Level:** Minggu depan kita akan belajar **External CSS** yang lebih rapi dan profesional!

---

## 📚 Rangkuman 1 Jam

1. **15 menit:** Struktur HTML dasar
2. **15 menit:** Tag-tag HTML penting (h1-h6, p, img, a, ul, ol, div)
3. **20 menit:** Inline CSS (color, font, size, border, padding, margin)
4. **10 menit:** Praktek membuat halaman profil

---

## 🎓 Tugas Rumah

Buat halaman web tentang topik favoritmu:

- Film/anime favorit
- Buku favorit
- Game favorit
- Tempat wisata impian

**Minimal harus ada:**

- 1 judul besar (h1)
- 2 subjudul (h2)
- 3 paragraf
- 1 gambar
- 1 list (ul atau ol)
- Minimal 5 inline CSS yang berbeda

**Deadline:** Jumat 13 Febuari 2026 Jam 18.00, Dikumpulkan dengan mengirim file HTML/CSS ke Whatsapp 081292698237

---

**Selamat Belajar! 🚀**
