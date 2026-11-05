from data import orders
from tabel import cetak_tabel_orders
from transisi import clear_screen, pause

def menu_pengguna(username):
    while True:
        clear_screen()
        print(f"=== MENU PELANGGAN ({username.upper()}) ===")
        print("1. Lihat Status Pesanan Saya")
        print("2. Logout")
        pilihan = input("Pilih menu (1/2): ").strip()

        if pilihan == "1":
            clear_screen()
            print(f"=== DAFTAR PESANAN PELANGGAN ({username}) ===")
            #Menampilkan Pelanggan yg Sedang Loginn
            user_orders = {k: v for k, v in orders.items() if v["nama"].lower() == username.lower()}
            cetak_tabel_orders(user_orders)
            pause()
        elif pilihan == "2":
            print("Logout berhasil.")
            pause()
            break
        else:
            print("Pilihan tidak valid!")
            pause()