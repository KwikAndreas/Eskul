# Review Week 23 - Evaluasi Hasil Siswa

Berikut pembahasan singkat hasil kerjaan Week 23. **Penilaian HANYA fokus pada fungsi JavaScript (15 nomor)**. HTML struktur dan CSS dari template tidak dinilai karena sudah disediakan sebagai template yang sama untuk semua.

## Rekap Nilai (JavaScript - 15 Nomor)

| Nama        | Nilai | Keterangan |
| ----------- | ----- | ---------- |
| Hans        | 45    | 3-4 nomor berjalan, banyak error JS, logic incomplete |
| Jonathan    | 15    | Syntax error parah, hampir tidak ada JS yang jalan |
| Lemuel      | 15    | Hanya nomor 1 coba, syntax error, 14 nomor kosong |
| Raphael     | 0     | File kosong, tidak ada submit |
| WW          | 0     | File kosong, tidak ada submit |

---

## Hans

**Yang sudah oke (JavaScript)**

- Nomor 1: Coba implementasi dengan `parseInt()`, sudah mengarah benar (walaupun masih error).
- Ada usaha untuk memahami DOM manipulation dengan `document.getElementById()`.

**Catatan perbaikan (JavaScript)**

- Nomor 1-3: Variabel tidak diinisialisasi dengan benar.
  - `let nilai = parseInt("inputNilai.value");` → Seharusnya ambil dari element dulu: `parseInt(document.getElementById('inputNilai').value)`
  - Tidak menampilkan hasil ke halaman (missing `document.getElementById().textContent = ...`).

- Nomor 4 (Manipulasi Teks): Placeholder ada tapi JS kosong.

- Nomor 5 (Array Daftar Barang): Button ada tapi event listener tidak ada.

- Nomor 6-15: Kosong atau hanya placeholder.

- JavaScript error:
  ```js
  const  document.getElementById.style.backgroundColor = "blue"
  // ❌ Syntax error - const statement salah, tidak assign variable
  ```
  - Seharusnya: `document.getElementById('elementId').style.backgroundColor = "blue"`

**Saran perbaikan**

- Selesaikan nomor 1-3 terlebih dahulu (variabel, kalkulator, cek nilai).
- Pastikan setiap nomor ada event listener (onClick, onChange, dll).
- Untuk menampilkan hasil, gunakan `document.getElementById().textContent` atau `.innerHTML`.
- Test di console browser untuk lihat error mana dulu yang muncul.

---

## Jonathan

**Yang sudah oke (JavaScript)**

- Coba menulis variabel pada nomor 1, ada usaha untuk belajar syntax.

**Catatan perbaikan (JavaScript)**

- Syntax error di banyak tempat yang membuat script tidak berjalan sama sekali:
  
  ```js
  const(PI);           // ❌ Error: const butuh assignment
  const{"3.14"};       // ❌ Error: syntax tidak valid
  Let name= "boni";    // ❌ Error: `Let` (capital), seharusnya `let`
  ```

- Variabel dideklarasikan dua kali tanpa perubahan makna:
  ```js
  let angka= "50";
  let angka= "69";     // ❌ Redeclaration error
  ```

- `console.log("name")` menampilkan string `"name"`, bukan value variabel.
  - Seharusnya: `console.log(name)` (tanpa quotes).

- Nomor 2-15: Kosong, tidak ada JavaScript sama sekali.

**Saran perbaikan**

- Mulai ulang dari template kosong yang rapi.
- Fokus nomor 1 dulu: pastikan variabel bisa di-assign dan di-display.
- Pahami perbedaan:
  - `console.log(variabel)` → tampilkan value
  - `console.log("variabel")` → tampilkan text `variabel`
- Jangan capitalize `let`, `const`, `var`.
- Setiap const harus ada assignment: `const PI = 3.14;`

---

## Lemuel

**Yang sudah oke (JavaScript)**

- Nomor 1: Menulis variabel nama, kelas, dan umur di JavaScript (walaupun ada error).
- Template string sudah coba gunakan (walaupun incomplete).

**Catatan perbaikan (JavaScript)**

- Nomor 1 (Variabel) syntax error:
  ```js
  let nama = lemuel     // ❌ `lemuel` tanpa quotes, seharusnya "lemuel"
  let kelas = 7         // ✓ OK
  let umur = 13         // ✓ OK
  ```

- Template string tidak ditampilkan ke halaman:
  ```js
  `Nama saya ${nama}, umur ${umur} tahun, kelas ${kelas}`
  ```
  - Ini hanya kode, tidak ditampilkan ke halaman. Seharusnya:
    ```js
    let hasil = `Nama saya ${nama}, umur ${umur} tahun, kelas ${kelas}`;
    document.getElementById('output').textContent = hasil;
    ```

- Nomor 2-15: Kosong (hanya ada comment placeholder), tidak ada JavaScript.

**Saran perbaikan**

- String harus dalam quotes: `"lemuel"` bukan `lemuel`.
- Setiap kode harus ditampilkan ke halaman dengan `document.getElementById().textContent` atau `.innerHTML`.
- Lanjutkan ke nomor 2 setelah nomor 1 benar-benar jalan.
- Buat satu nomor selesai dengan benar, baru lanjut ke nomor berikutnya.

---

## Raphael

**Status:** File kosong, tidak ada JavaScript sama sekali.

**Saran perbaikan**

- Download template dari Week23.md.
- Mulai dengan nomor 1, test sampai OK, baru lanjut ke nomor 2.
- Pastikan semua 15 nomor ada JavaScript yang berjalan.

---

## WW

**Status:** File kosong, tidak ada JavaScript sama sekali.

**Saran perbaikan**

- Download template dari Week23.md.
- Mulai dengan nomor 1, test sampai OK, baru lanjut ke nomor 2.
- Jangan takut dengan error di console, itu normal saat belajar.

---