# Week 23 - Soal Tugas JavaScript (15 Nomor)

**TUGAS DIKERJAKAN DI KELAS (Bukan Pekerjaan Rumah)**

Tugas ini harus dikerjakan langsung di kelas minggu ini untuk latihan konsep JavaScript yang sudah dipelajari di Week 22.

**Instruksi:**

- Buat 1 file HTML dengan nama `tugas-javascript-{nama}.html`
- Kerjakan semua 15 nomor dalam satu file
- Pastikan semua berjalan tanpa error
- Tulis nama dan kelas di bagian atas halaman

---

## Template HTML & CSS

Gunakan template ini sebagai struktur dasar:

```html
<!DOCTYPE html>
<html lang="id">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Tugas Week 23 - JavaScript</title>
    <style>
      * {
        margin: 0;
        padding: 0;
        box-sizing: border-box;
      }

      body {
        font-family: "Arial", sans-serif;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        min-height: 100vh;
        padding: 20px;
      }

      .container {
        max-width: 1000px;
        margin: 0 auto;
        background: white;
        border-radius: 10px;
        box-shadow: 0 10px 30px rgba(0, 0, 0, 0.3);
        padding: 30px;
      }

      .header {
        text-align: center;
        margin-bottom: 30px;
        border-bottom: 3px solid #667eea;
        padding-bottom: 20px;
      }

      .header h1 {
        color: #333;
        font-size: 28px;
        margin-bottom: 5px;
      }

      .header p {
        color: #666;
        font-size: 14px;
      }

      .task-section {
        margin-bottom: 30px;
        padding: 20px;
        border: 1px solid #ddd;
        border-radius: 8px;
        background: #f9f9f9;
      }

      .task-section h3 {
        color: #667eea;
        margin-bottom: 15px;
        font-size: 18px;
      }

      input,
      button,
      select,
      textarea {
        padding: 10px;
        margin: 5px 5px 5px 0;
        border: 1px solid #ddd;
        border-radius: 5px;
        font-size: 14px;
      }

      input:focus,
      button:focus,
      textarea:focus {
        outline: none;
        border-color: #667eea;
        box-shadow: 0 0 5px rgba(102, 126, 234, 0.3);
      }

      button {
        background-color: #667eea;
        color: white;
        cursor: pointer;
        border: none;
        transition: background 0.3s;
      }

      button:hover {
        background-color: #764ba2;
      }

      .output {
        margin-top: 10px;
        padding: 10px;
        background: white;
        border-left: 4px solid #667eea;
        border-radius: 3px;
        font-size: 14px;
        color: #333;
      }

      .list-item {
        padding: 8px 12px;
        background: #f0f0f0;
        margin: 5px 0;
        border-radius: 5px;
        display: flex;
        justify-content: space-between;
        align-items: center;
      }

      .list-item button {
        padding: 5px 10px;
        margin: 0;
        font-size: 12px;
      }

      .footer {
        text-align: center;
        margin-top: 30px;
        padding-top: 20px;
        border-top: 1px solid #ddd;
        color: #666;
        font-size: 12px;
      }
    </style>
  </head>
  <body>
    <div class="container">
      <div class="header">
        <h1>Tugas JavaScript Week 23</h1>
        <p>
          Nama: <span id="namaHeader">-</span> | Kelas:
          <span id="kelasHeader">-</span>
        </p>
      </div>

      <!-- Nomor 1 -->
      <div class="task-section" id="nomor1">
        <h3>Nomor 1 - Variabel</h3>
        <!-- Isi nomor 1 -->
      </div>

      <!-- Nomor 2 sampai 15 -->
      <!-- ... -->

      <div class="footer">
        <p>Semoga sukses! Jangan lupa test setiap nomor. 💪</p>
      </div>
    </div>

    <script>
      // Letakkan semua JavaScript di sini
      // Mulai dari nomor 1, 2, 3, ... sampai 15
    </script>
  </body>
</html>
```

---

---

## Nomor 1 - Variabel

Buat program yang:

- Buat variabel nama, umur, dan kelas
- Isi dengan data diri kamu
- Tampilkan di halaman: "Nama saya [nama], umur [umur] tahun, kelas [kelas]"

**Contoh output:**

```
Nama saya Budi, umur 14 tahun, kelas 7A
```

**Tips untuk Nomor 1:**

- Gunakan `let` untuk buat variabel: `let nama = "Budi";`
- Gunakan template literal untuk tampilkan: `` `Nama saya ${nama}, umur ${umur} tahun, kelas ${kelas}` ``

---

## Nomor 2 - Kalkulator Sederhana

Buat kalkulator dengan:

- Dua input angka
- Tombol + - \* /
- Tampilkan hasil di halaman

**Contoh:** 10 + 5 = 15
**Tips untuk Nomor 2:**

- Ambil value input: `parseInt(inputAngka1.value)`
- Gunakan if-else atau switch untuk tentukan operator mana yang diklik
- Hitung hasilnya dan tampilkan di halaman

---

## Nomor 3 - Cek Nilai Rapor

Buat program yang:

- Input nilai (0-100)
- Jika >= 80: "Sangat Baik"
- Jika 70-79: "Baik"
- Jika < 70: "Perlu diperbaiki"
- Tampilkan hasil

**Tips untuk Nomor 3:**

- Ambil input dan konversi: `let nilai = parseInt(inputNilai.value);`
- Gunakan if-else untuk cek kondisi
- Tampilkan hasil di halaman

---

## Nomor 4 - Manipulasi Teks

Buat program yang:

- User input teks apa saja
- Tampilkan:
  - Teks dalam huruf besar
  - Teks dalam huruf kecil
  - Jumlah karakter

**Tips untuk Nomor 4:**

- Ambil input: `let teks = inputTeks.value;`
- Huruf besar: `teks.toUpperCase();`
- Huruf kecil: `teks.toLowerCase();`
- Jumlah karakter: `teks.length`

---

## Nomor 5 - Array Daftar Barang

Buat "Daftar Belanja" dengan:

- Array berisi 4 barang awal
- Tombol "Tambah Barang"
- Tampilkan list belanja
- Tampilkan jumlah barang

**Tips untuk Nomor 5:**

- Buat array: `let barang = ["Apel", "Mangga", "Jeruk", "Telur"];`
- Gunakan `push()` untuk tambah barang baru: `barang.push(inputValue);`
- Display list dengan loop for...of: `for (let item of barang) { ... }`
- Tampilkan jumlah: `barang.length`

---

## Nomor 6 - Loop Menampilkan Angka

Buat program yang tampilkan:

- Angka 1 sampai 10 menggunakan loop for
- Hasilnya: 1, 2, 3, ..., 10
- Tampilkan dalam bentuk list di halaman

**Tips untuk Nomor 6:**

- Gunakan loop for: `for (let i = 1; i <= 10; i++) { ... }`
- Tampilkan setiap angka di halaman (bukan cuma console.log)
- Bisa pakai `document.innerHTML +=` atau append ke HTML

---

## Nomor 7 - Ubah Angka Dengan Map

Buat program yang:

- Ada array: [1, 2, 3, 4, 5]
- Gunakan map() untuk gandakan semua angka
- Hasil: [2, 4, 6, 8, 10]
- Tampilkan hasil di halaman

**Tips untuk Nomor 7:**

- Gunakan map dengan arrow function: `let hasilMap = angka.map(n => n * 2);`
- Tampilkan hasilnya: `hasilMap` adalah array baru dengan nilai yang digandakan

---

## Nomor 8 - Profil Diri

Buat "Kartu Profil" dengan object yang berisi:

- nama
- kelas
- hobi

Tampilkan dalam format rapi di halaman.

**Tips untuk Nomor 8:**

- Buat object: `let profil = { nama: "Budi", kelas: "7A", hobi: "gaming" };`
- Akses property: `profil.nama` atau `profil["nama"]`
- Tampilkan dengan template literal: `` `Nama: ${profil.nama} ... ` ``

---

## Nomor 9 - Function Hitung Luas

Buat function yang:

- `hitungLuas(panjang, lebar)` - buat persegi panjang
- Input panjang dan lebar dari user
- Tampilkan luasnya

**Tips untuk Nomor 9:**

- Buat function: `function hitungLuas(p, l) { return p * l; }`
- Ambil input dengan `.value` dan konversi dengan `parseInt`
- Panggil function dan tampilkan hasilnya di halaman

---

## Nomor 10 - Tombol Ubah Warna

Buat program dengan:

- Ada div/kotak di halaman
- Ada tombol "Ubah Warna"
- Setiap diklik tombol, warna kotak berubah
- (Boleh warna tetap atau random)

**Tips untuk Nomor 10:**

- Ubah warna: `element.style.backgroundColor = "blue";`
- Untuk random warna, bisa pakai array warna: `let warna = ["red", "blue", "green"];`
- Atau pakai random hex: `element.style.backgroundColor = "#" + Math.floor(Math.random()*16777215).toString(16);`

---

## Nomor 11 - Form Validasi

Buat form dengan:

- Input nama dan email
- Tombol submit
- Saat submit, cek apakah semua terisi
- Kalau kosong: tampilkan "Harus diisi semua!"
- Kalau lengkap: tampilkan "Terima kasih [nama]!"

**Tips:**

- Jangan lupa `e.preventDefault()` saat handle submit
- Gunakan kondisi `if` untuk cek apakah input kosong: `if (nama === "" || email === "")`
- Gunakan template literal untuk tampilkan pesan: `` `Terima kasih ${nama}!` ``

---

## Nomor 12 - Todo List Sederhana

Buat aplikasi todo dengan:

- Input untuk task baru
- Tombol "Tambah"
- Tampilkan list task
- Tiap task ada tombol "Hapus"
- Tampilkan jumlah task

**Tips untuk Nomor 12:**

- Gunakan array untuk simpan task: `let tasks = [];`
- Gunakan `push()` untuk tambah task baru
- Gunakan `splice(index, 1)` untuk hapus task yang diklik
- Display ulang list setiap kali ada perubahan (tambah/hapus)

---

## Nomor 13 - Loop For...Of

Buat program yang:

- Ada array nama siswa minimal 5 orang
- Tampilkan semua nama menggunakan loop for...of
- Format: "1. Budi", "2. Ani", "3. Citra"
- Tampilkan di halaman dalam bentuk list bernomor

**Tips untuk Nomor 13:**

- Buat array: `let siswa = ["Budi", "Ani", "Citra", "Doni", "Eka"];`
- Gunakan for...of: `for (let nama of siswa) { ... }`
- Gunakan counter untuk nomor urut

---

## Nomor 14 - Do-While Loop

Buat program yang:

- Ada input angka
- Tombol "Hitung"
- Jika angka >= 0, tampilkan: "Angka valid!"
- Gunakan do-while untuk minimal jalankan sekali

**Tips untuk Nomor 14:**

- Do-while pasti jalan minimal sekali: `do { ... } while (kondisi)`
- Cocok untuk validasi yang perlu jalan dulu sebelum cek kondisi
- Tampilkan hasil di halaman

---

## Nomor 15 - setTimeout & classList Toggle

Buat program yang:

- Ada tombol "Klik Saya"
- Saat diklik, tombol berubah warna jadi hijau
- Tombol kembali ke warna normal setelah 2 detik
- Gunakan setTimeout dan classList

**Tips untuk Nomor 15:**

- Gunakan addEventListener untuk handle klik
- Gunakan classList.toggle() untuk ubah class
- Gunakan setTimeout untuk kembali ke warna normal: `setTimeout(() => { ... }, 2000)`
- CSS class untuk warna: `.aktif { background-color: green; color: white; }`

---

## Catatan Penting

✓ Setiap nomor harus punya:

- Input dari user (kalo perlu)
- Tombol atau yang bisa diklik
- Output tampil di halaman (bukan cuma di console)

✓ Tips mengerjakan:

- Kerjakan nomor per nomor
- Test setiap nomor sebelum lanjut
- Buka console (F12) kalau ada error
- Jangan copy-paste dari teman - pahami caranya sendiri

**Tips Penting dari Week 22:**

1. **Input .value** (Nomor 2, 3, 4, 9, 11, 12, 14) - Ambil data user: `inputAngka.value`
2. **parseInt** (Nomor 2, 3, 9, 14) - Ubah teks jadi angka: `parseInt(inputAngka.value)`
3. **event.preventDefault()** (Nomor 11) - Cegah form refresh otomatis
4. **splice** (Nomor 12) - Hapus item array: `array.splice(index, 1)`
5. **Template literals** (Semua nomor) - String rapi: `` `Teks ${variabel}` ``
6. **backgroundColor** (Nomor 10, 15) - Ubah warna: `element.style.backgroundColor = "red"`
7. **let vs const** - `let` = data berubah, `const` = data tetap
8. **for...of loop** (Nomor 5, 12, 13) - Loop array simpel: `for (let item of array) { ... }`
9. **setTimeout** (Nomor 15) - Jalankan kode sekali: `setTimeout(() => { ... }, 2000)`
10. **Do-While loop** (Nomor 14) - Jalankan minimal sekali: `do { ... } while (kondisi)`
11. **classList.toggle** (Nomor 15) - Toggle class: `element.classList.toggle("aktif")`
12. **Conditional** (Nomor 3, 11, 14) - If-else untuk logika: `if (kondisi) { ... } else { ... }`

---

## Penilaian

| Nomor     | Bobot        |
| --------- | ------------ |
| 1-5       | 6% per nomor |
| 6-10      | 7% per nomor |
| 11-15     | 7% per nomor |
| **Total** | **100%**     |

---

## Catatan Pengumpulan

- File dikumpulkan **di akhir jam pelajaran** 
- **Tidak ada pengumpulan setelah jam pelajaran selesai** (Tugas dikerjakan hanya di kelas)

---

Selamat mengerjakan! Ingat - tujuannya adalah paham, bukan hanya dapat nilai.
