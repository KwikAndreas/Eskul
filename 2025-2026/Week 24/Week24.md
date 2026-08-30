## SOAL CERITA: Sistem Nilai Akhir Siswa

Ibu guru minta kamu membuat program untuk **menghitung nilai akhir siswa**. Program harus:
1. Memasukkan data dari beberapa siswa
2. Menghitung nilai akhir berdasarkan formula
3. Memberikan grade (A, B, C, D) sesuai nilai akhir
4. Menampilkan hasilnya dengan kategori kelulusan

---

## Ketentuan Program

### Masukan (Input):
- **Jumlah siswa** (integer): Berapa banyak siswa yang akan diinput
- Untuk setiap siswa:
  - **Nama** (string)
  - **Nilai UH** (float): 0-100
  - **Nilai UTS** (float): 0-100
  - **Nilai UAS** (float): 0-100

### Proses (Kalkulasi):
Rumus nilai akhir:
```
Nilai Akhir = (UH × 30%) + (UTS × 30%) + (UAS × 40%)
```

### Penentuan Grade:
```
- Nilai ≥ 85  → Grade A  → Lulus Sangat Baik
- Nilai 75-84 → Grade B  → Lulus Baik
- Nilai 65-74 → Grade C  → Lulus Cukup
- Nilai < 65  → Grade D  → Tidak Lulus
```

### Keluaran (Output):
Tampilkan untuk **setiap siswa**:
```
Nama: [nama]
Nilai Akhir: [nilai bulat 2 desimal]
Grade: [grade]
Status: [Lulus/Tidak Lulus]
---
```

Setelah semua siswa, tampilkan:
```
STATISTIK:
Total Siswa: [jumlah]
Siswa Lulus: [jumlah yang lulus]
Siswa Tidak Lulus: [jumlah yang tidak lulus]
Rata-rata Nilai Kelas: [nilai rata-rata]
```

---

## PANDUAN BELAJAR

### Konsep yang Digunakan:

1. **Variabel & Tipe Data** ✓
   - String untuk nama siswa
   - Float untuk nilai (ada koma)
   - Integer untuk jumlah siswa

2. **Matematika Dasar** ✓
   - Perkalian dan persentase
   - Penjumlahan
   - Pembagian untuk rata-rata

3. **Membandingkan Nilai** ✓
   - Menggunakan `>=` dan `<`
   - Menentukan grade berdasarkan perbandingan

4. **Logika Sederhana** ✓
   - Kondisi if-else untuk penentuan grade
   - Kondisi untuk status lulus/tidak lulus

5. **Keputusan If-Else** ✓
   - Nested if-else untuk grade A, B, C, D
   - Atau bisa menggunakan if-elif

6. **Loop** ✓
   - Loop untuk memasukkan data dari multiple siswa
   - Loop untuk menampilkan hasil semua siswa

---

## CONTOH RUN PROGRAM

```
=== PROGRAM NILAI AKHIR SISWA ===
Berapa jumlah siswa? 2

--- Data Siswa 1 ---
Nama: Budi
Nilai UH: 80
Nilai UTS: 85
Nilai UAS: 90

--- Data Siswa 2 ---
Nama: Siti
Nilai UH: 70
Nilai UTS: 65
Nilai UAS: 60

=== HASIL ===
Nama: Budi
Nilai Akhir: 86.50
Grade: A
Status: Lulus Sangat Baik
---
Nama: Siti
Nilai Akhir: 64.50
Grade: D
Status: Tidak Lulus
---

STATISTIK:
Total Siswa: 2
Siswa Lulus: 1
Siswa Tidak Lulus: 1
Rata-rata Nilai Kelas: 75.50
```

---


## CHECKLIST SEBELUM SUBMIT

- [ ] Program bisa input jumlah siswa
- [ ] Ada loop untuk input multiple siswa
- [ ] Nilai akhir dihitung dengan benar
- [ ] Ada if-else untuk penentuan grade
- [ ] Output format sesuai contoh
- [ ] Statistik ditampilkan di akhir
- [ ] Tidak ada error saat dijalankan
- [ ] Sudah ditest minimal 2 contoh siswa

---
<!-- 
### 📄 KODE LENGKAP JAVASCRIPT:

```javascript
// ===== PROGRAM NILAI AKHIR SISWA =====

// Deklarasi variabel (TIPE DATA)
let daftarSiswa = [];      // Array untuk simpan data siswa
let totalNilai = 0;        // Untuk hitung rata-rata
let siswaLulus = 0;        // Penghitung siswa lulus
let siswaGagal = 0;        // Penghitung siswa tidak lulus

// Input jumlah siswa
let jumlahSiswa = parseInt(prompt("Berapa jumlah siswa?"));

// LOOP: Input data setiap siswa
for (let i = 1; i <= jumlahSiswa; i++) {
  console.log(`\n--- Data Siswa ${i} ---`);
  
  // Input data siswa (VARIABEL & TIPE DATA)
  let nama = prompt(`Nama siswa ${i}:`);
  let nilaiUH = parseFloat(prompt(`${nama} - Nilai UH (0-100):`));
  let nilaiUTS = parseFloat(prompt(`${nama} - Nilai UTS (0-100):`));
  let nilaiUAS = parseFloat(prompt(`${nama} - Nilai UAS (0-100):`));
  
  // MATEMATIKA DASAR: Hitung nilai akhir
  let nilaiAkhir = (nilaiUH * 0.3) + (nilaiUTS * 0.3) + (nilaiUAS * 0.4);
  
  // MEMBANDINGKAN NILAI & IF-ELSE: Tentukan grade
  let grade;
  let status;
  
  if (nilaiAkhir >= 85) {
    grade = "A";
    status = "Lulus Sangat Baik";
    siswaLulus++;  // Increment penghitung lulus
  } else if (nilaiAkhir >= 75) {
    grade = "B";
    status = "Lulus Baik";
    siswaLulus++;  // Increment penghitung lulus
  } else if (nilaiAkhir >= 65) {
    grade = "C";
    status = "Lulus Cukup";
    siswaLulus++;  // Increment penghitung lulus
  } else {
    grade = "D";
    status = "Tidak Lulus";
    siswaGagal++;  // Increment penghitung gagal
  }
  
  // Simpan data siswa ke array
  daftarSiswa.push({
    nama: nama,
    nilaiAkhir: nilaiAkhir,
    grade: grade,
    status: status
  });
  
  // Tambah ke total untuk rata-rata
  totalNilai += nilaiAkhir;
}

// TAMPILKAN HASIL SEMUA SISWA
console.log("\n\n=== HASIL NILAI AKHIR ===\n");
for (let siswa of daftarSiswa) {
  console.log(`Nama: ${siswa.nama}`);
  console.log(`Nilai Akhir: ${siswa.nilaiAkhir.toFixed(2)}`);
  console.log(`Grade: ${siswa.grade}`);
  console.log(`Status: ${siswa.status}`);
  console.log("---");
}

// HITUNG STATISTIK (MATEMATIKA: Pembagian)
let rataRata = totalNilai / jumlahSiswa;

console.log("\n=== STATISTIK ===");
console.log(`Total Siswa: ${jumlahSiswa}`);
console.log(`Siswa Lulus: ${siswaLulus}`);
console.log(`Siswa Tidak Lulus: ${siswaGagal}`);
console.log(`Rata-rata Nilai Kelas: ${rataRata.toFixed(2)}`);
```

--- -->

<!-- ### 📖 PENJELASAN KODE (Konsep yang Digunakan):

#### 1️⃣ **VARIABEL & TIPE DATA**
```javascript
let daftarSiswa = [];      // Array (list)
let totalNilai = 0;        // Number (integer)
let nama = prompt(...);    // String (teks)
let nilaiUH = 80;          // Number (desimal)
```

#### 2️⃣ **LOOP** - Input multiple siswa
```javascript
for (let i = 1; i <= jumlahSiswa; i++) {
  // Repeat untuk setiap siswa
}
```

#### 3️⃣ **MATEMATIKA DASAR** - Rumus nilai akhir
```javascript
let nilaiAkhir = (nilaiUH * 0.3) + (nilaiUTS * 0.3) + (nilaiUAS * 0.4);
//                 perkalian    +    perkalian    +    perkalian
//                 30% + 30% + 40% = 100%
```

#### 4️⃣ **MEMBANDINGKAN NILAI** - Menggunakan operator perbandingan
```javascript
if (nilaiAkhir >= 85)    // >= = lebih besar atau sama dengan
else if (nilaiAkhir >= 75)
else if (nilaiAkhir >= 65)
else                     // Jika tidak memenuhi kondisi di atas
```

#### 5️⃣ **LOGIKA SEDERHANA** - Status lulus/tidak lulus
```javascript
if (nilaiAkhir >= 65) {
  siswaLulus++;          // Tambah 1 ke penghitung lulus
} else {
  siswaGagal++;          // Tambah 1 ke penghitung gagal
}
```

#### 6️⃣ **IF-ELSE NESTED** - Penentuan 4 grade
```javascript
if (nilaiAkhir >= 85) {
  grade = "A";
} else if (nilaiAkhir >= 75) {
  grade = "B";
} else if (nilaiAkhir >= 65) {
  grade = "C";
} else {
  grade = "D";
}
```

--- -->

### CONTOH OUTPUT SAAT DIJALANKAN:

```
--- Data Siswa 1 ---
(Input: Budi, UH: 80, UTS: 85, UAS: 90)

--- Data Siswa 2 ---
(Input: Siti, UH: 70, UTS: 65, UAS: 60)

=== HASIL NILAI AKHIR ===

Nama: Budi
Nilai Akhir: 86.50
Grade: A
Status: Lulus Sangat Baik
---
Nama: Siti
Nilai Akhir: 64.50
Grade: D
Status: Tidak Lulus
---

=== STATISTIK ===
Total Siswa: 2
Siswa Lulus: 1
Siswa Tidak Lulus: 1
Rata-rata Nilai Kelas: 75.50
```

---

### FUNGSI JAVASCRIPT YANG DIGUNAKAN:

| Fungsi | Kegunaan |
|--------|----------|
| `prompt()` | Input data dari user |
| `parseInt()` | Convert string ke integer |
| `parseFloat()` | Convert string ke desimal |
| `push()` | Tambah item ke array |
| `toFixed(2)` | Pembulatan ke 2 desimal |
| `console.log()` | Tampilkan output |
| `for` loop | Looping data |

---

**Selamat Mengerjakan!** 💪

