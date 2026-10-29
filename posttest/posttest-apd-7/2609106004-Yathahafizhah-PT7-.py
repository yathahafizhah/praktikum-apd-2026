import os

# ==========================================
# VARIABEL GLOBAL
# ==========================================
users = {
    "admintuh": {"password": "admin17", "role": "admin"},
    "yatha": {"password": "123", "role": "user"}
}

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


# ==========================================
# PROSEDUR
# ==========================================
def bersihkan_layar():
    """Prosedur 1: Membersihkan tampilan terminal."""
    os.system('cls' if os.name == 'nt' else 'clear')


def tampilkan_header(judul):
    """Prosedur 2: Menampilkan header menu secara konsisten."""
    bersihkan_layar()
    print(f"{judul:^45}")


# ==========================================
# FUNGSI TANPA PARAMETER
# ==========================================
def hitung_total_pesanan():
    """Fungsi Tanpa Parameter 1: Menghitung total pesanan dalam dictionary global."""
    return len(orders)


def get_layanan_tersedia():
    """Fungsi Tanpa Parameter 2: Mengembalikan daftar pilihan layanan dasar."""
    return ["Cuci Kering", "Cuci Komplit", "Setrika Saja"]


# ==========================================
# FUNGSI DENGAN PARAMETER
# ==========================================
def cari_pesanan_by_id(id_pesanan):
    """Fungsi Dengan Parameter 1: Mencari data pesanan berdasarkan ID."""
    if id_pesanan in orders:
        return orders[id_pesanan]
    return None


def format_status(status_code):
    """Fungsi Dengan Parameter 2: Mengonversi kode angka ke teks status."""
    if status_code == 1:
        return "Proses"
    elif status_code == 2:
        return "Selesai"
    elif status_code == 3:
        return "Siap Diambil"
    else:
        return None


# ==========================================
# FUNGSI REKURSIF 
# ==========================================
def hitung_estimasi_waktu(jumlah_pesanan):
    """Fungsi Rekursif: Menghitung total jam estimasi berdasarkan antrean pesanan."""
    if jumlah_pesanan <= 0:
        return 0
    return 2 + hitung_estimasi_waktu(jumlah_pesanan - 1)


# ==========================================
# PROGRAM UTAMA 
# ==========================================
while app_running:
    tampilkan_header("APLIKASI PENCATATAN STATUS LAUNDRY")
    print("1. Login")
    print("2. Register (Akun Pengguna Baru)")
    print("3. Keluar Program")

    # Error Handling untuk Input Pilihan Utama
    try:
        pilihan_awal = int(input("Pilih menu (1-3): "))
        if pilihan_awal < 1 or pilihan_awal > 3:
            raise ValueError("Pilihan menu harus antara 1 sampai 3.")
    except ValueError as e:
        print(f"[Error Input]: {e}")
        input("Tekan Enter untuk melanjutkan...")
        continue

    # --------------------------------------
    # MENU 1: Login
    # --------------------------------------
    if pilihan_awal == 1:
        tampilkan_header("LOGIN SISTEM")
        username_input = input("Username : ").strip()
        password_input = input("Password : ").strip()

        # Error Handling Manual dengan Raise jika input kosong
        try:
            if not username_input or not password_input:
                raise ValueError("Username dan Password tidak boleh kosong!")
        except ValueError as err:
            print(f"[Login Gagal]: {err}")
            input("Tekan Enter untuk kembali...")
            continue

        login_berhasil = False
        role_login = ""
        nama_login = ""

        # Pengecekan Login 
        for u in users:
            if u == username_input and users[u]["password"] == password_input:
                login_berhasil = True
                role_login = users[u]["role"]
                nama_login = u
                break

        if login_berhasil:
            print(f"Login berhasil! Selamat datang, {nama_login} ({role_login.upper()}).")
            input("Tekan Enter untuk masuk ke menu...")

            session_active = True
            while session_active:
                # ----------------------------------
                # MENU ROLE ADMIN
                # ----------------------------------
                if role_login == "admin":
                    tampilkan_header(f"MENU ADMIN ({nama_login.upper()})")
                    print("1. Lihat Daftar Pesanan (Read)")
                    print("2. Tambah Pesanan Baru (Create)")
                    print("3. Ubah Status Pesanan (Update)")
                    print("4. Ambil/Hapus Pesanan (Delete)")
                    print("5. Logout")
    
                    try:
                        menu_admin = int(input("Pilih menu admin (1-5): "))
                    except ValueError:
                        print("[Error Input]: Masukkan angka menu yang valid!")
                        input("Tekan Enter untuk kembali...")
                        continue

                    # 1. Read (Admin)
                    if menu_admin == 1:
                        tampilkan_header("DAFTAR PESANAN LAUNDRY")
                        total = hitung_total_pesanan()
                        
                        if total == 0:
                            print("Belum ada pesanan laundry yang aktif.")
                        else:
                            print(f"Total Pesanan Aktif: {total} | Estimasi Selesai Semua: {hitung_estimasi_waktu(total)} Jam")
                            print(f"{'ID':<6} | {'Nama Pelanggan':<16} | {'Berat':<8} | {'Layanan':<15} | {'Status':<12}")
                            for id_o, info in orders.items():
                                print(f"{id_o:<6} | {info['nama_pelanggan']:<16} | {info['berat']:<8} | {info['layanan']:<15} | {info['status']:<12}")
                        input("\nTekan Enter untuk kembali ke menu...")

                    # 2. Create (Admin)
                    elif menu_admin == 2:
                        tampilkan_header("TAMBAH PESANAN BARU")
                        try:
                            id_baru = input("Masukkan ID Pesanan (contoh L003) : ").strip().upper()
                            nama_pelanggan = input("Masukkan Nama Pelanggan          : ").strip()
                            berat_input = int(input("Masukkan Berat Laundry (Kg)     : "))
                            
                            # Menampilkan Rekomendasi Layanan
                            print("\nPilihan Layanan Tersedia:")
                            layanan_list = get_layanan_tersedia()
                            for idx, lay in enumerate(layanan_list, 1):
                                print(f"{idx}. {lay}")
                            
                            pilihan_layanan = int(input("Pilih Jenis Layanan (1-3)       : "))
                            if pilihan_layanan < 1 or pilihan_layanan > len(layanan_list):
                                raise IndexError("Pilihan jenis layanan di luar jangkauan!")
                            
                            layanan = layanan_list[pilihan_layanan - 1]
                            status_awal = "Proses"

                            if not id_baru or not nama_pelanggan:
                                raise ValueError("ID dan Nama Pelanggan wajib diisi!")
                            
                            if id_baru in orders:
                                print("[Gagal]: ID Pesanan sudah terdaftar dalam sistem.")
                            else:
                                orders[id_baru] = {
                                    "nama_pelanggan": nama_pelanggan,
                                    "berat": f"{berat_input} kg",
                                    "layanan": layanan,
                                    "status": status_awal
                                }
                                print(f"[Sukses]: Pesanan {id_baru} berhasil ditambahkan!")

                        except ValueError as err:
                            print(f"[Error Input]: {err}")
                        except IndexError as err:
                            print(f"[Error Layanan]: {err}")
                        except Exception as e:
                            print(f"[Error Tak Terduga]: {e}")
                        finally:
                            input("Tekan Enter untuk kembali ke menu...")

                    # 3. UPDATE (Admin)
                    elif menu_admin == 3:
                        tampilkan_header("UBAH STATUS PESANAN")
                        if hitung_total_pesanan() == 0:
                            print("Belum ada pesanan aktif.")
                        else:
                            for id_o, info in orders.items():
                                print(f"ID: {id_o} | Nama: {info['nama_pelanggan']} | Status: {info['status']}")

                            cari_id = input("Masukkan ID Pesanan yang ingin diubah: ").strip().upper()
                            data_pesanan = cari_pesanan_by_id(cari_id)

                            if data_pesanan:
                                print(f"Data ditemukan: {data_pesanan['nama_pelanggan']} ({data_pesanan['status']})")
                                print("Pilihan Status Baru:1. Proses 2. Selesai 3. Siap Diambil")
                                
                                try:
                                    pilih_status = int(input("Pilihan status (1-3): "))
                                    status_baru = format_status(pilih_status)
                                    
                                    if status_baru:
                                        orders[cari_id]["status"] = status_baru
                                        print(f"[Sukses]: Status ID {cari_id} diperbarui menjadi '{status_baru}'.")
                                    else:
                                        print("[Gagal]: Opsi status tidak valid.")
                                except ValueError:
                                    print("[Error Input]: Harus memasukkan angka pilihan status!")
                            else:
                                print("[Error]: ID Pesanan tidak ditemukan.")
                        input("Tekan Enter untuk kembali ke menu...")

                    # 4. DELETE (Admin)
                    elif menu_admin == 4:
                        tampilkan_header("AMBIL / HAPUS PESANAN")
                        if hitung_total_pesanan() == 0:
                            print("Belum ada pesanan aktif.")
                        else:
                            for id_o, info in orders.items():
                                print(f"ID: {id_o} | Nama: {info['nama_pelanggan']} | Status: {info['status']}")
                            print("-" * 45)

                            cari_id = input("Masukkan ID Pesanan yang diambil: ").strip().upper()
                            
                            try:
                                if cari_id not in orders:
                                    raise KeyError(f"Pesanan dengan ID '{cari_id}' tidak ada.")
                                
                                del orders[cari_id]
                                print(f"[Sukses]: Data pesanan {cari_id} berhasil dihapus (laundry telah diambil).")
                            except KeyError as err:
                                print(f"[Error Data]: {err}")
                        input("\nTekan Enter untuk kembali ke menu...")

                    # 5. LOGOUT (Admin)
                    elif menu_admin == 5:
                        session_active = False

                    else:
                        print("Pilihan menu tidak valid.")
                        input("Tekan Enter untuk kembali...")

                # ----------------------------------
                # Menu Role Pelangggan User Biasa
                # ----------------------------------
                elif role_login == "user":
                    tampilkan_header(f"MENU PELANGGAN ({nama_login.upper()})")
                    print("1. Lihat Status Laundry")
                    print("2. Logout")
                    

                    try:
                        menu_user = int(input("Pilih menu (1-2): "))
                    except ValueError:
                        print("\n[Error Input]: Masukkan angka menu yang valid!")
                        input("Tekan Enter untuk kembali...")
                        continue

                    # 1. Read (Sebagai User)
                    if menu_user == 1:
                        tampilkan_header("STATUS ANTREAN LAUNDRY")
                        total = hitung_total_pesanan()
                        if total == 0:
                            print("Belum ada pesanan aktif.")
                        else:
                            print(f"{'ID':<6} | {'Nama Pelanggan':<16} | {'Berat':<8} | {'Layanan':<15} | {'Status':<12}")
                            for id_o, info in orders.items():
                                print(f"{id_o:<6} | {info['nama_pelanggan']:<16} | {info['berat']:<8} | {info['layanan']:<15} | {info['status']:<12}")
                        input("Tekan Enter untuk kembali...")
                    
                    # 2. Logout (User)
                    elif menu_user == 2:
                        session_active = False
                    
                    else:
                        print("Pilihan tidak valid.")
                        input("Tekan Enter untuk kembali...")

        else:
            print("[Login Gagal]: Username atau password salah.")
            input("Tekan Enter untuk kembali...")

    # --------------------------------------
    # MENU 2: Register
    # --------------------------------------
    elif pilihan_awal == 2:
        tampilkan_header("REGISTER AKUN PELANGGAN BARU")
        new_user = input("Buat Username : ").strip()
        new_pass = input("Buat Password : ").strip()

        try:
            if not new_user or not new_pass:
                raise ValueError("Username dan Password tidak boleh kosong.")
            
            if new_user in users:
                print("\n[Registrasi Gagal]: Username sudah digunakan orang lain.")
            else:
                users[new_user] = {"password": new_pass, "role": "user"}
                print(f"\n[Registrasi Berhasil]: Akun '{new_user}' berhasil dibuat! Silakan login.")
        except ValueError as err:
            print(f"[Error Registrasi]: {err}")
        finally:
            input("Tekan Enter untuk kembali ke menu...")

    # --------------------------------------
    # MENU 3: Keluar dari Program
    # --------------------------------------
    elif pilihan_awal == 3:
        tampilkan_header("TERIMA KASIH")
        print("Terima kasih telah menggunakan Sistem Pencatatan Laundry Kiloan!")
        app_running = False
