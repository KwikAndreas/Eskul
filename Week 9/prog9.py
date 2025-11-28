# ====================================================================
# MANIPULASI ARRAY - Week 9
# Nama: _______________
# Kelas: ______________

print("="*70)
print(" "*20 + "BELAJAR MANIPULASI ARRAY - Week 9")
print("="*70)
print()

# ==================== LATIHAN SOAL ====================
print("\n" + "="*70)
print(" "*25 + "LATIHAN SOAL")
print("="*70 + "\n")

# ===== LATIHAN SOAL 1: TAMBAH ITEM DENGAN .append() =====
print("📌 LATIHAN SOAL 1: TAMBAH ITEM DI AKHIR DENGAN .append()")
print("-"*70)

buah = ["apel", "mangga", "jeruk"]
print(f"📍 Array awal:    {buah}")
print(f"📊 Jumlah item:   {len(buah)}")
print()

print("📝 Tulis kode untuk menambahkan 'pisang' di akhir:")
print("   Gunakan: buah.append('pisang')")
print()

# Tulis jawaban Anda di sini:
# buah.append("pisang")
# print(f"✅ Array setelah:  {buah}")
# print(f"📊 Jumlah item:    {len(buah)}")

print()

# ===== LATIHAN SOAL 2: TAMBAH ITEM DENGAN .insert() =====
print("📌 LATIHAN SOAL 2: TAMBAH ITEM DI POSISI TERTENTU DENGAN .insert()")
print("-"*70)

warna = ["merah", "biru", "hijau"]
print(f"📍 Array awal:    {warna}")
print(f"   Index 0='merah', Index 1='biru', Index 2='hijau'")
print()

print("📝 Tulis kode untuk menambahkan 'kuning' di posisi index 1:")
print("   Gunakan: warna.insert(1, 'kuning')")
print()

# Tulis jawaban Anda di sini:
# warna.insert(1, "kuning")
# print(f"✅ Array setelah:  {warna}")

print()

# ===== LATIHAN SOAL 3: HAPUS DENGAN .remove() =====
print("📌 LATIHAN SOAL 3: HAPUS BERDASARKAN NILAI DENGAN .remove()")
print("-"*70)

hewan = ["sapi", "kucing", "anjing", "burung", "ikan"]
print(f"📍 Array awal:    {hewan}")
print()

print("📝 Tulis kode untuk menghapus 'kucing':")
print("   Gunakan: hewan.remove('kucing')")
print()

# Tulis jawaban Anda di sini:
# hewan.remove("kucing")
# print(f"✅ Array setelah:  {hewan}")

print()

# ===== LATIHAN SOAL 4: HAPUS DENGAN .pop() =====
print("📌 LATIHAN SOAL 4: HAPUS BERDASARKAN POSISI DENGAN .pop()")
print("-"*70)

angka = [10, 20, 30, 40, 50]
print(f"📍 Array awal:    {angka}")
print(f"   Index 0=10, Index 1=20, Index 2=30, Index 3=40, Index 4=50")
print()

print("📝 Tulis kode untuk menghapus item di index 2 (nilai 30):")
print("   Gunakan: item_dihapus = angka.pop(2)")
print()

# Tulis jawaban Anda di sini:
# item_dihapus = angka.pop(2)
# print(f"✅ Item yang dihapus: {item_dihapus}")
# print(f"✅ Array setelah:     {angka}")

print()

# ===== LATIHAN SOAL 5: PINDAHKAN ITEM =====
print("📌 LATIHAN SOAL 5: PINDAHKAN ITEM DENGAN .pop() + .append()")
print("-"*70)

antrian = ["Ali", "Bina", "Citra", "Dini", "Eka"]
print(f"📍 Array awal:    {antrian}")
print(f"   Citra ada di index 2")
print()

print("📝 Tulis kode untuk memindahkan 'Citra' ke posisi akhir:")
print("   Langkah 1: item = antrian.pop(2)  # Ambil dari posisi 2")
print("   Langkah 2: antrian.append(item)   # Letakkan di akhir")
print()

# Tulis jawaban Anda di sini:
# item = antrian.pop(2)
# antrian.append(item)
# print(f"✅ Array setelah:  {antrian}")

print()
print()


# ==================== TUGAS MANDIRI ====================
print("="*70)
print(" "*22 + "TUGAS MANDIRI (5 NOMOR)")
print("="*70 + "\n")

print("Selesaikan 5 soal di bawah ini dengan BAIK dan BENAR!\n")

# ===== TUGAS 1 =====
print("📋 TUGAS 1: Manajemen Daftar Siswa Aktif")
print("-"*70)

print("""
Anda diminta membuat program untuk mengelola daftar siswa yang aktif 
di klub pemrograman.

Kondisi Awal:
- Daftar siswa: ["Andi", "Budi", "Cici", "Dodi"]
- Sebagai anggota baru, Eka ingin bergabung (tambah di akhir)
- Fani ingin bergabung dengan prioritas (masuk di posisi ke-2)
- Budi tidak bisa lagi (hapus dari list)
- Pindahkan Dodi ke urutan pertama

Tugas:
1. Buat array siswa dengan kondisi awal
2. Tambahkan Eka di akhir dengan .append()
3. Masukkan Fani di posisi index 1 dengan .insert()
4. Hapus Budi dengan .remove()
5. Pindahkan Dodi ke posisi awal
6. Tampilkan daftar akhir dengan format yang rapi

Output yang diharapkan:
=== DAFTAR SISWA AKTIF KLUB PEMROGRAMAN ===
1. Dodi
2. Andi
3. Fani
4. Cici
5. Eka
==================================
Total Siswa Aktif: 5 orang
""")

print("💻 Tulis kode Anda di bawah ini:\n")
# Tulis kode Anda di sini:


print("\n")

# ===== TUGAS 2 =====
print("� TUGAS 2: Manajemen Belanja Online")
print("-"*70)

print("""
Anda diminta membuat program untuk mengelola keranjang belanja online.

Kondisi Awal:
- Keranjang: ["Buku", "Pensil", "Penggaris", "Penghapus"]

Tugas:
1. Buat array keranjang dengan kondisi awal
2. Tambahkan "Penggaris" yang terlupakan (harus ada di posisi ke-2)
   Gunakan .insert()
3. Hapus "Penggaris" yang asli (di posisi index 2) karena out of stock
   Gunakan .pop()
4. Tambahkan "Tas" di akhir dengan .append()
5. Pindahkan "Buku" (yang paling berat) ke akhir untuk diambil terakhir
6. Tampilkan hasil akhir dengan penomoran

Output yang diharapkan:
=== DAFTAR BELANJA ANDA ===
1. Pensil
2. Penghapus
3. Tas
4. Buku
========================
Total Item: 4 barang
""")

print("💻 Tulis kode Anda di bawah ini:\n")
# Tulis kode Anda di sini:


print("\n")

# ===== TUGAS 3 =====
print("� TUGAS 3: Manajemen Antrian Pemain Game")
print("-"*70)

print("""
Di sebuah warnet, ada antrian pemain untuk menggunakan komputer gaming.

Kondisi Awal:
- Antrian: ["Rido", "Sinta", "Tommy", "Umi", "Vino"]

Peristiwa:
1. Rido selesai bermain (main terlebih dahulu, jadi di index 0)
2. Wawan datang dan harus antri di akhir
3. Umi mau duluan karena sudah lama menunggu (pindah ke posisi awal)
4. Sinta pindah dari posisi 1 ke posisi akhir

Tugas:
1. Buat array antrian dengan kondisi awal
2. Hapus Rido dengan .pop(0) karena selesai
3. Tambahkan Wawan di akhir dengan .append()
4. Pindahkan Umi (cari posisinya dulu) ke awal dengan kombinasi
5. Pindahkan Sinta ke akhir dengan kombinasi .pop() dan .append()
6. Tampilkan urutan akhir dengan penomoran

Output yang diharapkan:
=== ANTRIAN PEMAIN GAMING ===
Urutan Pemain:
1. Umi
2. Tommy
3. Vino
4. Wawan
5. Sinta
========================
Total Pemain: 5 orang
""")

print("💻 Tulis kode Anda di bawah ini:\n")
# Tulis kode Anda di sini:


print("\n")

# ===== TUGAS 4 =====
print("📋 TUGAS 4: Manajemen Playlist Musik Favorit")
print("-"*70)

print("""
Anda memiliki playlist musik favorit yang ingin diatur ulang.

Kondisi Awal:
- Playlist: ["Lagu Pop", "Lagu Rock", "Lagu Jazz", "Lagu K-Pop"]

Tugas:
1. Buat array playlist dengan kondisi awal
2. Tambahkan "Lagu Dangdut" di posisi ke-2 dengan .insert()
3. Hapus "Lagu Jazz" (tidak mood) dengan .remove()
4. "Lagu Pop" adalah favorit, pindahkan ke posisi awal
5. "Lagu K-Pop" pindahkan ke posisi akhir
6. Tambahkan "Lagu Indie" di akhir dengan .append()
7. Tampilkan playlist akhir dengan penomoran

Output yang diharapkan:
=== PLAYLIST MUSIK FAVORIT ===
1. Lagu Pop
2. Lagu Rock
3. Lagu Dangdut
4. Lagu Indie
5. Lagu K-Pop
=======================
Total Lagu: 5 buah

Catatan Lagu:
- "Lagu Pop" adalah favorit utama
- "Lagu K-Pop" untuk dengarkan di akhir
""")

print("💻 Tulis kode Anda di bawah ini:\n")
# Tulis kode Anda di sini:


print("\n")

# ===== TUGAS 5 =====
print("� TUGAS 5: Manajemen Urutan Presentasi Siswa")
print("-"*70)

print("""
Guru meminta siswa membuat urutan presentasi yang baru berdasarkan 
urutan berikut:

Kondisi Awal (urutan sesuai absen):
- Presentasi: ["Aldi", "Bella", "Citra", "Dimas", "Erlina", "Fani"]

Perubahan yang diminta:
1. Fani dipindahkan ke posisi pertama (karena siap paling awal)
2. Erlina ditarik dari urutan karena sakit (hapus)
3. Gita ingin join presentasi (tambah di akhir)
4. Hendro mendapat giliran lebih awal (tambah di posisi ke-2)
5. Bella pindah ke urutan terakhir (karena sudah berpengalaman)

Tugas:
1. Buat array presentasi dengan kondisi awal
2. Pindahkan Fani (index 5) ke posisi awal dengan kombinasi
3. Hapus Erlina dengan .remove()
4. Tambahkan Gita di akhir dengan .append()
5. Masukkan Hendro di posisi index 1 dengan .insert()
6. Pindahkan Bella (cari posisinya) ke akhir
7. Tampilkan urutan presentasi akhir dengan penomoran lengkap

Output yang diharapkan:
=== URUTAN PRESENTASI KELAS ===
NO  NAMA SISWA
-----------
1.  Fani
2.  Hendro
3.  Aldi
4.  Citra
5.  Dimas
6.  Gita
7.  Bella
-----------
Total Presentasi: 7 siswa

Catatan:
- Fani dimulai paling awal
- Bella menutup presentasi
""")

print("💻 Tulis kode Anda di bawah ini:\n")
# Tulis kode Anda di sini:


print("\n\n")
print("="*70)
print(" "*15 + "✅ SELESAI MENGERJAKAN SOAL DAN TUGAS!")
print(" "*10 + "Pastikan semua outputnya benar sebelum submit ke guru")
print("="*70)
