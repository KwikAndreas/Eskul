# ========================================
# Nama  : _______________
# Kelas : _______________
# ========================================

print("="*50)
print("  LATIHAN LOOP - Week 10")
print("="*50)
print()

# ========================================
# LATIHAN 1: Loop Dasar - Print Angka 1-10
# ========================================
print("LATIHAN 1: Print angka 1 sampai 10")
print("-" * 40)

# Cara 1: Menggunakan range()
# TODO: Hapus tanda # untuk menjalankan
# for i in range(1, 11):
#     print(i)

print()

# ========================================
# LATIHAN 2: Loop Array - Print Semua Nama
# ========================================
print("LATIHAN 2: Print semua nama siswa dengan nomor urut")
print("-" * 40)

siswa = ["Andi", "Budi", "Cici", "Dodi", "Eka"]

# TODO: Loop untuk print nama dengan nomor
# Contoh output:
# 1. Andi
# 2. Budi
# dst...

# for i in range(len(siswa)):
#     print(f"{i+1}. {siswa[i]}")

print()

# ========================================
# LATIHAN 3: Hitung Total - Jumlahkan Semua Nilai
# ========================================
print("LATIHAN 3: Hitung total dan rata-rata nilai")
print("-" * 40)

nilai_ujian = [85, 90, 78, 92, 88]

# TODO: Hitung total nilai
# total = 0
# for nilai in nilai_ujian:
#     total = total + nilai

# TODO: Hitung rata-rata
# rata_rata = total / len(nilai_ujian)

# print(f"Total nilai: {total}")
# print(f"Rata-rata: {rata_rata}")

print()

# ========================================
# LATIHAN 4: Filter Data - Tampilkan yang Lulus
# ========================================
print("LATIHAN 4: Tampilkan nilai yang LULUS (≥75)")
print("-" * 40)

nilai_kelas = [85, 65, 78, 92, 70, 88, 55, 95]

# TODO: Print hanya nilai yang >= 75
# print("Nilai yang LULUS:")
# for n in nilai_kelas:
#     if n >= 75:
#         print(f"✓ {n} - LULUS")

print()

# ========================================
# LATIHAN 5: Input Berulang - Tambah Item ke Array
# ========================================
print("LATIHAN 5: Input 3 nama buah favorit")
print("-" * 40)

daftar_buah = []

# TODO: Loop untuk input 3 buah
# for i in range(3):
#     buah = input(f"Buah ke-{i+1}: ")
#     daftar_buah.append(buah)

# TODO: Print semua buah yang sudah diinput
# print("\n🍎 Buah favorit Anda:")
# for buah in daftar_buah:
#     print(f"• {buah}")

print()

# ========================================
# BONUS 1: While Loop - Countdown
# ========================================
print("BONUS 1: Countdown dari 5")
print("-" * 40)

# TODO: Buat countdown dari 5 ke 1
# hitung = 5
# while hitung > 0:
#     print(f"Countdown: {hitung}")
#     hitung -= 1
# print("🚀 Start!")

print()

# ========================================
# BONUS 2: Cari Nilai Tertinggi dengan Loop
# ========================================
print("BONUS 2: Cari nilai tertinggi")
print("-" * 40)

angka = [45, 78, 92, 34, 88, 56, 99, 67]

# TODO: Cari nilai tertinggi
# tertinggi = angka[0]
# for num in angka:
#     if num > tertinggi:
#         tertinggi = num

# print(f"Nilai tertinggi: {tertinggi}")

print()

# ========================================
# BONUS 3: Hitung Kemunculan Item
# ========================================
print("BONUS 3: Hitung berapa kali 'apel' muncul")
print("-" * 40)

keranjang = ["apel", "mangga", "apel", "jeruk", "apel", "pisang"]

# TODO: Hitung berapa kali "apel" muncul
# jumlah_apel = 0
# for item in keranjang:
#     if item == "apel":
#         jumlah_apel += 1

# print(f"Jumlah apel: {jumlah_apel}")

print()

# ========================================
# CHALLENGE: Mini Program Kasir Sederhana
# ========================================
print("="*50)
print("  CHALLENGE: Mini Program Kasir")
print("="*50)
print()

"""
INSTRUKSI CHALLENGE:
Buat program kasir sederhana dengan fitur:
1. Loop untuk input maksimal 5 barang
2. Setiap barang punya nama dan harga
3. Hitung total belanja
4. Jika total > 100.000, dapat diskon 10%
5. Tampilkan struk belanja

Tips:
- Gunakan 2 array: satu untuk nama barang, satu untuk harga
- Gunakan for loop untuk input
- Gunakan for loop untuk hitung total
- Gunakan if untuk diskon
"""

# TODO: Tulis kode challenge di sini
# daftar_barang = []
# daftar_harga = []

# print("Masukkan maksimal 5 barang belanjaan:")
# for i in range(5):
#     nama = input(f"\nBarang ke-{i+1} (atau ketik 'selesai' untuk berhenti): ")
#     if nama.lower() == 'selesai':
#         break
#     harga = int(input(f"Harga {nama}: Rp "))
#     daftar_barang.append(nama)
#     daftar_harga.append(harga)

# # Hitung total
# total = 0
# for harga in daftar_harga:
#     total += harga

# # Cek diskon
# diskon = 0
# if total > 100000:
#     diskon = total * 0.1

# total_bayar = total - diskon

# # Print struk
# print("\n" + "="*40)
# print("         STRUK BELANJA")
# print("="*40)
# for i in range(len(daftar_barang)):
#     print(f"{i+1}. {daftar_barang[i]:<20} Rp {daftar_harga[i]:>10,}")
# print("-"*40)
# print(f"{'Subtotal':<20} Rp {total:>10,}")
# if diskon > 0:
#     print(f"{'Diskon 10%':<20} Rp {diskon:>10,}")
# print("="*40)
# print(f"{'TOTAL BAYAR':<20} Rp {total_bayar:>10,}")
# print("="*40)

print()
print("="*50)
print("  🎉 SELAMAT! Anda sudah menyelesaikan")
print("     Week 10 - Loop dengan Array!")
print("  🎊 Sampai jumpa tahun depan!")
print("="*50)
