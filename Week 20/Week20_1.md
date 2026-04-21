# Week 20: JavaScript Challenge - Perbaikan Nilai

Sebagai remediasi untuk meningkatkan nilai, berikut adalah 15 tugas JavaScript yang sedikit lebih sulit dari Week 19.
Gunakan pengetahuan yang sudah dipelajari untuk menganalisis apa yang dibutuhkan setiap tugas.

---

## Petunjuk Umum

1. Buka file `index.html` di browser dengan Live Server
2. Edit hanya bagian `<script>` - jangan ubah HTML atau CSS
3. Ikuti hint yang diberikan, tapi silakan explore lebih dalam
4. Test setiap tugas sebelum lanjut ke berikutnya
5. Gunakan DevTools (F12) untuk debug jika ada error
6. Tambahkan comments di kode Anda

---

## Bobot Penilaian

| Tugas | 1    | 2    | 3    | 4    | 5   | 6   | 7    | 8    | 9   | 10   | 11   | 12  | 13   | 14  | 15   |
| ----- | ---- | ---- | ---- | ---- | --- | --- | ---- | ---- | --- | ---- | ---- | --- | ---- | --- | ---- |
| Bobot | 3.5% | 3.5% | 3.5% | 3.5% | 3%  | 4%  | 3.5% | 3.5% | 3%  | 3.5% | 3.5% | 3%  | 3.5% | 3%  | 3.5% |

Total: 50% | Target minimum score: 25%

---

## Daftar Tugas

### Tugas 1: Kalkulator Sederhana (7%)

Buat kalkulator dengan operasi dasar (+, -, \*, /).

- Tombol angka 0-9 dan operasi +, -, \*, /
- Display menampilkan operasi real-time
- Tombol = untuk menghitung hasil
- Tombol Clear untuk reset

Hint: Simpan `currentValue`, `operator`, dan `nextValue`. Gunakan `parseInt()` atau `parseFloat()`.

---

### Tugas 2: To-Do List dengan Add/Delete (7%)

Buat sistem to-do sederhana.

- Input untuk item baru
- Tombol "Tambah" untuk menambahkan item
- Setiap item punya tombol delete
- List ter-render setiap kali ada perubahan

**Hint:** Array untuk store items. Function `renderList()` untuk display.

---

### **Tugas 3: Search & Filter Data** (7%)

Filter data produk saat user mengetik di search box.

- Data: ['Laptop', 'Mouse', 'Keyboard', 'Monitor', 'Headset', 'Webcam']
- Display hasil yang match dengan input
- Case-insensitive search

**Hint:** `.includes()` atau `.filter()` + event `input` di search-input.

---

### **Tugas 4: Accordion Menu** (7%)

Multiple accordion items yang bisa buka/tutup.

- Buat 4 accordion items dengan header dan content
- Hanya satu yang bisa buka sekaligus
- Klik item lain otomatis tutup item sebelumnya

**Hint:** `classList.remove()` untuk semua, `classList.add()` untuk yang aktif.

---

### **Tugas 5: Counter dengan Custom Step** (6%)

Counter yang bisa set increment step custom.

- Input untuk "Step Value"
- Tombol +/- increment sesuai step value
- Tombol Reset untuk reset ke 0

**Hint:** Baca `value` dari `step-input`, gunakan dalam operasi counter.

---

### **Tugas 6: Form Validasi Advanced** (8%)

Validasi form dengan multiple rules, real-time feedback.

- **Username:** min 5 karakter
- **Email:** format email valid (gunakan regex atau simple check)
- **Password:** min 8 karakter, minimal 1 angka, minimal 1 huruf besar
- Tampilkan error/success message real-time
- Tombol submit hanya aktif jika semua valid

**Hint:** EventListener pada `input` event. Regex: `/^[A-Z].*\d/` untuk password pattern.

---

### **Tugas 7: Random Quote Generator** (7%)

Generate random quote dengan random color.

- Setiap klik tombol, tampilkan random quote
- Tampilkan quote text + author
- Background quote box random color setiap kali

**Hint:** Buat array quote objects. `Math.random()` untuk index. CSS `.style.backgroundColor`.

---

### **Tugas 8: Countdown Timer** (7%)

Timer yang bisa di-customize dan dikontrol.

- Input menit (default 1 menit)
- Tombol Start, Pause, Reset
- Display format MM:SS
- Auto-stop saat mencapai 00:00

**Hint:** `setInterval()` untuk decrement. `clearInterval()` untuk pause. Format dengan `String.padStart()`.

---

### **Tugas 9: Real-time Character Counter** (6%)

Counter karakter dengan progress bar.

- Max 100 karakter
- Display jumlah karakter current/max
- Progress bar visual
- Disable input saat sudah 100 char (optional)

**Hint:** `.length` dari textarea value. Progress bar: `(currentLength / 100) * 100 + '%'`.

---

### **Tugas 10: Color Picker dengan Info RGB/HEX** (7%)

Color picker yang tampilkan preview dan info.

- Input color picker
- Preview warna di color box
- Tampilkan HEX value
- Optional: Convert HEX ke RGB

**Hint:** Event `change` pada color input. HEX dari `value` color input langsung. RGB conversion: parse hex string.

---

### **Tugas 11: Image Brightness Control** (7%)

Control brightness dan grayscale dengan slider.

- Slider brightness (0-200%, default 100%)
- Slider grayscale (0-100%, default 0%)
- Real-time update image filter
- Display percentage value

**Hint:** CSS `filter` property. Syntax: `filter: brightness(1) grayscale(0)`. Update `.style.filter`.

---

### **Tugas 12: Dark Mode Toggle dengan LocalStorage** (6%)

Toggle dark mode dengan persistent storage.

- Button untuk toggle dark/light mode
- Apply dark styling ke page (background, text color)
- Save preference ke localStorage
- Load preference saat page refresh

**Hint:** `localStorage.setItem()` dan `getItem()`. Toggle class `dark-mode` pada body.

---

### **Tugas 13: Modal Popup dengan Close** (7%)

Modal yang bisa dibuka/ditutup dengan multiple ways.

- Button untuk buka modal
- Close dengan X button
- Close dengan close button
- Close saat klik di luar modal (background)
- Smooth show/hide

**Hint:** `modal.classList.toggle('show')`. Click outside: `event.target === modal`.

---

### **Tugas 14: Sort List of Numbers** (6%)

Parse dan sort array angka.

- User input angka dipisah koma (contoh: "5,1,9,3")
- Button sort ascending
- Button sort descending
- Display hasil sort di output box

**Hint:** `.split(',')`, `.map(Number)`, `.sort((a,b) => a-b)` atau `reverse()`.

---

### **Tugas 15: FAQ Accordion** (7%)

FAQ dengan accordion behavior otomatis.

- Buat 4-5 FAQ items (Q&A pairs)
- Header (pertanyaan) bisa diklik untuk expand/collapse
- Hanya satu item yang buka sekaligus
- Smooth open/close animation (optional)

**Hint:** Loop array FAQ, buat accordion header/content untuk setiap item. Management similar ke Tugas 4.

---

## Checklist Sebelum Submit

- [ ] Semua 15 tugas sudah berfungsi
- [ ] Test di browser dengan F12 console (no errors)
- [ ] Kode rapi dengan comments
- [ ] Jangan ubah HTML atau CSS
- [ ] Nilai minimal 25%

---

## Cara Submit

1. Edit file `index.html` - isi bagian `<script>`
2. Test semua tugas di browser
3. Rename index.html dengan: `Week20_[NamaKamu].html` (contoh: `Week20_JustinArland.html`)
4. Kirim file ke guru
5. Kirim dengan Nama Lengkap dan Kelas

---

## Referensi

| Kebutuhan       | Syntax                                 |
| --------------- | -------------------------------------- |
| Find element    | `document.getElementById('id')`        |
| Find all        | `document.querySelectorAll('.class')`  |
| Add class       | `element.classList.add('class')`       |
| Remove class    | `element.classList.remove('class')`    |
| Toggle class    | `element.classList.toggle('class')`    |
| Change style    | `element.style.color = 'red'`          |
| Get input value | `input.value`                          |
| Set text        | `element.textContent = 'text'`         |
| Add event       | `elem.addEventListener('click', func)` |
| Array sort      | `arr.sort((a,b) => a-b)`               |
| Array filter    | `arr.filter(x => x > 5)`               |
| Regex test      | `/pattern/.test(string)`               |
| Interval        | `setInterval(func, 1000)`              |
| Timeout         | `setTimeout(func, 1000)`               |
| LocalStorage    | `localStorage.setItem('key', value)`   |

---

Selamat mengerjakan! Semoga nilai Anda meningkat.
