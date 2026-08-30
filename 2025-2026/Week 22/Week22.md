# Week 22 - Belajar JavaScript

Bayangkan saja: HTML itu struktur rumah, CSS itu dekorasi/cat rumahnya, nah JavaScript itu yang bikin lampu bisa dinyalakan, pintu bisa dibuka, dan segala macam aksinya.

---

## 1. Variabel - Tempat Menyimpan Data

Variabel itu seperti kotak untuk menyimpan barang. Kita beri nama kotak itu, terus masukkan data ke dalamnya.

Ada 2 cara utama membuat variabel:

### Menggunakan `let` (Bisa Diubah)

```javascript
let nama = "Justin"; // Bisa diubah nilainya
let umur = 13;
let sukses = true;

// Nanti bisa diubah:
nama = "Jonathan"; // OK, berhasil diubah
umur = 14; // OK, berhasil diubah
```

**Gunakan `let` kalau data akan berubah-ubah** (misalnya nilai input user, counter yang bertambah, dll).

### Menggunakan `const` (Tidak Bisa Diubah)

```javascript
const PI = 3.14; // Tidak boleh diubah
const NAMA_SEKOLAH = "SMPK Anugerah";
const JARAK_KE_BULAN = 384400;

// Ini akan ERROR:
PI = 3.15; // ERROR! Tidak boleh diubah konstanta
```

**Gunakan `const` kalau data tidak akan pernah berubah** (seperti konstanta matematika, nama sekolah yang tetap, dll).

### Ringkasan:

- **`let`** = variabel yang **bisa berubah** → gunakan saat menyimpan data dinamis (input user, counter, dll)
- **`const`** = variabel yang **tidak boleh berubah** → gunakan saat menyimpan data tetap (konstanta, nilai awal array/object)

Dalam kode kita, sering pakai `let` karena banyak data yang berubah-ubah.

---

## 2. Tipe Data

Ada beberapa jenis data yang bisa disimpan:

```javascript
let nama = "Hans"; // Teks (String) - pakai tanda kutip
let umur = 15; // Angka (Number) - tanpa tanda kutip
let lulus = true; // Benar/Salah (Boolean) - hanya true atau false
```

---

## 3. Matematika Dasar

JavaScript bisa hitung seperti kalkulator:

```javascript
let a = 10;
let b = 3;

console.log(a + b); // 13
console.log(a - b); // 7
console.log(a * b); // 30
console.log(a / b); // 3.33...
console.log(a % b); // 1 (sisa pembagian)
```

---

## 4. Membandingkan Nilai

Kita bisa bandingkan dua nilai:

```javascript
console.log(10 === 10); // true (sama)
console.log(10 !== 5); // true (tidak sama)
console.log(10 > 5); // true (lebih besar)
console.log(10 < 5); // false (lebih kecil)
console.log(10 >= 10); // true (lebih besar sama dengan)
```

Hasil perbandingan selalu **true** (benar) atau **false** (salah).

---

## 5. Logika Sederhana

Cara menggabung kondisi:

```javascript
let tua = true;
let pintar = false;

console.log(tua && pintar); // false (DAN - harus dua-duanya true)
console.log(tua || pintar); // true (ATAU - cukup salah satu true)
console.log(!tua); // false (BUKAN - balik nilai)
```

- **&&** (DAN): kedua-duanya harus benar
- **||** (ATAU): salah satu saja boleh benar
- **!** (TIDAK): balik nilai

---

## 6. Keputusan dengan If-Else

Program bisa membuat keputusan:

```javascript
let nilai = 85;

if (nilai >= 80) {
  console.log("Bagus!");
} else if (nilai >= 70) {
  console.log("Cukup");
} else {
  console.log("Harus belajar lagi");
}
```

Program ini cek nilai. Kalau >= 80 print "Bagus!", kalau 70-79 print "Cukup", sisanya print "Harus belajar lagi".

---

## 7. Keputusan Singkat - Ternary

Ada cara lebih singkat untuk if-else:

```javascript
let nilai = 75;
let status = nilai >= 70 ? "Lulus" : "Tidak Lulus";
console.log(status); // "Lulus"
```

Format: `kondisi ? kalau_benar : kalau_salah`

---

## 8. Switch - Pilihan Banyak

Ketika ada banyak pilihan:

```javascript
let hari = 1;

switch (hari) {
  case 1:
    console.log("Senin");
    break;
  case 2:
    console.log("Selasa");
    break;
  case 3:
    console.log("Rabu");
    break;
  default:
    console.log("Hari lain");
}
```

---

## 9. Loop - Ulang Dengan For

Kadang kita perlu ulang sesuatu berkali-kali:

```javascript
for (let i = 0; i < 5; i++) {
  console.log("Ke-" + i);
}

// Output: Ke-0, Ke-1, Ke-2, Ke-3, Ke-4
```

**Penjelasan:**

- `let i = 0` - mulai dari 0
- `i < 5` - ulang selama i kurang dari 5
- `i++` - setiap kali selesai, i ditambah 1

---

## 10. Loop - While

Loop yang bergantung kondisi:

```javascript
let i = 0;
while (i < 5) {
  console.log(i);
  i++;
}

// Output: 0, 1, 2, 3, 4
```

Ulang selama `i < 5`.

---

## 11. Loop - Do-While

Loop yang minimal jalankan sekali (bahkan kalau kondisi salah):

```javascript
let i = 0;
do {
  console.log("Nilai " + i);
  i++;
} while (i < 3);

// Output: Nilai 0, Nilai 1, Nilai 2
```

Bedanya dengan `while`: Do-While **pasti jalankan minimal sekali**, baru cek kondisinya.

Contoh perbedaan:

```javascript
let x = 10;

// While: tidak jalan sama sekali karena kondisi salah
while (x < 5) {
  console.log("While: " + x);
}

// Do-While: jalan sekali, baru cek kondisi
do {
  console.log("Do-While: " + x);
} while (x < 5);

// Output:
// Do-While: 10
```

---

## 12. Array - Kumpulan Data

Array itu seperti daftar atau list. Misal daftar teman:

```javascript
let teman = ["Justin", "Hans", "Marcello", "Jonathan"];

console.log(teman[0]); // "Justin" (yang pertama)
console.log(teman[1]); // "Hans" (yang kedua)
console.log(teman.length); // 4 (jumlah teman)
```

Hitung mulai dari **0**, bukan 1! Yang pertama itu index 0.

---

## 13. Array Methods - Tambah & Hapus

```javascript
let buah = ["Apel", "Mangga"];

buah.push("Jeruk"); // Tambah di belakang → ["Apel", "Mangga", "Jeruk"]
buah.pop(); // Hapus yang belakang → ["Apel", "Mangga"]
buah.unshift("Pisang"); // Tambah di depan → ["Pisang", "Apel", "Mangga"]
buah.shift(); // Hapus yang depan → ["Apel", "Mangga"]
```

---

## 14. Array - Map & Filter

Ubah atau saring isi array:

```javascript
let angka = [1, 2, 3, 4, 5];

// Map - ubah semua
let double = angka.map((n) => n * 2); // [2, 4, 6, 8, 10]

// Filter - ambil yang sesuai kondisi
let genap = angka.filter((n) => n % 2 === 0); // [2, 4]
```

---

## 15. String - Manipulasi Teks

Cara ngolah teks:

```javascript
let kalimat = "Belajar JavaScript";

console.log(kalimat.length); // 18 (jumlah karakter)
console.log(kalimat.toUpperCase()); // "BELAJAR JAVASCRIPT"
console.log(kalimat.toLowerCase()); // "belajar javascript"
console.log(kalimat.includes("Java")); // true (ada kata Java?)
console.log(kalimat.replace("Java", "JS")); // "Belajar JSScript"
```

---

## 16. Object - Data Terstruktur

Object itu seperti kartu pelajar - punya nama, kelas, nomor induk, dll:

```javascript
let siswa = {
  nama: "Budi",
  kelas: "7A",
  umur: 14,
  nilai: 85,
};

console.log(siswa.nama); // "Budi"
console.log(siswa.nilai); // 85
```

---

## 17. Function - Perintah Reusable

Function itu kode yang bisa dipakai berkali-kali:

```javascript
function sapa(nama) {
  console.log("Halo " + nama);
}

sapa("Budi"); // Halo Budi
sapa("Ani"); // Halo Ani
```

---

## 18. Function - Return (Memberikan Hasil)

Function bisa kasih hasil balik:

```javascript
function tambah(a, b) {
  return a + b;
}

let hasil = tambah(5, 3); // 8
console.log(hasil);
```

---

## 19. Arrow Function - Cara Modern

Cara singkat nulis function:

```javascript
const kali = (a, b) => a * b;

console.log(kali(4, 5)); // 20
```

---

## 20. DOM - Ubah Halaman

Kita bisa ubah apa yang tampil di halaman:

```javascript
let elemen = document.getElementById("output");

elemen.textContent = "Halo Dunia!"; // Ubah teks
elemen.style.color = "red"; // Ubah warna jadi merah
elemen.style.fontSize = "20px"; // Ubah ukuran font
```

---

## 21. Event - Klik & Interaksi

Program bisa "dengarkan" apa yang user lakukan:

```javascript
let tombol = document.getElementById("myButton");

tombol.addEventListener("click", function () {
  console.log("Tombol diklik!");
});
```

Event yang sering dipakai:

- `click` - saat diklik
- `input` - saat user ketik di text box
- `submit` - saat form dikirim

---

## 22. Input .value - Ambil Data dari User

Kita sering butuh ambil apa yang user ketik di text box:

```javascript
let inputNama = document.getElementById("nama");

// Ambil apa yang user ketik
let nilai = inputNama.value;
console.log(nilai); // Tampilkan di console
```

Ingat: gunakan `.value` untuk mengambil teks dari `<input>` atau `<textarea>`.

---

## 23. Konversi Angka - parseInt & parseFloat

Saat ambil value dari input, hasilnya selalu **text** (string). Kalau mau pakai untuk hitung, harus diubah jadi angka:

```javascript
let angka = "10"; // Ini teks, bukan angka
let angka2 = "3.5";

// Ubah ke integer (angka bulat)
console.log(parseInt(angka)); // 10
console.log(parseInt(angka2)); // 3 (potong desimal)

// Ubah ke float (angka desimal)
console.log(parseFloat(angka)); // 10
console.log(parseFloat(angka2)); // 3.5
```

**Kapan pakai?** Saat ambil input dari user untuk hitung:

```javascript
let num1 = parseInt(inputAngka1.value);
let num2 = parseInt(inputAngka2.value);
let hasil = num1 + num2; // Baru bisa hitung!
```

---

## 24. Splice - Hapus Elemen Array

Untuk hapus item tertentu dari array (bukan cuma yang belakang):

```javascript
let buah = ["Apel", "Mangga", "Jeruk", "Pisang"];

// Hapus elemen di index 1 (Mangga)
buah.splice(1, 1);
console.log(buah); // ["Apel", "Jeruk", "Pisang"]

// Hapus 2 elemen mulai dari index 0
buah.splice(0, 2);
console.log(buah); // ["Pisang"]
```

Format: `array.splice(posisi, jumlah)`

- Posisi = dari mana mulai menghapus
- Jumlah = berapa elemen yang dihapus

---

## 25. SetInterval - Ulang Kode Berkala

SetInterval buat kode jalan berulang tiap interval waktu (cocok untuk timer):

```javascript
let hitungan = 0;

// Jalankan tiap 1 detik (1000 ms)
let timer = setInterval(function () {
  hitungan++;
  console.log("Detik ke-" + hitungan);

  if (hitungan === 5) {
    clearInterval(timer); // Berhenti setelah 5 detik
  }
}, 1000);
```

**Tips:** Simpan setInterval di variabel, terus pakai `clearInterval()` untuk berhenti.

---

## 26. Ubah Style dengan backgroundColor & color

Kita bisa ubah warna elemen:

```javascript
let box = document.getElementById("myBox");

// Ubah warna background
box.style.backgroundColor = "red";
box.style.backgroundColor = "rgb(255, 0, 0)";
box.style.backgroundColor = "#FF0000";

// Ubah warna teks
box.style.color = "white";

// Ubah display (sembunyikan/tampilkan)
box.style.display = "none"; // Sembunyikan
box.style.display = "block"; // Tampilkan
```

---

## 27. classList.toggle - Ubah/Lepas Class

Toggle class (kalau ada dihapus, kalau tidak ada ditambah):

```javascript
let tombol = document.getElementById("tombol");
let konten = document.getElementById("konten");

tombol.addEventListener("click", function () {
  // Toggle class "aktif" pada konten
  konten.classList.toggle("aktif");
});
```

CSS-nya:

```css
.aktif {
  background-color: yellow;
  color: black;
}
```

Setiap klik, "aktif" class ditambah/dihapus.

---

## 28. event.preventDefault() - Cegah Aksi Default

Saat form di-submit, page akan refresh. Kita bisa cegah itu:

```javascript
let form = document.getElementById("myForm");

form.addEventListener("submit", function (e) {
  e.preventDefault(); // Cegah page refresh

  // Lanjut dengan kode kita sendiri
  console.log("Form tidak refresh!");
});
```

**Penting:** Selalu pakai `e.preventDefault()` saat handle form submit.

---

## 29. Template Literals - String Lebih Rapi

Cara modern menggabung teks dan variabel (pakai backtick `` ` ``):

```javascript
let nama = "Budi";
let umur = 14;

// Cara lama
console.log("Nama saya " + nama + " umur " + umur + " tahun");

// Cara baru (lebih rapi!)
console.log(`Nama saya ${nama} umur ${umur} tahun`);
```

Pakai `${}` untuk masukkan variabel di dalam teks.

---

## 30. setTimeout - Jalankan Kode Sekali Saja

SetTimeout jalankan kode **sekali saja** setelah delay tertentu (berbeda dengan setInterval yang berkala):

```javascript
// Jalankan sekali setelah 2 detik (2000 ms)
setTimeout(function () {
  console.log("Ini jalan setelah 2 detik");
}, 2000);

// Dengan arrow function
setTimeout(() => {
  console.log("Selesai download!");
}, 3000);
```

**Kapan pakai?**

- `setTimeout`: Jalankan kode **sekali** setelah delay (misal: hide message setelah 3 detik)
- `setInterval`: Jalankan kode **berulang** tiap interval (misal: refresh data tiap 5 detik)

Contoh praktis:

```javascript
// Tampilkan pesan, hilang setelah 3 detik
let pesan = document.getElementById("pesan");
pesan.textContent = "Data berhasil disimpan!";

setTimeout(function () {
  pesan.style.display = "none"; // Sembunyikan pesan
}, 3000);
```

---

## 30. For...Of Loop - Loop Array Simpel

Cara modern dan simpel untuk loop array (tidak perlu index):

```javascript
let buah = ["Apel", "Mangga", "Jeruk"];

// Cara lama (dengan index)
for (let i = 0; i < buah.length; i++) {
  console.log(buah[i]);
}

// Cara baru - For...Of (lebih simpel!)
for (let item of buah) {
  console.log(item); // Langsung ambil nilai, tidak perlu buah[i]
}

// Output:
// Apel
// Mangga
// Jeruk
```

**Keuntungan For...Of:**

- Lebih simpel dan mudah dibaca
- Tidak perlu mikir tentang index
- Cocok saat kita cuma butuh nilai, tidak perlu index

Contoh lain:

```javascript
let siswa = ["Budi", "Ani", "Citra"];

for (let nama of siswa) {
  console.log(`Halo ${nama}`);
}

// Output:
// Halo Budi
// Halo Ani
// Halo Citra
```

---

## Penutup

1. **Latihan terus** - buat program sendiri, jangan cuma baca
2. **Buka console** - tekan F12 untuk lihat error
3. **Eksperimen** - coba ubah kode, lihat apa yang terjadi
4. **Jangan hafal** - pahami caranya, bukan hafalnya

Kalau ada yang tidak paham, tanyakan! Whatsapp aja gapapa gausah malu, tidak ada yang namanya malu bertanya, malah kalau tidak tanya sesat dijalan.

---

**Tips**: Pakai console browser (F12) untuk test potongan kode. Ini cara cepat buat belajar!
