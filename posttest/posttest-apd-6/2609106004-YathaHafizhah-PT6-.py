import os

# Data users (Key: Username, Value: Dictionary)
users = {
    "admintuh": {"password": "admin17", "role": "admin"},
    "yatha": {"password": "123", "role": "user"}
}

# Data orders (Key: ID Pesanan, Value: Dictionary detail pesanan)
orders = {
    "L001": {
        "nama_pelanggan": "anna", 
        "berat": "3 kg", 
        "layanan": "Cuci Kering", 
        "status": "Proses"
    },
    "L002": {
        "nama_pelanggan": "al", 
        "berat": "5 kg", 
        "layanan": "Setrika Saja", 
        "status": "Siap Diambil"
    }
}

app_running = True

while app_running:
    os.system('cls' if os.name == 'nt' else 'clear')
    print("APLIKASI SISTEM PENCATATAN STATUS LAUNDRY")
    print("1. Login")
    print("2. Register (Akun Pengguna Baru)")
    print("3. Keluar Program")

    pilihan_awal = int(input("Pilih menu (1-3): "))

    if pilihan_awal == 1:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("LOGIN")
        username_input = input("Username : ")
        password_input = input("Password : ")

        login_berhasil = False
        role_login = ""
        nama_login = ""

        # Pengecekan login 
        for u in users:
            if u == username_input and users[u]["password"] == password_input:
                login_berhasil = True
                role_login = users[u]["role"]
                nama_login = u
                break

        if login_berhasil:
            print(f"Login berhasil! Selamat datang, {nama_login} ({role_login}).")
            input("Tekan Enter untuk masuk ke menu...")

            session_active = True
            while session_active:
                os.system('cls' if os.name == 'nt' else 'clear')

                # Menu Admin
                if role_login == "admin":
                    print(f"MENU ADMIN ({nama_login})")
                    print("1. Lihat Daftar Pesanan (Read)")
                    print("2. Tambah Pesanan Baru (Create)")
                    print("3. Ubah Status Pesanan (Update)")
                    print("4. Ambil/Hapus Pesanan (Delete)")
                    print("5. Logout")

                    menu_admin = int(input("Pilih menu admin (1-5): "))

                    # 1. Daftar Pesanan Laundry (Read)
                    if menu_admin == 1:
                        os.system('cls' if os.name == 'nt' else 'clear')
                        print("DAFTAR PESANAN LAUNDRY")
                        if len(orders) == 0:
                            print("Belum ada pesanan laundry yang aktif.")
                        else:
                            print("ID   | Nama Pelanggan | Berat | Layanan | Status")
                            for id_o, info in orders.items():
                                print(f"{id_o} | {info['nama_pelanggan']}        | {info['berat']} | {info['layanan']}   | {info['status']}")
                        input("Tekan Enter untuk kembali ke menu...")

                    # 2. Tambah Pesanan Baru (Create)
                    elif menu_admin == 2:
                        os.system('cls' if os.name == 'nt' else 'clear')
                        print("TAMBAH PESANAN BARU")
                        id_baru = input("Masukkan ID Pesanan (contoh L003) : ")
                        nama_pelanggan = input("Masukkan Nama Pelanggan          : ")
                        berat_laundry = input("Masukkan Berat (misal: 4 kg)     : ")
                        layanan = input("Masukkan Jenis Layanan           : ")
                        status_awal = "Proses"

                        if id_baru != "" and nama_pelanggan != "" and berat_laundry != "" and layanan != "":
                            if id_baru in orders:
                                print("Gagal! ID Pesanan sudah terdaftar.")
                            else:
                                orders[id_baru] = {
                                    "nama_pelanggan": nama_pelanggan,
                                    "berat": berat_laundry,
                                    "layanan": layanan,
                                    "status": status_awal
                                }
                                print("Pesanan baru berhasil ditambahkan ke antrean!")
                        else:
                            print("Gagal! Semua kolom data wajib diisi.")
                        input("Tekan Enter untuk kembali ke menu...")

                    # 3. Ubah Status Pesanan (Update)
                    elif menu_admin == 3:
                        os.system('cls' if os.name == 'nt' else 'clear')
                        print("UBAH STATUS PESANAN")
                        print("-" * 25)
                        if len(orders) == 0:
                            print("Belum ada pesanan.")
                        else:
                            print("Daftar Pesanan Saat Ini:")
                            for id_o, info in orders.items():
                                print(f"ID: {id_o} | Nama: {info['nama_pelanggan']} | Status: {info['status']}")
                            print("-" * 35)

                            cari_id = input("Masukkan ID Pesanan yang ingin diubah statusnya: ")
                            if cari_id in orders:
                                print("Pilih Status Baru:")
                                print("1. Proses")
                                print("2. Selesai")
                                print("3. Siap Diambil")
                                pilih_status = int(input("Pilihan status (1-3): "))

                                if pilih_status == 1:
                                    orders[cari_id]["status"] = "Proses"
                                    print("Status berhasil diubah menjadi 'Proses'.")
                                elif pilih_status == 2:
                                    orders[cari_id]["status"] = "Selesai"
                                    print("Status berhasil diubah menjadi 'Selesai'.")
                                elif pilih_status == 3:
                                    orders[cari_id]["status"] = "Siap Diambil"
                                    print("Status berhasil diubah menjadi 'Siap Diambil'.")
                                else:
                                    print("Pilihan status tidak valid.")
                            else:
                                print("ID Pesanan tidak ditemukan.")
                        input("Tekan Enter untuk kembali ke menu...")

                    # 4. Ambil / Hapus Pesanan (Delete)
                    elif menu_admin == 4:
                        os.system('cls' if os.name == 'nt' else 'clear')
                        print("AMBIL / HAPUS PESANAN")
                        if len(orders) == 0:
                            print("Belum ada pesanan.")
                        else:
                            print("Daftar Pesanan Saat Ini:")
                            for id_o, info in orders.items():
                                print(f"ID: {id_o} | Nama: {info['nama_pelanggan']} | Status: {info['status']}")

                            cari_id = input("Masukkan ID Pesanan yang diambil/dibayar pelanggan: ")
                            if cari_id in orders:
                                del orders[cari_id]
                                print("\nData pesanan berhasil dihapus dari antrean (Laundry telah diambil)!")
                            else:
                                print("\nID Pesanan tidak ditemukan.")
                        input("\nTekan Enter untuk kembali ke menu...")

                    elif menu_admin == 5:
                        session_active = False
                    else:
                        print("\nPilihan menu tidak valid.")
                        input("Tekan Enter untuk kembali...")

                # Menu Pelanggan (User)
                elif role_login == "user":
                    print(f"MENU PELANGGAN ({nama_login})")
                    print("1. Lihat Status Laundry")
                    print("2. Logout")

                    menu_user = int(input("Pilih menu (1-2): "))

                    if menu_user == 1:
                        os.system('cls' if os.name == 'nt' else 'clear')
                        print("STATUS ANTREAN LAUNDRY")
                        if len(orders) == 0:
                            print("Belum ada pesanan aktif.")
                        else:
                            print("ID   | Nama Pelanggan | Berat | Layanan      | Status")
                            for id_o, info in orders.items():
                                print(f"{id_o} | {info['nama_pelanggan']}        | {info['berat']} | {info['layanan']}   | {info['status']}")
                        input("Tekan Enter untuk kembali...")
                    elif menu_user == 2:
                        session_active = False
                    else:
                        print("Pilihan tidak valid.")
                        input("Tekan Enter untuk kembali...")

        else:
            print("Login Gagal! Username atau password salah.")
            input("Tekan Enter untuk kembali...")

    elif pilihan_awal == 2:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("REGISTER AKUN PELANGGAN BARU")
        new_user = input("Buat Username : ")
        new_pass = input("Buat Password : ")

        if new_user in users:
            print("Registrasi Gagal! Username sudah digunakan orang lain.")
        elif new_user == "" or new_pass == "":
            print("Registrasi Gagal! Username dan password tidak boleh kosong.")
        else:
            users[new_user] = {"password": new_pass, "role": "user"}
            print("Registrasi berhasil! Silakan login dengan akun baru Anda.")
        input("Tekan Enter untuk kembali ke menu...")

    elif pilihan_awal == 3:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Terima kasih telah menggunakan Sistem Pencatatan Laundry Kiloan!")
        app_running = False
    else:
        print("Pilihan tidak valid.")
        input("Tekan Enter untuk kembali...")
