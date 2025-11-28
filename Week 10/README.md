# 🔁 Week 10: Perulangan (Loop) dengan Array - Materi Terakhir Tahun Ini

## 📖 Apa itu Loop (Perulangan)?

**Loop** adalah cara untuk menjalankan kode yang sama **berulang-ulang** secara otomatis.

### Analogi Kehidupan:

```
❌ TANPA LOOP (Manual):
   print("Siswa ke-1")
   print("Siswa ke-2")
   print("Siswa ke-3")
   print("Siswa ke-4")
   print("Siswa ke-5")

✅ DENGAN LOOP (Otomatis):
   for i in range(1, 6):
       print(f"Siswa ke-{i}")
```

**Bayangkan:**

- 🎵 Tombol **repeat** di musik player
- 🏃 Berlari mengelilingi lapangan **5 putaran**
- 📝 Menulis nama **semua siswa** di daftar hadir

---

## 🔄 1. FOR LOOP - Loop untuk Array

`for` loop digunakan untuk **mengulangi aksi pada setiap item** dalam array.

### Format Dasar:

```python
for item in array:
    # Lakukan sesuatu dengan item
```

### Contoh 1: Print Semua Item

```python
buah = ["apel", "mangga", "jeruk", "pisang"]

for nama_buah in buah:
    print(nama_buah)
```

**Output:**

```
apel
mangga
jeruk
pisang
```

💡 **Penjelasan:** `nama_buah` adalah variabel sementara yang berubah setiap loop.

---

### Contoh 2: Print dengan Nomor Urut

```python
siswa = ["Andi", "Budi", "Cici", "Dodi"]

for i in range(len(siswa)):
    print(f"{i+1}. {siswa[i]}")
```

**Output:**

```
1. Jaden
2. Raphael
3. Nathan
4. Justin
```

💡 **Tips:**

- `range(len(siswa))` → menghasilkan 0, 1, 2, 3
- `i+1` → supaya mulai dari 1, bukan 0

---

### Contoh 3: Loop dengan Kondisi

```python
nilai = [85, 92, 65, 78, 95, 70, 88]

print("Siswa yang LULUS (nilai ≥ 75):")
for n in nilai:
    if n >= 75:
        print(f"✓ Nilai {n} - LULUS")
```

**Output:**

```
Siswa yang LULUS (nilai ≥ 75):
✓ Nilai 85 - LULUS
✓ Nilai 92 - LULUS
✓ Nilai 78 - LULUS
✓ Nilai 95 - LULUS
✓ Nilai 88 - LULUS
```

---

## 🔢 2. WHILE LOOP - Loop dengan Counter

`while` loop terus berjalan **selama kondisi masih True**.

### Format Dasar:

```python
while kondisi:
    # Lakukan sesuatu
    # Ubah kondisi (penting!)
```

### Contoh 1: Countdown Sederhana

```python
hitung = 5

while hitung > 0:
    print(f"Countdown: {hitung}")
    hitung = hitung - 1  # atau hitung -= 1

print("🚀 Start!")
```

**Output:**

```
Countdown: 5
Countdown: 4
Countdown: 3
Countdown: 2
Countdown: 1
🚀 Start!
```

⚠️ **HATI-HATI:** Jika tidak mengubah `hitung`, loop akan berjalan SELAMANYA (infinite loop)!

---

### Contoh 2: Input Berulang Sampai Benar

```python
password = ""

while password != "1234":
    password = input("Masukkan password: ")
    if password != "1234":
        print("❌ Salah! Coba lagi.")

print("✅ Password benar!")
```

---

## 🎯 3. Loop + Array Operations

### A. Hitung Total dan Rata-rata

```python
nilai_siswa = [80, 75, 90, 85, 95]

# Hitung total
total = 0
for nilai in nilai_siswa:
    total = total + nilai

# Hitung rata-rata
rata_rata = total / len(nilai_siswa)

print(f"Total nilai: {total}")
print(f"Rata-rata kelas: {rata_rata}")
```

**Output:**

```
Total nilai: 425
Rata-rata kelas: 85.0
```

---

### B. Cari Nilai Tertinggi

```python
angka = [45, 78, 92, 34, 88, 56]

tertinggi = angka[0]  # Mulai dari nilai pertama

for num in angka:
    if num > tertinggi:
        tertinggi = num

print(f"Nilai tertinggi: {tertinggi}")
```

**Output:**

```
Nilai tertinggi: 92
```

---

### C. Hitung Jumlah Item Tertentu

```python
hewan = ["kucing", "anjing", "kucing", "burung", "kucing", "ikan"]

jumlah_kucing = 0

for h in hewan:
    if h == "kucing":
        jumlah_kucing += 1

print(f"Ada {jumlah_kucing} kucing")
```

**Output:**

```
Ada 3 kucing
```

---

## 🔥 4. Loop + Manipulasi Array (Kombinasi Week 9!)

### Contoh: Tambah Item Berulang

```python
daftar_belanja = []

print("Masukkan 3 barang belanjaan:")
for i in range(3):
    barang = input(f"Barang ke-{i+1}: ")
    daftar_belanja.append(barang)

print("\n📋 Daftar belanja Anda:")
for item in daftar_belanja:
    print(f"• {item}")
```

**Contoh Interaksi:**

```
Masukkan 3 barang belanjaan:
Barang ke-1: Susu
Barang ke-2: Roti
Barang ke-3: Telur

📋 Daftar belanja Anda:
• Susu
• Roti
• Telur
```

---

## 📋 Tabel Perbandingan FOR vs WHILE

| **Aspek**        | **FOR Loop**                       | **WHILE Loop**                  |
| ---------------- | ---------------------------------- | ------------------------------- |
| **Kapan pakai?** | Jumlah pengulangan sudah diketahui | Loop sampai kondisi terpenuhi   |
| **Contoh Use**   | Loop melalui array, range angka    | Input sampai benar, countdown   |
| **Syntax**       | `for item in array:`               | `while kondisi:`                |
| **Keunggulan**   | Lebih ringkas untuk array          | Fleksibel untuk kondisi dinamis |

---

## 💡 Pattern Loop yang Sering Dipakai

### 1️⃣ Print Semua Item dengan Nomor

```python
items = ["Item A", "Item B", "Item C"]
for i, item in enumerate(items, start=1):
    print(f"{i}. {item}")
```

### 2️⃣ Filter dan Kumpulkan Data

```python
angka = [10, 25, 30, 15, 40, 8]
angka_besar = []

for n in angka:
    if n >= 20:
        angka_besar.append(n)

print(angka_besar)  # [25, 30, 40]
```

### 3️⃣ Range dengan Langkah (Step)

```python
# Angka genap dari 0-10
for i in range(0, 11, 2):
    print(i)  # 0, 2, 4, 6, 8, 10
```

---

## ❌ Kesalahan Umum & Solusinya

### Kesalahan 1: Lupa Indentasi

```python
❌ SALAH:
for i in range(5):
print(i)  # Error: harus pakai indentasi!

✅ BENAR:
for i in range(5):
    print(i)  # Pakai 4 spasi atau 1 tab
```

### Kesalahan 2: Infinite Loop pada While

```python
❌ SALAH:
x = 1
while x < 5:
    print(x)  # Loop selamanya, x tidak berubah!

✅ BENAR:
x = 1
while x < 5:
    print(x)
    x += 1  # HARUS update x
```

### Kesalahan 3: Modifikasi Array Saat Loop

```python
❌ SALAH:
angka = [1, 2, 3, 4, 5]
for n in angka:
    angka.remove(n)  # Bisa error!

✅ BENAR:
angka = [1, 2, 3, 4, 5]
angka.clear()  # Atau buat array baru
```

---

## 🎮 Latihan Praktis (15 Menit)

File `prog10.py` berisi **5 latihan singkat** untuk dipraktikkan:

1. **Loop Dasar**: Print angka 1-10
2. **Loop Array**: Print semua nama siswa
3. **Hitung Total**: Jumlahkan semua nilai
4. **Filter Data**: Tampilkan nilai yang lulus
5. **Input Berulang**: Tambah 3 item ke array

---

## 🎓 Tips untuk Latihan di Rumah

### Eksperimen yang Bisa Dicoba:

- 🔢 Buat tabel perkalian dengan loop
- 📊 Hitung rata-rata tinggi badan kelas
- 🎵 Buat playlist sederhana (tambah/hapus/loop songs)
- 🛒 Simulasi kasir dengan loop input barang
- 🎮 Loop untuk inventory game

---

## 🔗 Hubungan dengan Materi Sebelumnya

```
Week 5: Array Dasar → Membuat dan akses array
         ↓
Week 8: Sorting → Mengurutkan array
         ↓
Week 9: Manipulasi → Tambah/hapus/pindah item
         ↓
Week 10: LOOP → Proses SEMUA item secara otomatis! ✨
```

**Sekarang Anda bisa:**

- ✅ Membuat array
- ✅ Mengurutkan data
- ✅ Menambah/menghapus item
- ✅ **Proses semua data dengan loop!**

---

## 🎯 Tugas Eskul Coding 28 November 2025, Deadline 20.00 malam

### Tugas 1: Sistem Penilaian Otomatis

```python
# Buat program yang:
# 1. Loop input 5 nilai siswa
# 2. Hitung rata-rata
# 3. Tampilkan berapa siswa yang lulus (≥75)
```

### Tugas 2: Kasir Sederhana

```python
# Buat program yang:
# 1. Loop input harga barang (max 5 barang)
# 2. Hitung total belanja
# 3. Terapkan diskon 10% jika total > 100.000
```

---

## 📞 FAQ

**Q1: Kapan pakai `for` dan kapan pakai `while`?**

- `for` → Saat tahu berapa kali loop atau loop array
- `while` → Saat loop sampai kondisi tertentu tercapai

**Q2: Apa itu `range()`?**

- `range(5)` → 0, 1, 2, 3, 4 (5 angka dari 0)
- `range(1, 6)` → 1, 2, 3, 4, 5 (dari 1 sampai 5)
- `range(0, 10, 2)` → 0, 2, 4, 6, 8 (loncat 2)

**Q3: Kenapa `for` loop tidak perlu counter manual?**
Python otomatis menangani perpindahan ke item berikutnya!

**Q4: Bagaimana stop loop di tengah jalan?**
Gunakan `break` untuk keluar dari loop.

---

## 🎊 Selamat! Anda Sudah Menyelesaikan Fondasi Python!

### Yang Sudah Anda Kuasai:

- ✅ Variabel dan tipe data
- ✅ Input/Output
- ✅ Operasi matematika
- ✅ Conditional (if/elif/else)
- ✅ Array/List
- ✅ Sorting (mengurutkan)
- ✅ Manipulasi array (insert/remove/move)
- ✅ **LOOP (for/while)**

### 🚀 Tahun Depan: Level Selanjutnya!

- 📦 **Function** - Membuat perintah sendiri
- 🎯 **Nested Loop** - Loop dalam loop
- 📝 **Dictionary** - Data key-value
- 🎮 **Mini Project** - Game & aplikasi sederhana
- 🌐 **Pengenalan Web** - HTML/CSS basics

---

## 🎁 Bonus: Code Template untuk Dicoba

```python
# Template: Loop untuk Statistik Data
data = [85, 90, 78, 92, 88, 76, 95]

total = 0
tertinggi = data[0]
terendah = data[0]

for nilai in data:
    total += nilai
    if nilai > tertinggi:
        tertinggi = nilai
    if nilai < terendah:
        terendah = nilai

rata = total / len(data)

print(f"📊 Statistik Data:")
print(f"Total    : {total}")
print(f"Rata-rata: {rata}")
print(f"Tertinggi: {tertinggi}")
print(f"Terendah : {terendah}")
```

---

## 🏆 Achievement Unlocked!

```
🎖️ Python Beginner - COMPLETE!

Anda telah menyelesaikan:
✓ 10 Week Python Fundamentals
✓ 50+ Exercise Problems
✓ Array Mastery (Create, Sort, Manipulate, Loop)
✓ Logic & Conditional Thinking
✓ Ready for Next Level!

🎉 Selamat Libur & Sampai Jumpa Tahun Depan! 🎉
```

---

_💪 Keep coding, keep learning! Practice makes perfect!_

_🎯 Tahun depan kita akan buat program yang lebih keren lagi!_
