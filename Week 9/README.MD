# 📚 Materi Manipulasi Array (Minggu ke-9)

## 🎯 Tujuan Pembelajaran## 📚 Apa itu Manipulasi Array?

Setelah mempelajari Week 9, Anda akan memahami:Bayangkan Anda punya **kotak berisi bola** yang berjajar di atas meja:

- ✅ Konsep index (dimulai dari 0)```

- ✅ Menambah item dengan `.append()` dan `.insert()`Posisi: 0 1 2 3

- ✅ Menghapus item dengan `.remove()` dan `.pop()`Array: 🟥 🟦 🟩 🟨

- ✅ Memindahkan item dari satu posisi ke posisi lain```

- ✅ Mengetahui kapan menggunakan method yang tepat

**Manipulasi array** adalah cara untuk:

---

- ➕ Menambah bola baru

## 📖 Apa itu Manipulasi Array?- ➖ Menghilangkan bola yang ada

- ↔️ Memindahkan bola ke posisi lain

Bayangkan Anda punya **kotak berisi bola** yang berjajar di atas meja:

Inilah yang akan kita pelajari minggu ini! 🎯

````

Posisi:  0      1      2      3---

Array:  🟥     🟦     🟩     🟨

```## 📖 Pengertian Index (Posisi)



**Manipulasi array** adalah cara untuk:**Index** adalah nomor posisi setiap item dalam array, dimulai dari **0** (bukan 1!).

- ➕ Menambah bola baru

- ➖ Menghilangkan bola yang ada

- ↔️ Memindahkan bola ke posisi lainContoh Array:    ["Apel", "Mangga", "Jeruk", "Pisang"]

Index:            0        1         2        3

Inilah yang akan kita pelajari minggu ini! 🎯```



---⚠️ **Ingat:** Index dimulai dari 0, bukan 1!



## 📌 Pengertian Index (Posisi) - PENTING!---



**Index** adalah nomor posisi setiap item dalam array, dimulai dari **0** (bukan 1!).## 🛠️ 6 Method Utama Manipulasi Array



```### 1️⃣ `.append()` - Tambah di AKHIR

Contoh Array:    ["Apel", "Mangga", "Jeruk", "Pisang"]

Index:            0        1         2        3

````

```````python

⚠️ **INGAT:** Index dimulai dari 0, bukan 1! Ini sangat penting!buah = ["apel", "mangga", "jeruk"]

# Sebelum:  [0]"apel"  [1]"mangga"  [2]"jeruk"

**Akses item berdasarkan index:**

```pythonbuah.append("pisang")

buah = ["Apel", "Mangga", "Jeruk", "Pisang"]

print(buah[0])  # Output: "Apel"# Sesudah:  [0]"apel"  [1]"mangga"  [2]"jeruk"  [3]"pisang"

print(buah[1])  # Output: "Mangga"print(buah)

print(buah[2])  # Output: "Jeruk"```

print(buah[3])  # Output: "Pisang"

```**Output:**



---```

['apel', 'mangga', 'jeruk', 'pisang']

## 🛠️ 6 Method Utama Manipulasi Array```



### 1️⃣ `.append()` - Tambah di AKHIR💡 **Kapan pakai:** Saat ingin menambah data baru di akhir (contoh: tambah teman di grup chat)



**Kegunaan:** Menambahkan 1 item baru di posisi paling akhir.### 2️⃣ `.insert()` - Tambah di POSISI TERTENTU



```python**Kegunaan:** Menambahkan 1 item di posisi (index) yang kita pilih.

buah = ["apel", "mangga", "jeruk"]

# Sebelum:  [0]"apel"  [1]"mangga"  [2]"jeruk"```python

warna = ["merah", "biru", "hijau"]

buah.append("pisang")# Sebelum:  [0]"merah"  [1]"biru"  [2]"hijau"



# Sesudah:  [0]"apel"  [1]"mangga"  [2]"jeruk"  [3]"pisang"warna.insert(1, "kuning")

print(buah)  # Output: ['apel', 'mangga', 'jeruk', 'pisang']

```# Sesudah:  [0]"merah"  [1]"kuning"  [2]"biru"  [3]"hijau"

print(warna)

💡 **Kapan pakai:** Saat ingin menambah data baru di akhir (contoh: tambah teman di grup chat)```



---**Output:**



### 2️⃣ `.insert()` - Tambah di POSISI TERTENTU```

['merah', 'kuning', 'biru', 'hijau']

**Kegunaan:** Menambahkan 1 item di posisi (index) yang kita pilih.```



```python💡 **Kapan pakai:** Saat ingin memasukkan data di tengah-tengah (contoh: antri di urutan tertentu)

warna = ["merah", "biru", "hijau"]

# Sebelum:  [0]"merah"  [1]"biru"  [2]"hijau"---



warna.insert(1, "kuning")#### B. `.insert()` - Menambah di Posisi Tertentu



# Sesudah:  [0]"merah"  [1]"kuning"  [2]"biru"  [3]"hijau"Digunakan untuk menambahkan item di **posisi spesifik**.

print(warna)  # Output: ['merah', 'kuning', 'biru', 'hijau']

``````python

warna = ["merah", "biru", "hijau"]

💡 **Kapan pakai:** Saat ingin memasukkan data di tengah-tengah (contoh: antri di urutan tertentu)print(warna)  # Output: ['merah', 'biru', 'hijau']



---# Tambahkan "kuning" di index 1 (posisi ke-2)

warna.insert(1, "kuning")

### 3️⃣ `.remove()` - Hapus Berdasarkan NILAI (Nama)print(warna)  # Output: ['merah', 'kuning', 'biru', 'hijau']

```````

**Kegunaan:** Menghapus item berdasarkan **apa isinya**, bukan posisinya.

**Ciri-ciri `.insert()`:**

````python

hewan = ["sapi", "kucing", "anjing", "burung"]- Menambah item di posisi tertentu (berdasarkan index)

# Sebelum:  [0]"sapi"  [1]"kucing"  [2]"anjing"  [3]"burung"- Item di belakangnya akan bergeser

- Sintaks: `array.insert(index, item)`

hewan.remove("kucing")

**Perbedaan Index:**

# Sesudah:  [0]"sapi"  [1]"anjing"  [2]"burung"

print(hewan)  # Output: ['sapi', 'anjing', 'burung']```

```Index:  0        1        2        3

Array: 'merah' 'kuning' 'biru'  'hijau'

💡 **Kapan pakai:** Saat tahu nama/nilai yang mau dihapus (contoh: hapus "Budi" dari grup)```



⚠️ **Hati-hati:** Jika nilai tidak ada, akan ERROR!---



---### 3️⃣ `.remove()` - Hapus Berdasarkan NILAI (Nama)



### 4️⃣ `.pop()` - Hapus Berdasarkan POSISI (Index)**Kegunaan:** Menghapus item berdasarkan **apa isinya**, bukan posisinya.



**Kegunaan:** Menghapus item berdasarkan **nomor posisinya**, bukan namanya.```python

hewan = ["sapi", "kucing", "anjing", "burung"]

```python# Sebelum:  [0]"sapi"  [1]"kucing"  [2]"anjing"  [3]"burung"

angka = [10, 20, 30, 40, 50]

# Sebelum:  [0]10  [1]20  [2]30  [3]40  [4]50hewan.remove("kucing")



angka.pop(2)  # Hapus item di posisi index 2 (yaitu 30)# Sesudah:  [0]"sapi"  [1]"anjing"  [2]"burung"

print(hewan)

# Sesudah:  [0]10  [1]20  [2]40  [3]50```

print(angka)  # Output: [10, 20, 40, 50]

```**Output:**



💡 **Kapan pakai:** Saat tahu nomor urut yang mau dihapus (contoh: hapus orang no. 2 dalam antrian)```

['sapi', 'anjing', 'burung']

**Bonus - Hapus Item Terakhir:**```

```python

nama = ["Andi", "Budi", "Cici"]💡 **Kapan pakai:** Saat tahu nama/nilai yang mau dihapus (contoh: hapus "Budi" dari grup)

nama.pop()  # Tidak perlu nulis index, langsung hapus yang terakhir

print(nama)  # Output: ['Andi', 'Budi']⚠️ **Hati-hati:** Jika nilai tidak ada, akan ERROR!

````

---

---

#### A. `.remove()` - Menghapus Berdasarkan Nilai

### 5️⃣ `.clear()` - Hapus SEMUA Item

Digunakan untuk menghapus item berdasarkan **nilainya**.

**Kegunaan:** Mengosongkan array sekaligus.

````python

```pythonhewan = ["sapi", "kucing", "anjing", "burung"]

nomor = [1, 2, 3, 4, 5]print(hewan)  # Output: ['sapi', 'kucing', 'anjing', 'burung']

print(nomor)  # Output: [1, 2, 3, 4, 5]

# Hapus "kucing"

nomor.clear()hewan.remove("kucing")

print(hewan)  # Output: ['sapi', 'anjing', 'burung']

print(nomor)  # Output: []  (kosong!)```

````

**Ciri-ciri `.remove()`:**

💡 **Kapan pakai:** Saat ingin reset/mengosongkan data (contoh: hapus semua pesan chat)

- Menghapus item berdasarkan **nilai** (bukan index)

---- Jika ada nilai yang sama, hanya yang pertama yang dihapus

- Jika nilai tidak ditemukan, akan error

### 6️⃣ MEMINDAHKAN - Kombinasi `.pop()` + `.append()` atau `.insert()`- Sintaks: `array.remove(value)`

**Kegunaan:** Mengubah posisi item dari satu tempat ke tempat lain.---

**Contoh 1: Pindahkan ke AKHIR**### 4️⃣ `.pop()` - Hapus Berdasarkan POSISI (Index)

````python

antrian = ["Ali", "Bina", "Citra", "Dini"]**Kegunaan:** Menghapus item berdasarkan **nomor posisinya**, bukan namanya.



# Pindahkan Citra ke akhir```python

item = antrian.pop(2)      # Ambil Citra dari posisi 2angka = [10, 20, 30, 40, 50]

antrian.append(item)       # Tambahkan ke akhir# Sebelum:  [0]10  [1]20  [2]30  [3]40  [4]50



print(antrian)  # Output: ['Ali', 'Bina', 'Dini', 'Citra']angka.pop(2)  # Hapus item di posisi index 2 (yaitu 30)

````

# Sesudah: [0]10 [1]20 [2]40 [3]50

**Contoh 2: Pindahkan ke AWAL**print(angka)

`python`

barang = ["pensil", "penghapus", "penggaris", "buku"]

**Output:**

# Pindahkan buku ke awal

item = barang.pop(3) # Ambil buku dari posisi 3```

barang.insert(0, item) # Tambahkan ke posisi 0 (awal)[10, 20, 40, 50]

````

print(barang)  # Output: ['buku', 'pensil', 'penghapus', 'penggaris']

```💡 **Kapan pakai:** Saat tahu nomor urut yang mau dihapus (contoh: hapus orang no. 2 dalam antrian)



💡 **Ingat:** `.pop()` ambil dulu, terus `.append()` atau `.insert()` untuk letakkan di tempat baru!**Bonus - Hapus Item Terakhir:**



---```python

nama = ["Andi", "Budi", "Cici"]

## 📋 Tabel Cepat - Pilih Method yang Tepat!nama.pop()  # Tidak perlu nulis index, langsung hapus yang terakhir

print(nama)  # Output: ['Andi', 'Budi']

| **Mau Apa?** | **Gunakan** | **Contoh** |```

|---|---|---|

| Tambah di AKHIR | `.append()` | `list.append("baru")` |---

| Tambah di POSISI TERTENTU | `.insert()` | `list.insert(1, "baru")` |

| Hapus berdasarkan NAMA | `.remove()` | `list.remove("lama")` |#### B. `.pop()` - Menghapus Berdasarkan Index

| Hapus berdasarkan POSISI | `.pop()` | `list.pop(1)` |

| Hapus TERAKHIR | `.pop()` | `list.pop()` |Digunakan untuk menghapus item berdasarkan **posisinya (index)**.

| Hapus SEMUA | `.clear()` | `list.clear()` |

| PINDAH ke AKHIR | `.pop()` + `.append()` | `list.append(list.pop(1))` |```python

| PINDAH ke AWAL | `.pop()` + `.insert()` | `list.insert(0, list.pop(1))` |angka = [10, 20, 30, 40, 50]

print(angka)  # Output: [10, 20, 30, 40, 50]

---

# Hapus item di index 2 (nilai 30)

## ❌ Kesalahan Umum yang Sering Terjadiitem_terhapus = angka.pop(2)

print(f"Item yang dihapus: {item_terhapus}")  # Output: 30

### Kesalahan 1: Lupa Index Dimulai dari 0print(angka)  # Output: [10, 20, 40, 50]

```python```

# ❌ SALAH

buah = ["apel", "mangga", "jeruk"]**Pop tanpa Argument (menghapus yang terakhir):**

print(buah[1])  # Berharap "apel", padahal output "mangga"

```python

# ✅ BENARnama = ["Andi", "Budi", "Cici"]

print(buah[0])  # Output: "apel" (index 0 = posisi pertama)

```# Hapus item terakhir

nama_terakhir = nama.pop()

### Kesalahan 2: Gunakan `.remove()` Padahal Nilai Tidak Adaprint(nama_terakhir)  # Output: Cici

```pythonprint(nama)  # Output: ['Andi', 'Budi']

# ❌ SALAH - ERROR!```

hewan = ["sapi", "kucing", "anjing"]

hewan.remove("harimau")  # "harimau" tidak ada dalam list!**Ciri-ciri `.pop()`:**



# ✅ BENAR- Menghapus item berdasarkan **index** (posisi)

hewan.remove("kucing")  # "kucing" ada, baru dihapus- Mengembalikan nilai item yang dihapus

```- Jika tidak ada argument, menghapus item terakhir

- Sintaks: `array.pop(index)` atau `array.pop()`

### Kesalahan 3: Gunakan `.insert()` dengan Index yang Terlalu Besar

```python---

# ❌ SALAH - akan error

angka = [1, 2, 3]### 5️⃣ `.clear()` - Hapus SEMUA Item

angka.insert(10, 4)  # Index 10 tidak ada!

**Kegunaan:** Mengosongkan array sekaligus.

# ✅ BENAR

angka.insert(3, 4)  # Atau pakai .append(4)```python

```nomor = [1, 2, 3, 4, 5]

print(nomor)  # Output: [1, 2, 3, 4, 5]

### Kesalahan 4: Tidak Menyimpan Hasil `.pop()`

```pythonnomor.clear()

# ❌ SAYANG - item hilang!

nama = ["Andi", "Budi", "Cici"]print(nomor)  # Output: []  (kosong!)

nama.pop(1)  # Budi dihapus, tapi tidak disimpan```



# ✅ BENAR - simpan dulu💡 **Kapan pakai:** Saat ingin reset/mengosongkan data (contoh: hapus semua pesan chat)

nama_dihapus = nama.pop(1)

print(nama_dihapus)  # "Budi"---

````

#### C. `.clear()` - Menghapus Semua Item

---

Digunakan untuk menghapus **semua item** dalam array.

## 📝 File Latihan & Tugas

`````python

File `prog9.py` berisi:nomor = [1, 2, 3, 4, 5]

nomor.clear()

### 🔹 **LATIHAN SOAL (5 soal)**print(nomor)  # Output: []

1. Tambah item dengan `.append()````

2. Tambah item dengan `.insert()`

3. Hapus dengan `.remove()`---

4. Hapus dengan `.pop()`

5. Pindahkan item### 6️⃣ MEMINDAHKAN - Kombinasi `.pop()` + `.append()` atau `.insert()`



### TUGAS MANDIRI (5 soal kompleks) Deadline Sabtu jam 08.00
## Mengirim tugas dengan menambahkan # Nama - kelas di baris pertama program

1. **Manajemen Daftar Siswa Aktif** - Gabung operasi add/remove/move

2. **Manajemen Belanja Online** - Simulasi keranjang belanja**Contoh 1: Pindahkan ke AKHIR**

3. **Manajemen Antrian Pemain Game** - Simulasi warnet gaming

4. **Manajemen Playlist Musik** - Atur urutan lagu favorit```python

5. **Manajemen Urutan Presentasi** - Ubah urutan siswa presentasiantrian = ["Ali", "Bina", "Citra", "Dini"]
    - Sebelum:  [0]"Ali"  [1]"Bina"  [2]"Citra"  [3]"Dini"
    - Sesudah:  [0]"Ali"  [1]"Bina"  [2]"Dini"  [3]"Citra"

---

# Pindahkan Citra ke akhir

## 📞 FAQ - Pertanyaan yang Sering Diajakanitem = antrian.pop(2)      # Ambil Citra dari posisi 2

antrian.append(item)       # Tambahkan ke akhir

**Q1: Apa bedanya `.remove()` dan `.pop()`?**

```# Sesudah:  [0]"Ali"  [1]"Bina"  [2]"Dini"  [3]"Citra"

.remove("nilai")  → Hapus berdasarkan NAMA/NILAIprint(antrian)

.pop(index)       → Hapus berdasarkan POSISI/NOMOR```

`````

**Output:**

**Q2: Jika `.pop()` tanpa argument, apa yang terjadi?**

A: Akan menghapus item **paling akhir** dari array.```

['Ali', 'Bina', 'Dini', 'Citra']

**Q3: Bagaimana cara pindah item ke posisi tertentu?**```

A: Kombinasi `.pop()` untuk ambil + `.insert()` untuk letakkan.

**Contoh 2: Pindahkan ke AWAL**

**Q4: Apa bedanya `.clear()` dan `.pop()` berulang-ulang?**

A: Hasilnya sama (array kosong), tapi `.clear()` lebih cepat!```python

barang = ["pensil", "penghapus", "penggaris", "buku"]

**Q5: Kenapa saya perlu `.append()`? Bisa pakai `.insert()` kan?**

A: Bisa, tapi `.append()` lebih cepat untuk menambah di akhir.# Pindahkan buku ke awal

item = barang.pop(3) # Ambil buku dari posisi 3

---barang.insert(0, item) # Tambahkan ke posisi 0 (awal)

## 🎮 Mini Game untuk Latihanprint(barang)

```

### Game 1: "Tebak Hasilnya!"

**Output:**

Tanpa menjalankan, tebak output:

```

```````python['buku', 'pensil', 'penghapus', 'penggaris']

a = [1, 2, 3, 4, 5]```

a.pop(2)

print(a)💡 **Ingat:** `.pop()` ambil dulu, terus `.append()` atau `.insert()` untuk letakkan di tempat baru!

# Hasilnya? [1, 2, 4, 5] ✅

---

b = ["X", "Y", "Z"]

b.insert(1, "A")### 3. MEMINDAHKAN ITEM (MOVE)

print(b)

# Hasilnya? ['X', 'A', 'Y', 'Z']Untuk memindahkan item, kita kombinasikan `.pop()` dan `.append()` atau `.insert()`.



c = [10, 20, 30]---

c.remove(20)

print(c)## 📋 Tabel Cepat - Pilih Method yang Tepat!

# Hasilnya? [10, 30]

| **Mau Apa?**              | **Gunakan**            | **Contoh**                    |

d = ["Merah", "Biru", "Hijau"]| ------------------------- | ---------------------- | ----------------------------- |

x = d.pop(1)| Tambah di AKHIR           | `.append()`            | `list.append("baru")`         |

d.append(x)| Tambah di POSISI TERTENTU | `.insert()`            | `list.insert(1, "baru")`      |

print(d)| Hapus berdasarkan NAMA    | `.remove()`            | `list.remove("lama")`         |

# Hasilnya? ['Merah', 'Hijau', 'Biru']| Hapus berdasarkan POSISI  | `.pop()`               | `list.pop(1)`                 |

```| Hapus TERAKHIR            | `.pop()`               | `list.pop()`                  |

| Hapus SEMUA               | `.clear()`             | `list.clear()`                |

---| PINDAH ke AKHIR           | `.pop()` + `.append()` | `list.append(list.pop(1))`    |

| PINDAH ke AWAL            | `.pop()` + `.insert()` | `list.insert(0, list.pop(1))` |

## 💡 Contoh Kasus Nyata

---

### 1. Manajemen Todo List

## ❌ Kesalahan Umum yang Sering Terjadi

```python

# Todo list harian### Kesalahan 1: Lupa Index Dimulai dari 0

tugas = ["Belajar", "Bermain", "Makan"]

```python

# Tambah tugas baru# ❌ SALAH

tugas.append("Istirahat")buah = ["apel", "mangga", "jeruk"]

print(buah[1])  # Berharap "apel", padahal output "mangga"

# Insert tugas di tempat penting (index 1)

tugas.insert(1, "Minum")# ✅ BENAR

print(buah[0])  # Output: "apel" (index 0 = posisi pertama)

# Hapus tugas yang sudah selesai```

tugas.remove("Bermain")

### Kesalahan 2: Gunakan `.remove()` Padahal Nilai Tidak Ada

print(tugas)  # Output: ['Belajar', 'Minum', 'Makan', 'Istirahat']

``````python

# ❌ SALAH - ERROR!

### 2. Manajemen Urutan Bermain Gamehewan = ["sapi", "kucing", "anjing"]

hewan.remove("harimau")  # "harimau" tidak ada dalam list!

```python

# Urutan pemain# ✅ BENAR

pemain = ["Andi", "Budi", "Cici", "Dodi"]hewan.remove("kucing")  # "kucing" ada, baru dihapus

```````

# Pindahkan Dodi ke giliran pertama

orang = pemain.pop(3)### Kesalahan 3: Gunakan `.insert()` dengan Index yang Terlalu Besar

pemain.insert(0, orang)

````python

print(pemain)  # Output: ['Dodi', 'Andi', 'Budi', 'Cici']# ❌ SALAH - akan error

```angka = [1, 2, 3]

angka.insert(10, 4)  # Index 10 tidak ada!

### 3. Mengelola Inventori Toko

# ✅ BENAR

```pythonangka.insert(3, 4)  # Atau pakai .append(4)

# Stok barang```

barang = ["Pensil", "Penggaris", "Penghapus"]

### Kesalahan 4: Tidak Menyimpan Hasil `.pop()`

# Barang baru masuk

barang.append("Buku")```python

# ❌ SAYANG - item hilang!

# Stok lama dihapus (sudah terjual)nama = ["Andi", "Budi", "Cici"]

barang.pop(1)  # Hapus "Penggaris"nama.pop(1)  # Budi dihapus, tapi tidak disimpan



print(barang)  # ['Pensil', 'Penghapus', 'Buku']# ✅ BENAR - simpan dulu

```nama_dihapus = nama.pop(1)

print(nama_dihapus)  # "Budi"

---```



## 🎓 Tips untuk Guru---



### Strategi Pengajaran:## 🎯 Latihan Soal



1. **Demonstrasi Fisik**: Gunakan objek nyata (pensil, buku) untuk menunjukkan insert/removeFile `prog9.py` berisi beberapa soal latihan:

2. **Praktek Terbimbing**: Kerjakan Latihan 1-2 bersama

3. **Praktek Mandiri**: Biarkan siswa mengerjakan Latihan 3-5### **Soal 1: Memasukkan Item**

4. **Diskusi**: Tanyakan perbedaan `.remove()` vs `.pop()`

5. **Kasus Nyata**: Tunjukkan aplikasi dalam kehidupan sehari-hari- Gunakan `.append()` untuk menambah item di akhir

- Gunakan `.insert()` untuk menambah di posisi spesifik

### Aktivitas Interaktif:

### **Soal 2: Menghapus Item**

- 👥 **Simulasi Antrian**: Siswa berdiri sebagai array item

- 🎮 **Game Sederhana**: Manajemen inventory dalam game- Gunakan `.remove()` untuk menghapus berdasarkan nilai

- 📝 **Proyek Mini**: Buat aplikasi todo list- Gunakan `.pop()` untuk menghapus berdasarkan index



### Kriteria Penilaian:### **Soal 3: Memindahkan Item**



✅ Dapat membedakan `.append()` dan `.insert()`  - Kombinasikan `.pop()` dan `.append()` untuk pindah ke akhir

✅ Dapat menggunakan `.remove()` dan `.pop()`  - Kombinasikan `.pop()` dan `.insert()` untuk pindah ke posisi lain

✅ Memahami perbedaan berdasarkan **nilai vs index**

✅ Dapat memindahkan item antar posisi  ### **Soal 4: Kombinasi**

✅ Dapat menerapkan pada kasus berbeda

✅ Dapat menyelesaikan semua tugas dengan benar- Praktik menggunakan berbagai method sekaligus

- Skenario praktis: manajemen daftar putar musik

---

### **Bonus: Operasi Lanjutan**

## 🎯 Checklist Pembelajaran

- `.clear()` untuk menghapus semua

Pastikan siswa sudah memahami:- `len()` untuk mengetahui jumlah item



- [ ] Perbedaan `.append()` dan `.insert()`---

- [ ] Kapan menggunakan `.remove()` dan `.pop()`

- [ ] Cara memindahkan item dengan `.pop()` + `.append()`/`.insert()`## 🚀 Cara Mengerjakan Soal

- [ ] Cara membaca dan menulis di index yang tepat

- [ ] Dapat menyelesaikan semua latihan soal1. **Buka file `prog9.py`**

- [ ] Dapat menyelesaikan semua tugas mandiri2. **Baca setiap soal** dengan teliti

- [ ] Bisa membuat contoh sendiri3. **Tulis kode** di setiap bagian yang diminta

4. **Hapus tanda `#`** pada baris jawaban untuk melihat hasilnya

---5. **Jalankan program** dengan Python

6. **Eksperimen sendiri** dengan nilai yang berbeda

## 🔗 Referensi Materi Sebelumnya & Lanjutan

### Contoh Cara Menjalankan:

**Sebelumnya:**

- **Week 7**: String (Manipulasi Text)```bash

- **Week 8**: Sorting (Pengurutan Array)python prog9.py

````

**Week 9** ← **INI** (Manipulasi Array - Insert, Remove, Move)

---

**Selanjutnya:**

- **Week 10**: Perulangan dengan Array (Loop)## 💡 Contoh Kasus Nyata

### Preview Week 10:### 1. Manajemen Todo List

````python

# Contoh Week 10:```python

nama_teman = ["Andi", "Budi", "Cici", "Dodi"]# Todo list harian

tugas = ["Belajar", "Bermain", "Makan"]

# Loop untuk print semua nama

for nama in nama_teman:# Tambah tugas baru

    print(nama)tugas.append("Istirahat")



# Loop untuk manipulasi array# Insert tugas di tempat penting (index 1)

for i in range(len(nama_teman)):tugas.insert(1, "Minum")

    print(f"Nama ke-{i}: {nama_teman[i]}")

```# Hapus tugas yang sudah selesai

tugas.remove("Bermain")

---

print(tugas)  # Output: ['Belajar', 'Minum', 'Makan', 'Istirahat']

## 💪 Challenge Level Tinggi```



### Challenge 1: Manajemen Playlist Lagu### 2. Manajemen Urutan Bermain Game

Buat program yang:

1. Mulai dengan 3 lagu```python

2. Tambah 2 lagu baru# Urutan pemain

3. Hapus 1 lagupemain = ["Andi", "Budi", "Cici", "Dodi"]

4. Pindahkan lagu favorit ke posisi pertama

# Pindahkan Dodi ke giliran pertama

### Challenge 2: Manajemen Antrianorang = pemain.pop(3)

Buat program yang:pemain.insert(0, orang)

1. Mulai dengan antrian 5 orang

2. Orang baru datang, tambah ke akhirprint(pemain)  # Output: ['Dodi', 'Andi', 'Budi', 'Cici']

3. Orang pertama selesai, hapus```

4. Orang baru prioritas, masuk di urutan ke-2

### 3. Mengelola Inventori Toko

---

```python

## ❓ Troubleshooting - Error Yang Sering# Stok barang

barang = ["Pensil", "Penggaris", "Penghapus"]

### Error 1: `IndexError: list index out of range`

# Barang baru masuk

```pythonbarang.append("Buku")

❌ SALAH:

a = [1, 2, 3]# Stok lama dihapus (sudah terjual)

a.pop(5)  # Index 5 tidak ada!barang.pop(1)  # Hapus "Penggaris"



✅ BENAR:print(barang)

a = [1, 2, 3]```

a.pop(2)  # Index 0-2 ada

```---



### Error 2: `ValueError: list.remove(x): x not in list`## 📝 Perbedaan dengan Week 8



```python| Week 8                            | Week 9                                                  |

❌ SALAH:| --------------------------------- | ------------------------------------------------------- |

nama = ["Andi", "Budi", "Cici"]| **Sorting (Pengurutan)**          | **Manipulasi (Insert, Remove, Move)**                   |

nama.remove("Dodi")  # "Dodi" tidak ada!| Mengubah urutan berdasarkan nilai | Menambah, menghapus, memindahkan item                   |

| Contoh: `sorted()`, `.sort()`     | Contoh: `.append()`, `.insert()`, `.remove()`, `.pop()` |

✅ BENAR:| Lihat di: `Week 8/prog8.py`       | Lihat di: `Week 9/prog9.py`                             |

nama = ["Andi", "Budi", "Cici"]

nama.remove("Budi")  # "Budi" ada---

````

## 🎁 Pengembangan Lebih Lanjut

### Error 3: Lupa tanda kutip

Setelah menguasai manipulasi array, siswa dapat mempelajari:

```python

❌ SALAH:- 🔄 **Perulangan dengan Array**: Menggunakan `for` loop untuk manipulasi array

a = ["apel", "mangga", "jeruk"]- 🔍 **Pencarian Array**: Menggunakan `.index()` dan `.count()`

a.remove(mangga)  # Mangga tanpa tanda kutip!- 📊 **Array 2D (Multidimensi)**: Array dalam array

- 🗂️ **Dictionary dan List**: Struktur data yang lebih kompleks

✅ BENAR:- 💾 **File Handling**: Menyimpan array ke file

a = ["apel", "mangga", "jeruk"]

a.remove("mangga")  # "mangga" dengan tanda kutip---

```

---

_Ingat: Array adalah fondasi untuk struktur data yang lebih kompleks. Pastikan siswa benar-benar mengerti sebelum lanjut ke materi berikutnya!_
