# Materi Pengurutan Array (Sorting) untuk SMP

## 📚 Pengenalan Array dan Pengurutan

### Apa itu Array?

Array adalah kumpulan data yang disimpan dalam satu variabel. Bayangkan seperti kotak yang berisi beberapa item yang tersusun berurutan.

**Contoh:**

```python
nilai = [80, 75, 90, 85]  # Array berisi 4 nilai
nama = ["Andi", "Budi", "Cici"]  # Array berisi 3 nama
```

### Mengapa Perlu Mengurutkan Data?

- 🔍 **Mudah mencari**: Data yang terurut lebih mudah dicari
- 📊 **Analisis yang lebih baik**: Mudah melihat nilai tertinggi/terendah
- 📋 **Tampilan yang rapi**: Data terlihat lebih terorganisir

## 🛠️ Cara Mengurutkan Array di Python

### 1. Menggunakan `sorted()`

Fungsi ini membuat array baru yang sudah terurut, tanpa mengubah array asli.

```python
# Contoh penggunaan sorted()
angka = [5, 2, 8, 1, 9]

# Urutkan dari kecil ke besar (ascending)
angka_naik = sorted(angka)
print(angka_naik)  # Output: [1, 2, 5, 8, 9]

# Urutkan dari besar ke kecil (descending)
angka_turun = sorted(angka, reverse=True)
print(angka_turun)  # Output: [9, 8, 5, 2, 1]

# Array asli tidak berubah
print(angka)  # Output: [5, 2, 8, 1, 9]
```

### 2. Menggunakan `.sort()`

Method ini mengubah array asli secara langsung.

```python
# Contoh penggunaan .sort()
angka = [5, 2, 8, 1, 9]

# Urutkan array asli dari kecil ke besar
angka.sort()
print(angka)  # Output: [1, 2, 5, 8, 9]

# Urutkan array asli dari besar ke kecil
angka.sort(reverse=True)
print(angka)  # Output: [9, 8, 5, 2, 1]
```

## 📝 Perbedaan `sorted()` dan `.sort()`

| `sorted()`              | `.sort()`           |
| ----------------------- | ------------------- |
| Membuat array baru      | Mengubah array asli |
| Array asli tetap sama   | Array asli berubah  |
| `hasil = sorted(array)` | `array.sort()`      |

## 🎯 Latihan Soal

File `prog.py` berisi beberapa soal latihan:

1. **Soal 1**: Mengurutkan nilai ujian dari terkecil ke terbesar
2. **Soal 2**: Mengurutkan tinggi badan dari terbesar ke terkecil
3. **Soal 3**: Mengurutkan nama buah secara alfabetis
4. **Soal 4**: Mengurutkan umur dari tertua ke termuda
5. **Bonus**: Menggunakan method `.sort()`

### Cara Mengerjakan:

1. Buka file `prog.py`
2. Baca setiap soal dengan teliti
3. Hapus tanda `#` pada baris jawaban untuk melihat hasilnya
4. Coba modifikasi dan eksperimen sendiri!

## 🚀 Tips untuk Guru

### Aktivitas Pembelajaran:

1. **Demonstrasi**: Tunjukkan contoh pengurutan menggunakan objek fisik
2. **Praktek Terbimbing**: Kerjakan soal 1-2 bersama-sama
3. **Praktek Mandiri**: Biarkan siswa mengerjakan soal sisanya
4. **Diskusi**: Bahas perbedaan `sorted()` dan `.sort()`

### Variasi Soal Tambahan:

- Urutkan data suhu harian
- Urutkan daftar harga barang
- Urutkan nama siswa berdasarkan absen
- Urutkan waktu lari (dari tercepat ke terlambat)

### Kriteria Penilaian:

- ✅ Dapat membedakan `sorted()` dan `.sort()`
- ✅ Dapat mengurutkan ascending dan descending
- ✅ Memahami konsep array dan pengurutan
- ✅ Dapat menerapkan pada data berbeda

## 🎁 Pengembangan Lebih Lanjut

Setelah mahir dengan pengurutan dasar, siswa dapat mempelajari:

- Pengurutan berdasarkan kriteria khusus
- Algoritma sorting sederhana (bubble sort)
- Pengurutan data yang lebih kompleks (dictionary, tuple)

---

**Selamat Belajar! 🎓**

_Ingat: Programming adalah tentang pemecahan masalah. Semakin sering berlatih, semakin mahir!_
