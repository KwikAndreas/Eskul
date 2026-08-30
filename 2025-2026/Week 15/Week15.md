# Week 15: Aturan Dasar HTML & CSS yang Benar

---

## Tujuan Pembelajaran

Setelah belajar hari ini, kalian akan paham:

1. ✅ Aturan menulis HTML yang benar dan mengapa penting
2. ✅ Aturan menulis CSS yang optimal
3. ✅ Struktur kode yang rapi dan mudah dibaca
4. ✅ Kesalahan umum yang harus dihindari

---

## Bagian 1: Aturan Dasar HTML (20 menit)

### 1.1 Struktur HTML yang HARUS Ada

Setiap file HTML **wajib** memiliki struktur ini:

```html
<!DOCTYPE html>
<html lang="id">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Judul Halaman</title>
  </head>
  <body>
    <!-- Konten di sini -->
  </body>
</html>
```

**Mengapa harus seperti ini?**

| Bagian                   | Fungsi                                                      | Mengapa Penting?                                  |
| ------------------------ | ----------------------------------------------------------- | ------------------------------------------------- |
| `<!DOCTYPE html>`        | Memberitahu browser ini adalah HTML5                        | Browser bisa menampilkan dengan benar             |
| `<html lang="id">`       | Pembungkus semua kode, `lang="id"` artinya bahasa Indonesia | Membantu Google dan pembaca layar memahami bahasa |
| `<head>`                 | Informasi tentang website                                   | Tempat menaruh title, CSS, dan setting penting    |
| `<meta charset="UTF-8">` | Encoding karakter                                           | Agar huruf Indonesia (é, ñ, dll) tampil benar     |
| `<meta name="viewport">` | Setting tampilan di HP                                      | Website responsive di layar kecil                 |
| `<title>`                | Judul di tab browser                                        | User tahu isi halaman ini                         |
| `<body>`                 | Konten yang terlihat                                        | Semua yang muncul di layar ada di sini            |

---

### 1.2 Aturan Penulisan Tag HTML

#### ✅ **BENAR** - Tag Harus Ditutup

```html
<!-- Tag berpasangan WAJIB ditutup -->
<p>Ini paragraf</p>
<div>Ini div</div>
<h1>Ini heading</h1>

<!-- Tag tunggal pakai self-closing -->
<img src="gambar.jpg" alt="Gambar" />
<br />
<hr />
<input type="text" />
```

#### ❌ **SALAH** - Lupa Menutup Tag

```html
<!-- Jangan seperti ini! -->
<p>Ini paragraf</p>
<div>
  Ini div <img src="gambar.jpg" />
  <!-- Kurang / di akhir -->
</div>
```

**Mengapa harus ditutup?**  
Kalau tidak ditutup, browser bingung di mana tag selesai. Hasilnya tampilan berantakan!

---

### 1.3 Aturan Nesting (Pemasangan) Tag

**Aturan: Tag yang dibuka terakhir harus ditutup duluan**

#### ✅ **BENAR** - Nesting yang Rapi

```html
<div>
  <p>Ini teks <strong>tebal</strong> di dalam paragraf</p>
</div>
```

Urutan: `div` buka → `p` buka → `strong` buka → `strong` tutup → `p` tutup → `div` tutup

#### ❌ **SALAH** - Nesting yang Berantakan

```html
<div>
  <p>
    Ini teks <strong>tebal</p>
  </strong>
</div>
```

**Mengapa harus rapi?**  
Seperti kurung dalam matematika: `( { [ ] } )` harus urut. Kalau berantakan, browser error!

---

### 1.4 Aturan Penamaan & Atribut

#### ✅ **BENAR** - Nama yang Jelas dan Konsisten

```html
<!-- ID untuk elemen unik (hanya 1 di halaman) -->
<div id="header-utama">Header</div>

<!-- Class untuk elemen yang bisa banyak -->
<p class="paragraf-merah">Paragraf 1</p>
<p class="paragraf-merah">Paragraf 2</p>

<!-- Nama pakai huruf kecil dan strip (-) -->
<div class="kartu-project">
  <h3 class="judul-kartu">Project 1</h3>
</div>
```

#### ❌ **SALAH** - Penamaan yang Buruk

```html
<!-- Jangan pakai spasi! -->
<div class="kartu project">SALAH</div>

<!-- Jangan pakai huruf besar campur aduk -->
<div class="KartuProject">Tidak konsisten</div>

<!-- Jangan pakai nama yang tidak jelas -->
<div class="a1">Apa ini?</div>
<div class="div1">Tidak bermakna</div>
```

**Aturan Emas Penamaan:**

- ✅ Gunakan huruf kecil semua
- ✅ Pakai strip `-` untuk pemisah (bukan spasi atau underscore)
- ✅ Nama harus jelas dan bermakna
- ✅ ID unik (hanya 1 kali), Class bisa banyak

**Mengapa penting?**  
Nama yang jelas membuat kode mudah dipahami oleh kamu dan orang lain. 6 bulan kemudian kalau buka lagi, langsung paham!

---

### 1.5 Aturan Indentasi (Jarak Menjorok)

**Indentasi = jarak menjorok untuk menunjukkan level/tingkat**

#### ✅ **BENAR** - Rapi dan Mudah Dibaca

```html
<body>
  <header>
    <h1>Judul Website</h1>
    <nav>
      <ul>
        <li><a href="#home">Home</a></li>
        <li><a href="#about">About</a></li>
      </ul>
    </nav>
  </header>
  <main>
    <section>
      <h2>Section Title</h2>
      <p>Paragraf di dalam section.</p>
    </section>
  </main>
</body>
```

**Aturan Indentasi:**

- Setiap level dalam = geser 2 atau 4 spasi (pilih salah satu, konsisten!)
- Tag anak lebih menjorok dari tag induk

#### ❌ **SALAH** - Berantakan

```html
<body>
  <header>
    <h1>Judul Website</h1>
    <nav>
      <ul>
        <li><a href="#home">Home</a></li>
      </ul>
    </nav>
  </header>
</body>
```

**Mengapa harus rapi?**  
Bayangkan baca buku tanpa paragraf, spasi, atau bab. Susah banget kan? Kode juga sama!

---

## 🎨 Bagian 2: Aturan Dasar CSS (20 menit)

### 2.1 Struktur CSS yang Benar

CSS terdiri dari 3 bagian:

```css
selector {
  property: value;
}
```

**Contoh Lengkap:**

```css
/* Selector - elemen mana yang di-styling */
h1 {
  /* Property: value; */
  color: blue;
  font-size: 24px;
  margin-bottom: 10px;
}

/* Class selector pakai titik */
.tombol-merah {
  background-color: red;
  color: white;
  padding: 10px 20px;
}

/* ID selector pakai pagar */
#header-utama {
  background-color: navy;
  height: 80px;
}
```

**Aturan Penulisan:**

1. Setiap property diakhiri dengan `;` (titik koma)
2. Setiap pasangan property-value dalam `{ }` (kurung kurawal)
3. Gunakan `:` (titik dua) antara property dan value

---

### 2.2 Tipe-Tipe Selector

#### **1. Element Selector** - Memilih semua elemen

```css
/* Semua paragraf jadi merah */
p {
  color: red;
}

/* Semua heading 1 jadi besar */
h1 {
  font-size: 32px;
}
```

#### **2. Class Selector** - Bisa dipakai banyak elemen

```css
/* Titik (.) sebelum nama class */
.tombol {
  background-color: blue;
  color: white;
  padding: 10px;
}
```

```html
<!-- Bisa dipakai berkali-kali -->
<button class="tombol">Klik 1</button>
<button class="tombol">Klik 2</button>
<a class="tombol">Link</a>
```

#### **3. ID Selector** - Hanya untuk 1 elemen unik

```css
/* Pagar (#) sebelum nama ID */
#nav-bar {
  background-color: black;
}
```

```html
<!-- Hanya 1 elemen punya ID ini -->
<nav id="nav-bar">Menu</nav>
```

**Kapan pakai apa?**

| Selector | Kapan Dipakai               | Contoh                          |
| -------- | --------------------------- | ------------------------------- |
| Element  | Untuk semua elemen sejenis  | Semua `<p>` jadi font 16px      |
| Class    | Untuk kelompok elemen       | Tombol-tombol dengan style sama |
| ID       | Untuk 1 elemen spesial/unik | Header utama, footer utama      |

---

### 2.3 Cara Menghubungkan CSS ke HTML

Ada 3 cara, tapi ada yang lebih baik!

#### **1. External CSS** ⭐ **PALING DIREKOMENDASIKAN**

**HTML:**

```html
<head>
  <link rel="stylesheet" href="style.css" />
</head>
```

**CSS (file: style.css):**

```css
body {
  font-family: Arial;
}
```

**✅ Keuntungan:**

- 1 file CSS untuk banyak halaman HTML
- Kode lebih rapi dan terorganisir
- Mudah di-maintain (perbaiki)
- File HTML lebih ringan

#### **2. Internal CSS** - Untuk halaman khusus

```html
<head>
  <style>
    body {
      font-family: Arial;
    }
    p {
      color: blue;
    }
  </style>
</head>
```

**⚠️ Gunakan jika:**

- Hanya 1 halaman HTML
- Style khusus untuk halaman itu saja

#### **3. Inline CSS** ❌ **HINDARI!**

```html
<p style="color: red; font-size: 16px;">Teks merah</p>
```

**❌ Masalah:**

- Sulit di-maintain (harus ubah satu-satu)
- Kode berantakan
- Tidak efisien

**Kesimpulan: SELALU pakai External CSS untuk project nyata!**

---

### 2.4 Urutan Prioritas CSS (Specificity)

Kalau ada beberapa CSS yang bentrok, mana yang menang?

**Urutan (dari yang paling kuat):**

1. **Inline CSS** (langsung di tag) - PALING KUAT
2. **ID Selector** (#id)
3. **Class Selector** (.class)
4. **Element Selector** (p, div, h1)

**Contoh:**

```html
<style>
  /* Element selector - nilai: 1 */
  p {
    color: blue;
  }

  /* Class selector - nilai: 10 */
  .teks-merah {
    color: red;
  }

  /* ID selector - nilai: 100 */
  #paragraf-khusus {
    color: green;
  }
</style>

<p>Saya biru</p>
<p class="teks-merah">Saya merah</p>
<p class="teks-merah" id="paragraf-khusus">Saya hijau</p>
<p class="teks-merah" id="paragraf-khusus" style="color: yellow;">
  Saya kuning (inline paling kuat!)
</p>
```

**Mengapa harus paham ini?**  
Nanti kalau style tidak muncul, kamu tahu karena ada yang lebih kuat (spesifik)!

---

### 2.5 Property CSS yang Sering Dipakai

#### **Warna & Background**

```css
.kotak {
  color: #333333; /* Warna teks */
  background-color: #f0f0f0; /* Warna background */
  background: linear-gradient(to bottom, #ffffff, #eeeeee); /* Gradient */
}
```

#### **Ukuran**

```css
.kotak {
  width: 300px; /* Lebar */
  height: 200px; /* Tinggi */
  max-width: 100%; /* Maksimal lebar (responsive) */
}
```

#### **Jarak**

```css
.kotak {
  margin: 20px; /* Jarak LUAR elemen */
  padding: 15px; /* Jarak DALAM elemen */

  /* Margin/Padding per sisi */
  margin-top: 10px;
  margin-right: 20px;
  margin-bottom: 10px;
  margin-left: 20px;

  /* Shorthand (atas, kanan, bawah, kiri) */
  margin: 10px 20px 10px 20px;

  /* Shorthand (atas-bawah, kanan-kiri) */
  margin: 10px 20px;
}
```

**Visualisasi Margin vs Padding:**

```
┌─────────────────────────┐
│   Margin (luar)         │
│  ┌───────────────────┐  │
│  │ Border            │  │
│  │ ┌───────────────┐ │  │
│  │ │ Padding       │ │  │
│  │ │ ┌───────────┐ │ │  │
│  │ │ │  Content  │ │ │  │
│  │ │ └───────────┘ │ │  │
│  │ └───────────────┘ │  │
│  └───────────────────┘  │
└─────────────────────────┘
```

#### **Teks**

```css
.teks {
  font-family: Arial, sans-serif; /* Font */
  font-size: 16px; /* Ukuran font */
  font-weight: bold; /* Ketebalan (bold/normal) */
  text-align: center; /* Alignment (left/center/right) */
  line-height: 1.5; /* Jarak antar baris */
  text-decoration: none; /* Hilangkan underline di link */
}
```

#### **Border & Radius**

```css
.kotak {
  border: 2px solid #000000; /* Border: tebal, style, warna */
  border-radius: 10px; /* Sudut membulat */

  /* Border per sisi */
  border-top: 1px solid red;
  border-right: 2px dashed blue;
}
```

---

## ⚡ Bagian 3: Best Practices & Kesalahan Umum (10 menit)

### 3.1 Aturan Emas Kode yang Bagus

#### ✅ **DO (Lakukan)**

1. **Gunakan nama yang bermakna**

   ```css
   /* BAIK */
   .tombol-submit {
   }
   .kartu-produk {
   }

   /* BURUK */
   .btn1 {
   }
   .box {
   }
   ```

2. **Kelompokkan CSS dengan komentar**

   ```css
   /* ========== NAVIGATION ========== */
   .nav-bar {
   }
   .nav-link {
   }

   /* ========== BUTTONS ========== */
   .tombol {
   }
   .tombol-besar {
   }
   ```

3. **Gunakan shorthand jika bisa**

   ```css
   /* Panjang */
   margin-top: 10px;
   margin-right: 15px;
   margin-bottom: 10px;
   margin-left: 15px;

   /* Singkat - LEBIH BAIK */
   margin: 10px 15px;
   ```

4. **Konsisten dengan satuan**
   ```css
   /* Gunakan px untuk border, rem/em untuk text */
   font-size: 1rem; /* Responsive */
   border: 1px solid; /* Tetap */
   padding: 1rem; /* Responsive */
   ```

#### ❌ **DON'T (Jangan)**

1. **Jangan pakai terlalu banyak ID**

   ```css
   /* BURUK - terlalu banyak ID */
   #header {
   }
   #menu {
   }
   #content {
   }

   /* BAIK - pakai class */
   .header {
   }
   .menu {
   }
   .content {
   }
   ```

2. **Jangan inline CSS berlebihan**

   ```html
   <!-- BURUK -->
   <p style="color: red; font-size: 16px; margin: 10px;">Teks</p>

   <!-- BAIK -->
   <p class="teks-khusus">Teks</p>
   ```

3. **Jangan duplikasi code**

   ```css
   /* BURUK - banyak yang sama */
   .tombol-merah {
     padding: 10px;
     border-radius: 5px;
     font-size: 14px;
     background-color: red;
   }
   .tombol-biru {
     padding: 10px;
     border-radius: 5px;
     font-size: 14px;
     background-color: blue;
   }

   /* BAIK - pisahkan yang sama */
   .tombol {
     padding: 10px;
     border-radius: 5px;
     font-size: 14px;
   }
   .tombol-merah {
     background-color: red;
   }
   .tombol-biru {
     background-color: blue;
   }
   ```

---

### 3.2 Kesalahan Umum & Cara Memperbaiki

#### ❌ **Kesalahan 1: Lupa titik koma**

```css
/* SALAH */
p {
  color: red
  font-size: 16px
}

/* BENAR */
p {
  color: red;
  font-size: 16px;
}
```

#### ❌ **Kesalahan 2: Salah selector**

```html
<!-- HTML -->
<p class="paragraf-merah">Teks</p>
```

```css
/* SALAH - lupa titik untuk class */
paragraf-merah {
  color: red;
}

/* BENAR */
.paragraf-merah {
  color: red;
}
```

#### ❌ **Kesalahan 3: Tag tidak ditutup**

```html
<!-- SALAH -->
<div>
  <p>Paragraf</p>
</div>

<!-- BENAR -->
<div>
  <p>Paragraf</p>
</div>
```

#### ❌ **Kesalahan 4: Path file salah**

```html
<!-- SALAH - file ada di folder css/ -->
<link rel="stylesheet" href="style.css" />

<!-- BENAR -->
<link rel="stylesheet" href="css/style.css" />
```

---

## 🏆 Bagian 4: Checklist Kode yang Baik (5 menit)

Sebelum selesai coding, cek ini:

### ✅ **HTML Checklist**

- [ ] Ada `<!DOCTYPE html>` di awal?
- [ ] Semua tag sudah ditutup?
- [ ] Indentasi rapi dan konsisten?
- [ ] Nama class/id pakai huruf kecil dan strip (-)
- [ ] `<img>` punya atribut `alt`?
- [ ] File terorganisir (HTML, CSS, gambar di folder terpisah)?

### ✅ **CSS Checklist**

- [ ] Pakai external CSS (file .css terpisah)?
- [ ] Semua property diakhiri titik koma `;`?
- [ ] Nama class bermakna dan jelas?
- [ ] Tidak ada duplikasi code?
- [ ] Ada komentar untuk bagian-bagian penting?
- [ ] Selector tidak terlalu banyak ID?

---

## 💡 Contoh Praktis: Kode Baik vs Buruk

### ❌ **Contoh Kode BURUK**

**bad.html:**

```html
<html>
<head>
<title>web</title>
<style>
body{background-color:white;margin:0;}
.a{color:red;font-size:16px;}
#b{background-color:blue;padding:10px;}
</style>
</head>
<body>
<div id="b">
<h1 class="a">Judul
<p>ini paragraf</p>
</div>
</body>
</html>
```

**Masalah:**

- ❌ Tidak ada `<!DOCTYPE html>`
- ❌ Tidak ada `lang`, `charset`, `viewport`
- ❌ Tag `<h1>` tidak ditutup
- ❌ Indentasi berantakan
- ❌ CSS internal (harusnya external)
- ❌ CSS tidak pakai spasi, sulit dibaca
- ❌ Nama class/id tidak bermakna (a, b)

---

### ✅ **Contoh Kode BAIK**

**good.html:**

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
    <div class="container-utama">
      <h1 class="judul-merah">Judul Website</h1>
      <p class="paragraf">Ini adalah paragraf yang rapi.</p>
    </div>
  </body>
</html>
```

**style.css:**

```css
/* ========== RESET ========== */
body {
  margin: 0;
  padding: 0;
  font-family: Arial, sans-serif;
  background-color: #ffffff;
}

/* ========== CONTAINER ========== */
.container-utama {
  max-width: 800px;
  margin: 0 auto;
  padding: 20px;
  background-color: #f0f0f0;
}

/* ========== TEXT ========== */
.judul-merah {
  color: #ff0000;
  font-size: 32px;
  margin-bottom: 15px;
}

.paragraf {
  color: #333333;
  font-size: 16px;
  line-height: 1.6;
}
```

**Keuntungan:**

- ✅ Struktur HTML lengkap dan benar
- ✅ Indentasi rapi dan konsisten
- ✅ CSS terpisah di file sendiri
- ✅ Nama class bermakna dan jelas
- ✅ Ada komentar untuk organisasi
- ✅ Mudah dibaca dan di-maintain

---

## 🎯 Kesimpulan & Rangkuman

### **Aturan Emas HTML**

1. Selalu pakai struktur lengkap (`<!DOCTYPE>`, `<html>`, `<head>`, `<body>`)
2. Tutup semua tag
3. Nesting yang rapi (buka terakhir tutup duluan)
4. Indentasi konsisten (2 atau 4 spasi)
5. Nama class/id pakai huruf kecil dan strip (-)

### **Aturan Emas CSS**

1. Pakai external CSS (file terpisah)
2. Selector: `.` untuk class, `#` untuk ID
3. Setiap property pakai titik koma `;`
4. Nama class bermakna dan jelas
5. Kelompokkan dengan komentar

### **Kenapa Aturan Ini Penting?**

| Alasan                               | Manfaat                             |
| ------------------------------------ | ----------------------------------- |
| **Kode mudah dibaca**                | Kamu dan orang lain langsung paham  |
| **Mudah di-perbaiki**                | Kalau ada error, cepat ketemu       |
| **Browser menampilkan dengan benar** | Tidak ada tampilan aneh/error       |
| **Profesional**                      | Seperti programmer sungguhan        |
| **Bisa kerja tim**                   | Orang lain bisa lanjutkan kode kamu |

---

## 📝 Tugas Mini (15 menit - di luar kelas)

Buat 1 halaman HTML sederhana tentang diri kamu dengan aturan yang BENAR:

**Syarat:**

1. ✅ Struktur HTML lengkap
2. ✅ CSS di file terpisah (style.css)
3. ✅ Minimal ada: heading, paragraf, list, gambar
4. ✅ Indentasi rapi
5. ✅ Nama class bermakna
6. ✅ Cek dengan checklist di atas

**Contoh Topik:**

- Tentang Saya
- Hobi Saya
- Cita-cita Saya
- Liburan Favorit

---

## 🔗 Referensi Tambahan

- **Validator HTML:** https://validator.w3.org/ (cek kode kamu benar atau tidak)
- **Validator CSS:** https://jigsaw.w3.org/css-validator/
- **Belajar lebih lanjut:** https://www.w3schools.com/

---
