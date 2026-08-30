# Week 19: Tes JavaScript Dasar - JavaScript Internal dalam HTML

## Tujuan Pembelajaran

Pada minggu ini, murid-murid akan menguji pemahaman mereka tentang:

- Cara menulis JavaScript internal (di dalam tag `<script>`)
- Manipulasi DOM (Document Object Model)
- Event listeners dan event handling
- Interaksi dasar dengan pengguna
- Validasi form sederhana

---

## Petunjuk Umum

1. **Buka file `index.html`** di browser Anda (bisa dengan membuka langsung atau menggunakan Live Server)
2. **Baca setiap tugas** dengan cermat
3. **Implementasikan JavaScript** untuk setiap tugas di section `<script>` di bagian akhir file HTML
4. **Test setiap fitur** untuk memastikan bekerja dengan baik
5. **Jangan mengubah HTML atau CSS**, hanya tambahkan JavaScript
6. **Gunakan `console.log()`** untuk debug jika diperlukan (buka DevTools dengan F12)

---

## Daftar Tugas

### ✅ Tugas 1: Tombol Pesan Sederhana

**Level: Mudah**

Klik tombol dengan ID `btn-hello` untuk menampilkan pesan menggunakan `alert()`.

**Petunjuk:**

```javascript
// Targetkan tombol dengan ID "btn-hello"
// Gunakan addEventListener untuk mendengarkan event "click"
// Gunakan alert() untuk menampilkan pesan

const btn = document.getElementById("btn-hello");
btn.addEventListener("click", function () {
  // Tulis kode Anda di sini
});
```

**Hasil yang diharapkan:** Saat tombol diklik, muncul popup alert dengan pesan apapun.

---

### ✅ Tugas 2: Penghitung (Counter)

**Level: Mudah-Menengah**

Buat sistem penghitung yang:

- Tombol `+` (ID: `btn-increase`) menambah angka di display (ID: `counter-display`)
- Tombol `-` (ID: `btn-decrease`) mengurangi angka di display
- Display menampilkan nilai saat ini

**Petunjuk:**

```javascript
let count = 0;

// Targetkan elemen yang diperlukan
const increaseBtn = document.getElementById("btn-increase");
const decreaseBtn = document.getElementById("btn-decrease");
const counterDisplay = document.getElementById("counter-display");

// Tambahkan event listener untuk tombol +
increaseBtn.addEventListener("click", function () {
  // Tambah count
  // Update counterDisplay.textContent
});

// Tambahkan event listener untuk tombol -
decreaseBtn.addEventListener("click", function () {
  // Kurangi count
  // Update counterDisplay.textContent
});
```

**Hasil yang diharapkan:**

- Angka di display mulai dari 0
- Klik + menjadi 1, 2, 3, dst
- Klik - menjadi -1, -2, -3, dst

---

### ✅ Tugas 3: Toggle Warna Latar

**Level: Mudah**

Buat tombol yang mengubah warna latar belakang dari `color-box` (ID: `color-box`) dengan warna yang berbeda setiap kali diklik.

**Petunjuk:**

```javascript
const colorBox = document.getElementById("color-box");
const toggleColorBtn = document.getElementById("btn-toggle-color");

const colors = [
  "#FF6B6B",
  "#4ECDC4",
  "#45B7D1",
  "#FFA07A",
  "#98D8C8",
  "#F7DC6F",
];
let currentColorIndex = 0;

toggleColorBtn.addEventListener("click", function () {
  // Update warna box
  // Bisa menggunakan array colors
});
```

**Hasil yang diharapkan:** Setiap kali tombol diklik, warna kotak berubah.

---

### ✅ Tugas 4: Validasi Form Sederhana

**Level: Menengah**

Validasi form saat tombol "Kirim" (ID: `btn-submit`) diklik:

- Cek apakah input "Nama" (ID: `nama`) kosong → tampilkan error di `error-nama`
- Cek apakah input "Email" (ID: `email`) kosong → tampilkan error di `error-email`
- Jika semua terisi, tampilkan alert "Form berhasil dikirim!"

**Petunjuk:**

```javascript
const form = document.getElementById("form-validation");
const namaInput = document.getElementById("nama");
const emailInput = document.getElementById("email");
const namaError = document.getElementById("error-nama");
const emailError = document.getElementById("error-email");
const submitBtn = document.getElementById("btn-submit");

submitBtn.addEventListener("click", function () {
  // Reset error messages
  namaError.textContent = "";
  emailError.textContent = "";

  let valid = true;

  // Validasi nama
  if (namaInput.value.trim() === "") {
    // Tampilkan error
    valid = false;
  }

  // Validasi email
  if (emailInput.value.trim() === "") {
    // Tampilkan error
    valid = false;
  }

  // Jika valid
  if (valid) {
    // Tampilkan alert sukses
  }
});
```

**Hasil yang diharapkan:**

- Jika klik submit tanpa input, tampil pesan error di bawah input
- Jika kedua input terisi, tampil alert sukses

---

### ✅ Tugas 5: Tampil/Sembunyikan Konten

**Level: Mudah**

Buat tombol (ID: `btn-toggle-content`) yang menampilkan atau menyembunyikan konten (ID: `hidden-content-box`):

- Saat diklik pertama kali: konten ditampilkan dan tombol text berubah menjadi "Sembunyikan Konten"
- Saat diklik lagi: konten disembunyikan dan tombol kembali menjadi "Tampilkan Konten"

**Petunjuk:**

```javascript
const toggleBtn = document.getElementById("btn-toggle-content");
const hiddenContent = document.getElementById("hidden-content-box");

toggleBtn.addEventListener("click", function () {
  // Toggle class 'show' pada hidden-content
  // Atau gunakan hiddenContent.style.display

  // Ubah text tombol
  if (hiddenContent.classList.contains("show")) {
    toggleBtn.textContent = "Sembunyikan Konten";
  } else {
    toggleBtn.textContent = "Tampilkan Konten";
  }
});
```

**Hasil yang diharapkan:** Konten muncul dan hilang saat tombol diklik bergantian.

---

### ✅ Tugas 6: Ubah Teks Dinamis

**Level: Mudah**

Setiap kali tombol (ID: `btn-change-text`) diklik, ubah teks di elemen (ID: `dynamic-text`) dengan berbagai teks yang berbeda.

**Petunjuk:**

```javascript
const changeTextBtn = document.getElementById("btn-change-text");
const dynamicText = document.getElementById("dynamic-text");

const texts = [
  "Teks original - klik tombol untuk mengubah",
  "Teks berubah pertama!",
  "Teks berubah kedua!",
  "Teks berubah ketiga!",
  "Kembali ke awal...",
];

let textIndex = 0;

changeTextBtn.addEventListener("click", function () {
  // Update textIndex
  // Jika sudah sampai akhir array, reset ke 0
  // Update dynamic-text content
});
```

**Hasil yang diharapkan:** Teks berubah setiap kali tombol diklik (cycling through array).

---

### ✅ Tugas 7: Input dan Tampilkan Teks

**Level: Menengah**

Buat sistem input yang:

- User mengetik teks di input (ID: `user-input`)
- Klik tombol (ID: `btn-display-input`)
- Teks dari input ditampilkan di element (ID: `user-output`)

**Petunjuk:**

```javascript
const userInput = document.getElementById("user-input");
const displayBtn = document.getElementById("btn-display-input");
const userOutput = document.getElementById("user-output");

displayBtn.addEventListener("click", function () {
  // Ambil value dari userInput
  // Tampilkan di userOutput menggunakan textContent
});

// BONUS: Buat input otomatis update saat user tekan Enter
userInput.addEventListener("keypress", function (event) {
  if (event.key === "Enter") {
    // Trigger display button click
  }
});
```

**Hasil yang diharapkan:**

- User mengetik "Halo dunia" di input
- Klik tombol → "Halo dunia" muncul di output area
- BONUS: Bisa tekan Enter untuk langsung menampilkan tanpa klik tombol

---

## Kriteria Penilaian

| Tugas                | Poin    | Kriteria                                    |
| -------------------- | ------- | ------------------------------------------- |
| 1. Tombol Pesan      | 10      | Alert muncul saat tombol diklik             |
| 2. Counter           | 15      | Counter berjalan dengan benar + dan -       |
| 3. Toggle Warna      | 10      | Warna berubah saat tombol diklik            |
| 4. Validasi Form     | 15      | Validasi bekerja, error muncul dengan benar |
| 5. Toggle Konten     | 15      | Konten muncul/hilang, text tombol berubah   |
| 6. Ubah Teks         | 10      | Teks cycling dengan benar                   |
| 7. Input & Tampilkan | 15      | Input ditampilkan dengan benar              |
| **TOTAL**            | **100** |                                             |

---

## Tips & Trik

### Selector JavaScript yang Berguna

```javascript
// Memilih elemen berdasarkan ID
const element = document.getElementById("id-name");

// Memilih elemen berdasarkan class atau tag
const element = document.querySelector(".class-name");
const element = document.querySelector("tag-name");

// Memilih multiple elemen
const elements = document.querySelectorAll(".class-name");

// Mengubah teks
element.textContent = "Teks baru";
element.innerHTML = "<p>HTML baru</p>";

// Mengubah class
element.classList.add("class-name");
element.classList.remove("class-name");
element.classList.toggle("class-name");

// Mengubah style
element.style.backgroundColor = "red";
element.style.display = "none";
```

### Event Listeners yang Berguna

```javascript
// Click event
element.addEventListener('click', function() { ... });

// Input/Change event
input.addEventListener('input', function() { ... });
input.addEventListener('change', function() { ... });

// Keyboard event
element.addEventListener('keypress', function(event) {
    if (event.key === 'Enter') { ... }
});

// Submit event
form.addEventListener('submit', function(event) {
    event.preventDefault(); // Cegah reload halaman
});
```

### Debugging

1. **Buka DevTools:** Tekan `F12` di browser
2. **Console Tab:** Gunakan `console.log()` untuk lihat nilai variabel
3. **Elements Tab:** Lihat struktur HTML dan CSS
4. **Sources Tab:** Debug code step-by-step

---

## Bonus Challenge (Opsional)

Jika sudah selesai semua tugas, coba:

1. **Styling dinamis:** Ubah style elemen dengan JavaScript, bukan hanya textContent
2. **Multiple color cycles:** Buat counter untuk cycle warna
3. **Form cleanup:** Hapus isi input setelah form dikirim
4. **Local storage:** Simpan counter value agar tidak reset saat refresh
5. **Animation:** Tambahkan animasi smooth transition

---

## Bagaimana Cara Submit

1. Edit file **index.html** - tambahkan JavaScript di section `<script>`
2. Test setiap tugas di browser
3. Pastikan semua berjalan dengan baik
4. Zip folder Week 19 atau push ke git repo
5. Kirim link atau file ke guru

---

## Reminder Penting ❗

- **JANGAN ubah HTML atau CSS** - hanya focus pada JavaScript
- **Gunakan ID yang benar** - pastikan match dengan elemen HTML
- **Test setiap fitur** - jangan submit tanpa test
- **Gunakan meaningful variable names** - jangan pakai `x`, `y`, `z`
- **Tambahkan comments** - jelaskan apa yang kode Anda lakukan

---

## Referensi

- [MDN: DOM Manipulation](https://developer.mozilla.org/en-US/docs/Learn/JavaScript/Client-side_web_APIs/Manipulating_documents)
- [MDN: Events](https://developer.mozilla.org/en-US/docs/Learn/JavaScript/Building_blocks/Events)
- [MDN: getElementById](https://developer.mozilla.org/en-US/docs/Web/API/Document/getElementById)
- [MDN: addEventListener](https://developer.mozilla.org/en-US/docs/Web/API/EventTarget/addEventListener)

---

**Selamat mengerjakan! 💪**
