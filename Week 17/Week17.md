# Week 17: JavaScript Dasar di HTML

---

## 1) Pemanasan: JavaScript itu apa?

- HTML = kerangka rumah
- CSS = cat dan dekorasi
- JavaScript = listrik yang bikin rumah jadi hidup

Contoh:

- Tombol Like yang menambah angka
- Pop up notifikasi
- Kalkulator
- Validasi form saat daftar akun

"Kalau HTML dan CSS itu diam, JavaScript membuat halaman bisa bereaksi saat kita klik, ketik, atau geser."

---

## 2) Menaruh JavaScript di HTML

Gunakan tag script di bagian bawah body.

Contoh sederhana:

```html
<!DOCTYPE html>
<html lang="id">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Belajar JavaScript</title>
  </head>
  <body>
    <h1>Halo, kelas 7-9!</h1>

    <script>
      alert("Selamat datang di kelas JavaScript!");
    </script>
  </body>
</html>
```

Penjelasan singkat:

- alert menampilkan kotak pesan
- script dibaca browser sebagai perintah JavaScript

---

## 3) Variabel, Input, dan Output

### A. Variabel

Variabel itu seperti kotak penyimpanan data.

```html
<script>
  let nama = "Budi";
  let umur = 13;

  console.log("Nama:", nama);
  console.log("Umur:", umur);
</script>
```

Catatan pengajar:

- let: nilai boleh berubah
- const: nilai tetap

### B. Input dan output ke halaman

Contoh yang langsung terlihat:

```html
<!DOCTYPE html>
<html lang="id">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Input Nama</title>
  </head>
  <body>
    <h2>Masukkan nama kamu</h2>
    <input id="namaInput" type="text" placeholder="Contoh: Raka" />
    <button onclick="sapa()">Sapa Saya</button>
    <p id="hasil"></p>

    <script>
      function sapa() {
        let nama = document.getElementById("namaInput").value;
        document.getElementById("hasil").textContent = "Halo, " + nama + "!";
      }
    </script>
  </body>
</html>
```

Konsep yang dikenalkan dari contoh ini:

- document.getElementById untuk mengambil elemen HTML
- .value untuk membaca isi input
- .textContent untuk mengubah tulisan

---

## 4) Event Dasar: Klik Tombol

Event adalah kejadian. Misalnya: klik, ketik, atau submit.

Contoh counter sederhana:

```html
<!DOCTYPE html>
<html lang="id">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Counter</title>
  </head>
  <body>
    <h2>Counter Sederhana</h2>
    <p id="angka">0</p>
    <button onclick="tambah()">Tambah +1</button>
    <button onclick="resetAngka()">Reset</button>

    <script>
      let nilai = 0;

      function tambah() {
        nilai = nilai + 1;
        document.getElementById("angka").textContent = nilai;
      }

      function resetAngka() {
        nilai = 0;
        document.getElementById("angka").textContent = nilai;
      }
    </script>
  </body>
</html>
```

---

## 5) Mini Proyek (10 menit): Cek Bilangan Genap/Ganjil

Tujuan mini proyek:

- Siswa membaca input angka
- Siswa memakai if else
- Siswa menampilkan hasil ke halaman

Contoh proyek:

```html
<!DOCTYPE html>
<html lang="id">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Cek Genap Ganjil</title>
  </head>
  <body>
    <h2>Cek Genap atau Ganjil</h2>
    <input id="angkaInput" type="number" placeholder="Masukkan angka" />
    <button onclick="cekAngka()">Cek</button>
    <p id="output"></p>

    <script>
      function cekAngka() {
        let angka = Number(document.getElementById("angkaInput").value);

        if (angka % 2 === 0) {
          document.getElementById("output").textContent =
            angka + " adalah bilangan genap";
        } else {
          document.getElementById("output").textContent =
            angka + " adalah bilangan ganjil";
        }
      }
    </script>
  </body>
</html>
```

Challenge cepat (opsional kalau waktu cukup):

- Tambahkan validasi jika input kosong
- Ubah warna hasil: hijau untuk genap, oranye untuk ganjil

---

## Tugas Rumah 1 (Ringan) Porsi Nilai 30%

Buat satu file HTML berjudul Tebak Cuaca:

Aturan:

1. Ada input teks (contoh: panas, hujan, mendung)
2. Ada tombol Cek
3. JavaScript menampilkan saran:
   - panas -> jangan lupa minum air
   - hujan -> bawa payung
   - mendung -> siap-siap jas hujan
4. Jika kata tidak dikenal, tampilkan: cuaca belum dikenali
5. dan Pastikan sudah di Styling dan enak dimata, tidak terlalu kompleks juga gapapa

Tujuan tugas: melatih input, if else, dan output.

Deadline Rabu, 1 April 2026. Jam 20.00 Malam.

---

## Tugas Rumah 2 (Susah) Porsi Nilai 70%

Buat satu file HTML berjudul TokoOnline:

Aturan:

1. Ada list item Produk (contoh: Xiaomi, Oppo, Samsung, Iphone)
2. Setiap item Produk terdapat Nama Produk, Deskripsi Produk, Harga, Stok
3. Javascript:
   - Tambah Produk ke Keranjang
   - Tambah/Kurang kuantitas setiap produk
   - Menampilkan Total Harga, Total Jumlah Produk
   - Menghapus Item dalam Keranjang

Tujuan tugas: melatih penggunaan fungsi untuk operasi tambah, kurang, kali dalam study Case TokoOnline.

Deadline Rabu 1 April 2026. Jam 20.00 Malam.
