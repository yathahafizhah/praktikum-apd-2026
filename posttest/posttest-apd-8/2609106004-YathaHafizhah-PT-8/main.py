from auth import login, register
from admin import menu_admin
from pengguna import menu_pengguna
from transisi import clear_screen, pause

def main():
    app_running = True
    while app_running:
        clear_screen()
        print("==========================================")
        print("  APLIKASI PENCATATAN STATUS LAUNDRY KILOAN")
        print("==========================================")
        print("1. Login Sistem")
        print("2. Registrasi Akun Pelanggan Baru")
        print("3. Keluar dari Aplikasi")
        print("------------------------------------------")
        pilihan_awal = input("Pilih Menu (1-3): ").strip()

        if pilihan_awal == "1":
            is_logged_in, username, role = login()
            if is_logged_in:
                if role == "admin":
                    menu_admin()
                elif role == "customer":
                    menu_pengguna(username)
        elif pilihan_awal == "2":
            register()
        elif pilihan_awal == "3":
            clear_screen()
            print("Terima kasih telah menggunakan aplikasi ini!")
            app_running = False
        else:
            print("Pilihan tidak valid! Masukkan angka 1, 2, atau 3.")
            pause()

if __name__ == "__main__":
    main()