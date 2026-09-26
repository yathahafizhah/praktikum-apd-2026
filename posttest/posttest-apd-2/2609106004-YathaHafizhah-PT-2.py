# Tugas Posttest 2 APD
barang = [15000, 25000, 10000, 5500, 5000, 20000]
print("Barang 1, 3, dan 5:", barang[0:5:2])
total_belanja = barang[0] + barang[1] + barang[2] + barang[3] + barang[4] + barang[5]
pajak = total_belanja * 0.15
total_bayar = total_belanja + pajak
total_usd = total_bayar / 15500
total_eur = total_bayar / 17000
rata_rata = total_bayar / len(barang)
nim = 4
bolean = nim < rata_rata
print("Daftar Harga Barang :", barang)
print("Total Belanja       :", total_belanja)
print("Pajak (15%)         :", pajak)
print("Total Bayar         :", total_bayar)
print("Total Bayar (USD)   :", total_usd)
print("Total Bayar (EUR)   :", total_eur)
print("Rata-Rata           :", rata_rata)
print("NIM                 :", nim)
print("Hasil Bolean        :", bolean)