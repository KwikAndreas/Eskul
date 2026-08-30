nama = input("Masukkan nama pembeli: ")
total = int(input("Masukkan total belanja: Rp "))

if total > 100000:
    diskon = 0.10
elif total >= 50000:
    diskon = 0.05
else:
    diskon = 0

potongan = total * diskon
bayar = total - potongan

print("\n=== Struk Pembayaran ===")
print("Nama Pembeli :", nama)
print("Total Belanja: Rp", total)
print("Diskon       :", int(diskon * 100), "%")
print("Total Bayar  : Rp", int(bayar))
