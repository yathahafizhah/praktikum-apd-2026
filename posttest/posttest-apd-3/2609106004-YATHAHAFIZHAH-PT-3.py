#SISTEM KASIR BIOSKOP

nama = input("Masukkan nama pembeli: ")
umur = int(input("Masukkan umur pembeli: "))
jenis_tiket = input("Masukkan jenis tiket (Reguler/Premium/VIP): ")
status_member = input("Apakah anda member? (Ya/Tidak): ")
uang_bayar = int(input("Masukkan nominal uang bayar: Rp "))

if umur < 13:
    print("Mohon maaf, anda belum cukup umur untuk menonton")
else:
    if jenis_tiket == "Reguler":
        harga_tiket = 50000
    elif jenis_tiket == "Premium":
        harga_tiket = 75000
    elif jenis_tiket == "VIP":
        harga_tiket = 100000
    else:
        print("Peringatan: Jenis tiket tidak valid.")
        harga_tiket = None

    
    if harga_tiket is not None:
        diskon_persen = 20 if status_member == "Ya" else 0
        nominal_diskon = harga_tiket * diskon_persen / 100
        biaya_admin = 0 if status_member == "Ya" else 2000
        total_bayar = harga_tiket - nominal_diskon + biaya_admin

        if uang_bayar < total_bayar:
            print("Peringatan: Uang bayar kurang.")
            print("Total yang harus dibayar: Rp", int(total_bayar))
        else:
            kembalian = uang_bayar - total_bayar

            print("\n========== STRUK BIOSKOP ==========")
            print("Nama Pembeli   :", nama)
            print("Umur           :", umur)
            print("Jenis Tiket    :", jenis_tiket)
            print("Status Member  :", status_member)
            print("Total Bayar    : Rp", int(total_bayar))
            print("Kembalian      : Rp", int(kembalian))
            print("===================================")