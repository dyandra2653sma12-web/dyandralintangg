print("== PROGRAM HITUNG GAJI ===")

nama = input("Masukkan Nama: ")
gaji_pokok = float(input("Masukkan Gaji Pokok: "))

tunjangan = 0.20 * gaji_pokok
pajak = 0.15 * (gaji_pokok + tunjangan)
gaji_bersih = gaji_pokok + tunjangan - pajak 

print("\n=== HASIL ===")
print("nama:", nama)
print("Gaji Pokok:", gaji pokok)
print("Tunjangan:", tunjangan)
print("Pajak:", pajak)
print("Gaji Bersih:", gaji_bersih)