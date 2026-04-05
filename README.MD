# 🚀 Eskul Coding - SMPK Anugerah

Repositori ini berisi materi pembelajaran, tugas, dan dokumentasi perbaikan untuk Ekstrakurikuler Coding di SMPK Anugerah periode awal 2026. Fokus utama pembelajaran adalah pengembangan web dasar (**HTML**, **CSS**) dan pengenalan **JavaScript**.

## 🎯 Tujuan Pembelajaran

Project ini bertujuan untuk membimbing murid agar:

1.  **Memahami struktur Semantic HTML** yang benar.
2.  **Mengimplementasikan External CSS** untuk tampilan yang konsisten dan profesional.
3.  **Menghindari kesalahan umum** seperti penamaan file yang tidak standar (misal: `uhhhhhhhhh.html`).
4.  **Mengenal logika dasar** pemrograman menggunakan **JavaScript** (Variabel, Input, Output, dan Event).

---

## 📝 Panduan bagi Murid

### General Best Practices

- **Penamaan File**: Selalu gunakan huruf kecil semua dan tanda hubung untuk spasi
  - ✅ Benar: `data-diri.html`, `style.css`, `main.js`
  - ❌ Salah: `DataDiri.html`, `data_diri.html`, `uhhhhhhh.html`
- **Struktur HTML**: Gunakan semantic tags dengan indentasi yang benar
  - ✅ Benar: `<header>`, `<nav>`, `<main>`, `<article>`, `<footer>`
  - ❌ Salah: Semua menggunakan `<div>` (div soup)

- **CSS Organization**: Gunakan komentar untuk mengelompokkan

  ```css
  /* HEADER & NAVIGATION */
  .header { ... }

  /* HERO SECTION */
  .hero { ... }

  /* FOOTER */
  .footer { ... }
  ```

- **Validasi HTML**: Pastikan setiap tag pembuka punya penutup
  - ✅ `<img alt="..." />` (self-closing OK)
  - ❌ `<p>Text tanpa penutup`

### Week 18 Specific Tips

1. **CSS Variables adalah HARUS untuk consistency**

   ```css
   :root {
     --primary-color: #2563eb;
     --spacing-4: 16px;
   }
   ```

2. **Jangan duplicate code** - buat function yang reusable

   ```javascript
   // ✅ GOOD: Satu function untuk search & filter
   function filterAndSort() {}

   // ❌ BAD: Copy-paste logic di berbagai tempat
   ```

3. **Test responsive design** di semua ukuran:
   - Desktop (>1000px)
   - Tablet (768px)
   - Mobile (<480px)

4. **Image URLs** harus valid:
   - Gunakan official store images (apple.com, samsung.com)
   - Atau store lokal (eraspace.com)
   - Jangan lupa fallback ke placeholder

---

## 🎯 Progression Path

**Beginner (W13-W15)**

- HTML structure & CSS basics
- External stylesheets
- Proper naming & indentation

**Intermediate (W16-W17)**

- File management & organization
- JavaScript variables & DOM manipulation
- Event handling

**Advanced (W18)**

- Professional architecture (Semantic HTML)
- Design systems (CSS Variables)
- Modular code (reusable functions)
- Real-world features (e-commerce)
- Best practices & performance

---

## 📚 Additional Resources

- **MDN Web Docs**: https://developer.mozilla.org
- **CSS-Tricks**: https://css-tricks.com
- **JavaScript Info**: https://javascript.info
- **Web.dev**: https://web.dev (performance & best practices)

---

_Dikelola oleh Kwik Andreas Jonathan._
_Last Updated: April 2026_