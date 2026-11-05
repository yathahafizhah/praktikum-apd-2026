from data import users
from transisi import clear_screen, pause

def login():
    clear_screen()
    print("=== LOGIN SISTEM LAUNDRY ===")
    username = input("Username : ").strip()
    password = input("Password : ").strip()

    if username in users and users[username]["password"] == password:
        print(f"Login berhasil! Selamat datang, {username}.")
        pause()
        return True, username, users[username]["role"]
    else:
        print("Username atau password salah!")
        pause()
        return False, None, None

def register():
    clear_screen()
    print("=== REGISTRASI AKUN PELANGGAN BARU ===")
    username = input("Masukkan Username Baru : ").strip()
    password = input("Masukkan Password Baru : ").strip()

    if not username or not password:
        print("\nUsername dan password tidak boleh kosong!")
        pause()
        return

    if username in users:
        print("\nUsername sudah terdaftar! Gunakan username lain.")
        pause()
        return

    users[username] = {"password": password, "role": "customer"}
    print(f"\nAkun '{username}' berhasil didaftarkan sebagai Pelanggan!")
    pause()