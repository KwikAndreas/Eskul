# Kunci Jawaban - Pengurutan Array

# SOAL 1: Urutkan array nilai ujian dari terkecil ke terbesar
nilai_ujian = [85, 92, 78, 95, 88, 73, 90]
print("=== SOAL 1 ===")
print("Nilai ujian sebelum diurutkan:", nilai_ujian)

nilai_ujian_ascending = sorted(nilai_ujian)
print("Nilai ujian dari terkecil ke terbesar:", nilai_ujian_ascending)
print("Nilai terendah:", min(nilai_ujian))
print("Nilai tertinggi:", max(nilai_ujian))
print()

# SOAL 2: Urutkan array tinggi badan dari terbesar ke terkecil
tinggi_badan = [165, 170, 158, 175, 162, 180, 155]
print("=== SOAL 2 ===")
print("Tinggi badan sebelum diurutkan:", tinggi_badan)

tinggi_badan_descending = sorted(tinggi_badan, reverse=True)
print("Tinggi badan dari terbesar ke terkecil:", tinggi_badan_descending)
print("Yang paling tinggi:", max(tinggi_badan), "cm")
print("Yang paling pendek:", min(tinggi_badan), "cm")
print()

# SOAL 3: Urutkan array nama buah secara alfabetis
buah = ["mangga", "apel", "jeruk", "pisang", "anggur"]
print("=== SOAL 3 ===")
print("Nama buah sebelum diurutkan:", buah)

buah_alfabetis = sorted(buah)
print("Nama buah secara alfabetis:", buah_alfabetis)
print("Buah pertama secara alfabetis:", buah_alfabetis[0])
print("Buah terakhir secara alfabetis:", buah_alfabetis[-1])
print()

# SOAL 4: Urutkan array umur dari yang tertua ke termuda
umur_siswa = [13, 15, 14, 13, 16, 14, 15]
print("=== SOAL 4 ===")
print("Umur siswa sebelum diurutkan:", umur_siswa)

umur_siswa_descending = sorted(umur_siswa, reverse=True)
print("Umur siswa dari tertua ke termuda:", umur_siswa_descending)
print("Siswa tertua:", max(umur_siswa), "tahun")
print("Siswa termuda:", min(umur_siswa), "tahun")
print()

# BONUS: Coba gunakan metode .sort() untuk mengubah array asli
print("=== BONUS ===")
angka_bonus = [7, 2, 9, 1, 5, 8, 3]
print("Array bonus sebelum:", angka_bonus)

angka_bonus.sort()
print("Array bonus setelah .sort():", angka_bonus)

# Demonstrasi perbedaan sorted() vs .sort()
print("\n=== DEMONSTRASI PERBEDAAN ===")
data_asli = [10, 5, 8, 3, 7]
print("Data asli:", data_asli)

# Menggunakan sorted() - tidak mengubah array asli
data_sorted = sorted(data_asli)
print("Setelah sorted():")
print("  data_asli:", data_asli)  # Masih sama
print("  data_sorted:", data_sorted)  # Yang baru

# Menggunakan .sort() - mengubah array asli
data_asli.sort()
print("Setelah .sort():")
print("  data_asli:", data_asli)  # Sudah berubah

print("\n=== ANALISIS DATA ===")
# Contoh analisis sederhana
nilai_ujian = [85, 92, 78, 95, 88, 73, 90]
nilai_terurut = sorted(nilai_ujian)

print("Statistik Nilai Ujian:")
print(f"Jumlah siswa: {len(nilai_ujian)}")
print(f"Nilai tertinggi: {max(nilai_ujian)}")
print(f"Nilai terendah: {min(nilai_ujian)}")
print(f"Rata-rata: {sum(nilai_ujian)/len(nilai_ujian):.1f}")
print(f"Nilai tengah (median): {nilai_terurut[len(nilai_terurut)//2]}")

# Kategorisasi nilai
nilai_tinggi = [n for n in nilai_ujian if n >= 90]
nilai_sedang = [n for n in nilai_ujian if 80 <= n < 90]
nilai_rendah = [n for n in nilai_ujian if n < 80]

print(f"\nKategorisasi:")
print(f"Nilai tinggi (>=90): {len(nilai_tinggi)} siswa -> {nilai_tinggi}")
print(f"Nilai sedang (80-89): {len(nilai_sedang)} siswa -> {nilai_sedang}")
print(f"Nilai rendah (<80): {len(nilai_rendah)} siswa -> {nilai_rendah}")