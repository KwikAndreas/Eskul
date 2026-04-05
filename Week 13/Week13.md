# Week 13: Membuat Website yang Profesional dengan HTML & CSS

**Yang akan kita pelajari:**

1. ✅ Struktur HTML yang rapi dan terorganisir
2. ✅ CSS External vs Internal - kapan menggunakan yang mana
3. ✅ Teknik styling yang membuat website terlihat modern
4. ✅ Layout yang profesional dengan CSS sederhana

---

## 📚 Bagian 1: Struktur HTML yang Baik (15 menit)

### Prinsip HTML yang Terstruktur

**❌ HTML yang Berantakan (Seperti minggu lalu):**

```html
<h3>Ini seharusnya paragraf</h3>
<p>Ini cerita saya...</p>
<h3>Ini juga paragraf lagi</h3>
<br /><br /><br /><br />
<p>Spasi dengan banyak br</p>
```

**✅ HTML yang Terstruktur dan Rapi:**

```html
<section class="content-section">
  <h2>Judul Section</h2>
  <p>
    Ini paragraf yang benar. Menggunakan CSS untuk styling, bukan tag yang
    salah.
  </p>
  <p>Paragraf kedua dengan jarak yang tepat menggunakan CSS margin.</p>
</section>
```

### Semantic HTML - Gunakan Tag yang Tepat

**Semantic HTML** artinya menggunakan tag sesuai dengan makna/tujuannya, bukan hanya tampilannya.

```html
<!DOCTYPE html>
<html lang="id">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Website Profesional</title>
    <link rel="stylesheet" href="style.css" />
  </head>
  <body>
    <!-- HEADER: Bagian atas website -->
    <header>
      <h1>Portfolio Saya</h1>
      <nav>
        <ul>
          <li><a href="#about">Tentang</a></li>
          <li><a href="#projects">Project</a></li>
          <li><a href="#contact">Kontak</a></li>
        </ul>
      </nav>
    </header>

    <!-- MAIN: Konten utama -->
    <main>
      <section id="about">
        <h2>Tentang Saya</h2>
        <p>Deskripsi singkat tentang diri kamu.</p>
      </section>

      <section id="projects">
        <h2>Project Saya</h2>
        <div class="project-card">
          <h3>Project 1</h3>
          <p>Deskripsi project</p>
        </div>
      </section>
    </main>

    <!-- FOOTER: Bagian bawah -->
    <footer>
      <p>&copy; 2026 Nama Kamu. All rights reserved.</p>
    </footer>
  </body>
</html>
```

**Kenapa pakai semantic HTML?**

- ✅ Kode lebih mudah dibaca dan dipahami
- ✅ Google bisa lebih mudah memahami website kamu
- ✅ Lebih mudah untuk di-styling dengan CSS
- ✅ Terlihat lebih profesional

---

## 🎨 Bagian 2: CSS External vs Internal (15 menit)

### Perbedaan External dan Internal CSS

#### 1️⃣ Internal CSS (Di dalam HTML)

**Kapan digunakan?**

- Website hanya 1 halaman
- Styling yang sangat spesifik untuk halaman tertentu
- Prototype cepat

```html
<!DOCTYPE html>
<html lang="id">
  <head>
    <meta charset="UTF-8" />
    <title>Website dengan Internal CSS</title>

    <!-- INTERNAL CSS: Ditulis di dalam tag <style> -->
    <style>
      body {
        font-family: "Segoe UI", Arial, sans-serif;
        margin: 0;
        padding: 0;
        background-color: #f5f5f5;
      }

      header {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        padding: 2rem;
        text-align: center;
      }

      h1 {
        margin: 0;
        font-size: 2.5rem;
      }
    </style>
  </head>
  <body>
    <header>
      <h1>Website Saya</h1>
    </header>
  </body>
</html>
```

**Kelebihan Internal CSS:**

- ✅ Semua kode dalam 1 file
- ✅ Tidak perlu file tambahan
- ✅ Loading lebih cepat (tidak perlu download file CSS terpisah)

**Kekurangan:**

- ❌ Tidak bisa digunakan di halaman lain
- ❌ File HTML jadi panjang dan berantakan
- ❌ Sulit di-maintain kalau website besar

---

#### 2️⃣ External CSS (File Terpisah)

**Kapan digunakan?**

- Website lebih dari 1 halaman
- Ingin CSS bisa digunakan ulang
- Project yang lebih besar dan profesional

**File: index.html**

```html
<!DOCTYPE html>
<html lang="id">
  <head>
    <meta charset="UTF-8" />
    <title>Website dengan External CSS</title>

    <!-- EXTERNAL CSS: Link ke file CSS terpisah -->
    <link rel="stylesheet" href="style.css" />
  </head>
  <body>
    <header>
      <h1>Website Saya</h1>
    </header>
    <main>
      <section class="hero">
        <h2>Selamat Datang!</h2>
        <p>Ini adalah website profesional saya.</p>
      </section>
    </main>
  </body>
</html>
```

**File: style.css** (File terpisah)

```css
/* Reset dan Base Styles */
* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

body {
  font-family: "Segoe UI", Tahoma, Geneva, Verdana, sans-serif;
  line-height: 1.6;
  color: #333;
  background-color: #f8f9fa;
}

/* Header Styling */
header {
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  color: white;
  padding: 2rem;
  text-align: center;
  box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
}

h1 {
  font-size: 2.5rem;
  margin-bottom: 0.5rem;
}

/* Hero Section */
.hero {
  max-width: 800px;
  margin: 3rem auto;
  padding: 2rem;
  background: white;
  border-radius: 10px;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
}

.hero h2 {
  color: #667eea;
  margin-bottom: 1rem;
}
```

**Kelebihan External CSS:**

- ✅ Bisa digunakan di banyak halaman HTML
- ✅ HTML tetap bersih dan mudah dibaca
- ✅ Lebih mudah di-maintain dan diubah
- ✅ Browser bisa cache file CSS (website lebih cepat)

**Kekurangan:**

- ❌ Perlu file tambahan
- ❌ Sedikit lebih lambat di loading pertama

---

### 🤔 Mana yang Sebaiknya Digunakan?

| Situasi                     | Pilihan          | Alasan                             |
| --------------------------- | ---------------- | ---------------------------------- |
| Website 1 halaman sederhana | Internal CSS     | Lebih praktis, semua dalam 1 file  |
| Website multi-halaman       | External CSS     | CSS bisa dipakai ulang             |
| Portfolio/Project besar     | External CSS     | Lebih terorganisir dan profesional |
| Prototype cepat             | Internal CSS     | Lebih cepat untuk testing          |
| **Untuk latihan hari ini**  | **External CSS** | **Belajar cara profesional**       |

---

## 💎 Bagian 3: Teknik CSS yang Membuat Website Terlihat Profesional (20 menit)

### 1. Spacing yang Konsisten

**❌ Spacing yang Berantakan:**

```css
.card {
  padding: 5px;
  margin: 3px;
}

.header {
  padding: 25px;
  margin: 7px;
}
```

**✅ Spacing yang Konsisten (Menggunakan sistem 8px):**

```css
/* Gunakan kelipatan 8: 8px, 16px, 24px, 32px, 40px */

.card {
  padding: 16px;
  margin: 16px;
}

.header {
  padding: 24px;
  margin: 0;
}

.section {
  padding: 32px 16px;
  margin-bottom: 24px;
}
```

---

### 2. Warna yang Harmonis

**❌ Warna yang Asal-asalan:**

```css
body {
  background: yellow;
}
header {
  background: red;
}
button {
  background: lime;
  color: blue;
}
```

**✅ Palet Warna yang Profesional:**

```css
:root {
  /* Primary Colors */
  --color-primary: #667eea;
  --color-primary-dark: #5568d3;

  /* Neutral Colors */
  --color-text: #2d3748;
  --color-text-light: #718096;
  --color-background: #f7fafc;
  --color-white: #ffffff;

  /* Accent */
  --color-accent: #48bb78;
}

body {
  background-color: var(--color-background);
  color: var(--color-text);
}

.button-primary {
  background-color: var(--color-primary);
  color: var(--color-white);
}

.button-primary:hover {
  background-color: var(--color-primary-dark);
}
```

**Sumber Palet Warna:**

- [Coolors.co](https://coolors.co) - Generator warna otomatis
- [ColorHunt.co](https://colorhunt.co) - Koleksi palet siap pakai

---

### 3. Typography yang Rapi

**✅ Hierarki Ukuran Font yang Jelas:**

```css
/* Font Sizes - Gunakan skala yang konsisten */
h1 {
  font-size: 2.5rem; /* 40px */
  font-weight: 700;
  line-height: 1.2;
  margin-bottom: 1rem;
}

h2 {
  font-size: 2rem; /* 32px */
  font-weight: 600;
  line-height: 1.3;
  margin-bottom: 0.75rem;
}

h3 {
  font-size: 1.5rem; /* 24px */
  font-weight: 600;
  line-height: 1.4;
}

p {
  font-size: 1rem; /* 16px */
  line-height: 1.6;
  margin-bottom: 1rem;
}

small {
  font-size: 0.875rem; /* 14px */
}
```

---

### 4. Shadow & Border Radius untuk Depth

**Tanpa shadow = Flat dan membosankan**
**Dengan shadow = Terlihat modern dan depth**

```css
.card {
  background: white;
  border-radius: 10px;
  padding: 24px;

  /* Shadow yang subtle tapi efektif */
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);

  /* Animasi saat hover */
  transition:
    transform 0.3s ease,
    box-shadow 0.3s ease;
}

.card:hover {
  transform: translateY(-5px);
  box-shadow: 0 8px 15px rgba(0, 0, 0, 0.15);
}
```

---

### 5. Layout dengan Flexbox (Simple & Powerful)

```css
/* Container Utama */
.container {
  max-width: 1200px;
  margin: 0 auto;
  padding: 0 16px;
}

/* Flexbox untuk Card Grid */
.card-grid {
  display: flex;
  gap: 24px;
  flex-wrap: wrap;
}

.card {
  flex: 1 1 300px; /* Grow, shrink, basis */
  background: white;
  border-radius: 10px;
  padding: 24px;
}

/* Center Content Vertikal & Horizontal */
.center-content {
  display: flex;
  justify-content: center;
  align-items: center;
  min-height: 300px;
}
```

---

## 🚀 Bagian 4: Project Praktik - Website Portfolio Sederhana (10 menit)

### Final Project: Buat Website Portfolio yang Profesional

**Struktur File:**

```
Week 13/
  ├── index.html
  └── style.css
```

### File: index.html

```html
<!DOCTYPE html>
<html lang="id">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Portfolio - Nama Kamu</title>
    <link rel="stylesheet" href="style.css" />
  </head>
  <body>
    <!-- Navigation -->
    <nav class="navbar">
      <div class="container">
        <h1 class="logo">Portfolio Ku</h1>
        <ul class="nav-links">
          <li><a href="#about">Tentang</a></li>
          <li><a href="#skills">Skill</a></li>
          <li><a href="#projects">Project</a></li>
          <li><a href="#contact">Kontak</a></li>
        </ul>
      </div>
    </nav>

    <!-- Hero Section -->
    <header class="hero">
      <div class="container">
        <h1 class="hero-title">
          Halo, Saya <span class="highlight">Nama Kamu</span>
        </h1>
        <p class="hero-subtitle">
          Pelajar SMP yang Sedang Belajar Web Development
        </p>
        <a href="#projects" class="btn btn-primary">Lihat Project Saya</a>
      </div>
    </header>

    <!-- About Section -->
    <section id="about" class="section">
      <div class="container">
        <h2 class="section-title">Tentang Saya</h2>
        <div class="about-content">
          <p>
            Halo! Saya adalah pelajar SMP yang tertarik dengan dunia web
            development. Saya sedang belajar HTML, CSS, dan Python untuk membuat
            website dan aplikasi sederhana.
          </p>
          <p>
            Saya senang belajar hal-hal baru dan terus mengembangkan skill saya
            di bidang teknologi.
          </p>
        </div>
      </div>
    </section>

    <!-- Skills Section -->
    <section id="skills" class="section section-gray">
      <div class="container">
        <h2 class="section-title">Skill yang Sedang Dipelajari</h2>
        <div class="skills-grid">
          <div class="skill-card">
            <h3>HTML</h3>
            <p>Struktur dasar website dan semantic HTML</p>
          </div>
          <div class="skill-card">
            <h3>CSS</h3>
            <p>Styling website agar terlihat menarik</p>
          </div>
          <div class="skill-card">
            <h3>Python</h3>
            <p>Programming dasar dan logic</p>
          </div>
          <div class="skill-card">
            <h3>Problem Solving</h3>
            <p>Berpikir logis dan menyelesaikan masalah</p>
          </div>
        </div>
      </div>
    </section>

    <!-- Projects Section -->
    <section id="projects" class="section">
      <div class="container">
        <h2 class="section-title">Project Saya</h2>
        <div class="projects-grid">
          <div class="project-card">
            <div class="project-header">
              <h3>Website Liburan</h3>
              <span class="project-tag">HTML & CSS</span>
            </div>
            <p>
              Website storytelling tentang pengalaman liburan saya menggunakan
              HTML dan CSS.
            </p>
            <a href="#" class="project-link">Lihat Project →</a>
          </div>

          <div class="project-card">
            <div class="project-header">
              <h3>Kalkulator Python</h3>
              <span class="project-tag">Python</span>
            </div>
            <p>
              Program kalkulator sederhana yang dibuat dengan Python untuk
              melakukan operasi matematika.
            </p>
            <a href="#" class="project-link">Lihat Project →</a>
          </div>

          <div class="project-card">
            <div class="project-header">
              <h3>Game Tebak Angka</h3>
              <span class="project-tag">Python</span>
            </div>
            <p>
              Game interaktif sederhana untuk menebak angka menggunakan logic
              Python.
            </p>
            <a href="#" class="project-link">Lihat Project →</a>
          </div>
        </div>
      </div>
    </section>

    <!-- Contact Section -->
    <section id="contact" class="section section-gray">
      <div class="container">
        <h2 class="section-title">Hubungi Saya</h2>
        <div class="contact-content">
          <p>Punya pertanyaan atau ingin berkolaborasi? Hubungi saya!</p>
          <div class="contact-links">
            <a href="mailto:email@example.com" class="btn btn-secondary"
              >Email Saya</a
            >
            <a href="#" class="btn btn-secondary">Instagram</a>
          </div>
        </div>
      </div>
    </section>

    <!-- Footer -->
    <footer class="footer">
      <div class="container">
        <p>&copy; 2026 Nama Kamu. Dibuat dengan ❤️ menggunakan HTML & CSS</p>
      </div>
    </footer>
  </body>
</html>
```

---

### File: style.css

```css
/* ============================================
   RESET & BASE STYLES
   ============================================ */
* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

:root {
  /* Colors */
  --primary: #6366f1;
  --primary-dark: #4f46e5;
  --secondary: #ec4899;
  --text: #1f2937;
  --text-light: #6b7280;
  --background: #ffffff;
  --background-gray: #f9fafb;
  --border: #e5e7eb;

  /* Spacing */
  --spacing-xs: 8px;
  --spacing-sm: 16px;
  --spacing-md: 24px;
  --spacing-lg: 32px;
  --spacing-xl: 48px;

  /* Shadows */
  --shadow-sm: 0 2px 4px rgba(0, 0, 0, 0.05);
  --shadow-md: 0 4px 6px rgba(0, 0, 0, 0.1);
  --shadow-lg: 0 10px 15px rgba(0, 0, 0, 0.1);
}

body {
  font-family: "Segoe UI", Tahoma, Geneva, Verdana, sans-serif;
  line-height: 1.6;
  color: var(--text);
  background-color: var(--background);
}

/* ============================================
   CONTAINER & LAYOUT
   ============================================ */
.container {
  max-width: 1200px;
  margin: 0 auto;
  padding: 0 var(--spacing-sm);
}

.section {
  padding: var(--spacing-xl) 0;
}

.section-gray {
  background-color: var(--background-gray);
}

.section-title {
  font-size: 2rem;
  font-weight: 700;
  text-align: center;
  margin-bottom: var(--spacing-lg);
  color: var(--text);
}

/* ============================================
   NAVIGATION
   ============================================ */
.navbar {
  background-color: white;
  box-shadow: var(--shadow-sm);
  position: sticky;
  top: 0;
  z-index: 100;
  padding: var(--spacing-sm) 0;
}

.navbar .container {
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.logo {
  font-size: 1.5rem;
  font-weight: 700;
  color: var(--primary);
}

.nav-links {
  display: flex;
  list-style: none;
  gap: var(--spacing-md);
}

.nav-links a {
  text-decoration: none;
  color: var(--text);
  font-weight: 500;
  transition: color 0.3s ease;
}

.nav-links a:hover {
  color: var(--primary);
}

/* ============================================
   HERO SECTION
   ============================================ */
.hero {
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  color: white;
  padding: var(--spacing-xl) 0;
  text-align: center;
  min-height: 400px;
  display: flex;
  align-items: center;
  justify-content: center;
}

.hero-title {
  font-size: 3rem;
  font-weight: 800;
  margin-bottom: var(--spacing-sm);
}

.highlight {
  color: #fbbf24;
  text-decoration: underline;
  text-decoration-color: #fbbf24;
  text-decoration-thickness: 3px;
  text-underline-offset: 5px;
}

.hero-subtitle {
  font-size: 1.25rem;
  margin-bottom: var(--spacing-md);
  opacity: 0.9;
}

/* ============================================
   BUTTONS
   ============================================ */
.btn {
  display: inline-block;
  padding: 12px 24px;
  border-radius: 8px;
  text-decoration: none;
  font-weight: 600;
  transition: all 0.3s ease;
  cursor: pointer;
}

.btn-primary {
  background-color: white;
  color: var(--primary);
  box-shadow: var(--shadow-md);
}

.btn-primary:hover {
  transform: translateY(-2px);
  box-shadow: var(--shadow-lg);
}

.btn-secondary {
  background-color: transparent;
  color: var(--primary);
  border: 2px solid var(--primary);
}

.btn-secondary:hover {
  background-color: var(--primary);
  color: white;
}

/* ============================================
   ABOUT SECTION
   ============================================ */
.about-content {
  max-width: 800px;
  margin: 0 auto;
  text-align: center;
}

.about-content p {
  font-size: 1.125rem;
  color: var(--text-light);
  margin-bottom: var(--spacing-sm);
  line-height: 1.8;
}

/* ============================================
   SKILLS SECTION
   ============================================ */
.skills-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
  gap: var(--spacing-md);
  margin-top: var(--spacing-lg);
}

.skill-card {
  background: white;
  padding: var(--spacing-md);
  border-radius: 12px;
  box-shadow: var(--shadow-md);
  text-align: center;
  transition:
    transform 0.3s ease,
    box-shadow 0.3s ease;
}

.skill-card:hover {
  transform: translateY(-5px);
  box-shadow: var(--shadow-lg);
}

.skill-card h3 {
  color: var(--primary);
  font-size: 1.5rem;
  margin-bottom: var(--spacing-xs);
}

.skill-card p {
  color: var(--text-light);
  font-size: 0.95rem;
}

/* ============================================
   PROJECTS SECTION
   ============================================ */
.projects-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
  gap: var(--spacing-md);
  margin-top: var(--spacing-lg);
}

.project-card {
  background: white;
  border-radius: 12px;
  padding: var(--spacing-md);
  box-shadow: var(--shadow-md);
  transition:
    transform 0.3s ease,
    box-shadow 0.3s ease;
  border: 1px solid var(--border);
}

.project-card:hover {
  transform: translateY(-5px);
  box-shadow: var(--shadow-lg);
  border-color: var(--primary);
}

.project-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: var(--spacing-sm);
}

.project-header h3 {
  color: var(--text);
  font-size: 1.25rem;
}

.project-tag {
  background-color: #dbeafe;
  color: var(--primary);
  padding: 4px 12px;
  border-radius: 20px;
  font-size: 0.75rem;
  font-weight: 600;
}

.project-card p {
  color: var(--text-light);
  margin-bottom: var(--spacing-sm);
  line-height: 1.6;
}

.project-link {
  color: var(--primary);
  text-decoration: none;
  font-weight: 600;
  transition: color 0.3s ease;
}

.project-link:hover {
  color: var(--primary-dark);
  text-decoration: underline;
}

/* ============================================
   CONTACT SECTION
   ============================================ */
.contact-content {
  max-width: 600px;
  margin: 0 auto;
  text-align: center;
}

.contact-content p {
  font-size: 1.125rem;
  color: var(--text-light);
  margin-bottom: var(--spacing-md);
}

.contact-links {
  display: flex;
  gap: var(--spacing-sm);
  justify-content: center;
  flex-wrap: wrap;
}

/* ============================================
   FOOTER
   ============================================ */
.footer {
  background-color: var(--text);
  color: white;
  padding: var(--spacing-md) 0;
  text-align: center;
}

.footer p {
  font-size: 0.9rem;
  opacity: 0.9;
}

/* ============================================
   RESPONSIVE DESIGN
   ============================================ */
@media (max-width: 768px) {
  .hero-title {
    font-size: 2rem;
  }

  .nav-links {
    gap: var(--spacing-sm);
  }

  .section-title {
    font-size: 1.5rem;
  }

  .skills-grid,
  .projects-grid {
    grid-template-columns: 1fr;
  }
}
```

---

## 📝 Checklist: Website yang Terlihat Profesional

Gunakan checklist ini untuk memastikan website kamu terlihat profesional:

### ✅ HTML Structure

- [ ] Menggunakan semantic HTML (`<header>`, `<nav>`, `<main>`, `<section>`, `<footer>`)
- [ ] Semua tag memiliki pembuka dan penutup yang benar
- [ ] Menggunakan tag sesuai fungsinya (heading untuk judul, `<p>` untuk paragraf)
- [ ] Ada meta viewport untuk responsive
- [ ] HTML terindentasi dengan rapi

### ✅ CSS Styling

- [ ] Menggunakan External CSS (file terpisah)
- [ ] Spacing yang konsisten (kelipatan 8px)
- [ ] Palet warna yang harmonis (max 3-4 warna utama)
- [ ] Typography dengan hierarki yang jelas
- [ ] Shadow dan border-radius untuk depth
- [ ] Hover effects pada elemen interaktif

### ✅ Professional Touch

- [ ] Layout yang rapi dengan flexbox/grid
- [ ] Tidak ada warna yang "menyakiti mata" (terlalu terang/mencolok)
- [ ] Whitespace yang cukup (tidak terlalu penuh)
- [ ] Konsistensi dalam desain (button style sama semua, card style sama semua)
- [ ] Responsive (terlihat bagus di mobile)

---

## 🎯 Tugas Praktik (Dikerjakan di Kelas)

**Buat Portfolio Website dengan kriteria:**

1. **HTML Requirements:**
   - Minimal 4 section (Hero, About, Skills/Projects, Contact)
   - Gunakan semantic HTML
   - Navigasi yang berfungsi (link ke section)

2. **CSS Requirements:**
   - **WAJIB menggunakan External CSS**
   - Gunakan minimal 3 warna yang harmonis
   - Spacing konsisten
   - Minimal 1 hover effect
   - Shadow pada card/container

3. **Professional Look:**
   - Tidak boleh menggunakan warna dasar HTML (red, blue, yellow, lime, dll)
   - Harus ada gradient atau shadow
   - Typography rapi dengan ukuran yang jelas
   - Layout terorganisir

4. **Kreativitas:**
   - Isi dengan data pribadi kamu (nama, hobi, skill yang dipelajari)
   - Tambahkan personality (warna favorit, style yang kamu suka)
   - Boleh modifikasi template yang diberikan

---

## 📚 Sumber Belajar Tambahan

### Warna & Design Inspiration:

- **Coolors.co** - Generate palet warna
- **ColorHunt.co** - Koleksi palet warna
- **Dribbble.com** - Design inspiration

### Font:

- **Google Fonts** - Font gratis untuk website
- Rekomendasi: Inter, Poppins, Roboto, Montserrat

### CSS Reference:

- **MDN Web Docs** - Dokumentasi lengkap CSS
- **CSS-Tricks.com** - Tutorial dan tips CSS

---

## 🎓 Kesimpulan

**Yang Sudah Dipelajari Hari Ini:**

1. ✅ **Struktur HTML yang Terorganisir** - Menggunakan semantic HTML dengan benar
2. ✅ **External vs Internal CSS** - Kapan menggunakan yang mana dan keuntungannya
3. ✅ **Teknik Styling Profesional** - Spacing, warna, typography, shadow
4. ✅ **Layout Modern** - Flexbox dan Grid untuk layout yang rapi
5. ✅ **Best Practices** - Cara membuat website yang tidak terlihat seperti buatan pemula

**Tips untuk Lanjutan:**

- Latihan terus dengan membuat website sederhana
- Coba modifikasi warna dan layout sesuai selera
- Lihat website profesional dan coba analisis CSS-nya (pakai Inspect Element)
- Jangan takut eksperimen dengan CSS

**Remember:**

> "Website yang profesional bukan tentang seberapa rumit kode-nya, tapi seberapa rapi dan terorganisir desainnya!"

---

**Selamat Belajar! 🚀**
