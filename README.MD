# 🚀 Eskul Coding - SMPK Anugerah

Repositori ini berisi materi pembelajaran, tugas, dan dokumentasi perbaikan untuk Ekstrakurikuler Coding di SMPK Anugerah periode awal 2026. Fokus utama pembelajaran adalah pengembangan web dasar (**HTML**, **CSS**) dan pengenalan **JavaScript**.

## 🎯 Tujuan Pembelajaran

Project ini bertujuan untuk membimbing murid agar:

1.  **Memahami struktur Semantic HTML** yang benar.
2.  **Mengimplementasikan External CSS** untuk tampilan yang konsisten dan profesional.
3.  **Menghindari kesalahan umum** seperti penamaan file yang tidak standar (misal: `uhhhhhhhhh.html`).
4.  **Mengenal logika dasar** pemrograman menggunakan **JavaScript** (Variabel, Input, Output, dan Event).

## 📚 Rangkuman Kurikulum

|  Week   | Fokus Materi                | Key Takeaways                                                                                |
| :-----: | :-------------------------- | :------------------------------------------------------------------------------------------- |
| **W13** | Website Profesional         | Layouting dengan Flexbox & penggunaan External CSS.                                          |
| **W15** | Aturan Dasar                | Pentingnya indentasi, nesting tag, dan atribut `alt` pada gambar.                            |
| **W16** | File Management             | Standar penamaan file (kebab-case) dan penggunaan ekstensi file yang benar (.html, .css).    |
| **W17** | Basic JavaScript            | Penggunaan variabel `let`/`const`, event `onclick`, dan manipulasi DOM.                      |
| **W18** | Dari Biasa Jadi Profesional | CSS Variables, Semantic HTML, Modular JS, dan implementasi e-commerce yang fully functional. |

---

## 🎓 Detail Week 18: Dari Biasa Jadi Profesional

**Durasi:** 60 menit (1x teaching session)  
**Level:** Pemula - Menengah  
**Demo Website:** `/Week 18/TokoOnline/` - Fully functional e-commerce

### 🎯 Learning Objectives

1. **Memahami WHY** di balik professional code & design decisions
2. **Menerapkan 3 Key Principles:**
   - 🏗️ **Semantic HTML** - Struktur yang SEO-friendly & accessible
   - 🎨 **CSS Variables** - DRY principle, consistency, maintainability
   - ⚙️ **Modular JavaScript** - Reusable, testable, scalable code
3. **Implement Real E-Commerce Features:**
   - Product search & filter
   - Shopping cart with quantity management
   - Stock validation
   - Price calculation
4. **Best Practices:** Responsive design, image optimization, error handling

### 📂 Project Structure

```
Week 18/TokoOnline/
├── index.html              Homepage dengan product grid
├── cart.html              Shopping cart page
├── data.js                Product database & utilities
├── app.js                 Product page logic
├── cart.js                Cart page logic
└── style.css              Unified CSS dengan design system
```

### 🎬 Key Features Implemented

| Feature                | Implementasi               | WHY?                |
| ---------------------- | -------------------------- | ------------------- |
| **Product Search**     | Real-time search           | Users expect search |
| **Filter & Sort**      | Category & price/rating    | Better discovery    |
| **Add to Cart**        | Stock validation           | Prevent overselling |
| **Qty Management**     | Input dengan limit         | Realistic ordering  |
| **Sticky Summary**     | Always-visible cart total  | Reduce friction     |
| **Image Optimization** | Lazy loading, aspect ratio | Performance & UX    |
| **Responsive Design**  | Mobile-first               | Works everywhere    |

### 💡 3 Key Principles

**1. Semantic HTML**

```html
<!-- ✅ PREFER -->
<header><nav>...</nav></header>
<main><article>...</article></main>
```

Benefit: Better SEO, accessibility, self-documenting.

**2. CSS Variables**

```css
/* ✅ PREFER */
:root {
  --primary: #2563eb;
}
.button {
  background: var(--primary);
}
```

Benefit: DRY, one-place maintenance, easy dark mode.

**3. Modular JavaScript**

```javascript
/* ✅ PREFER */
// data.js - Single source of truth
const PRODUCTS = [...];

// app.js & cart.js - Reuse data.js
```

Benefit: Reusable, testable, maintainable.

### 📊 Quality Checklist

- ✅ Semantic HTML
- ✅ CSS Variables system
- ✅ Mobile-first responsive
- ✅ Lazy loading images
- ✅ Error handling
- ✅ No code duplication
- ✅ Clear naming
- ✅ Data centralization
- ✅ Smooth animations
- ✅ Accessibility

### 🚀 How to Run Demo

1. Open `/Week 18/TokoOnline/index.html` di browser
2. Try: Search, filter, add to cart, manage quantity
3. Modify `data.js` - perubahan otomatis di website!

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