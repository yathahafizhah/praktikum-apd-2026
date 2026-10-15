#Program Menghitung Laundry Kiloan

users = [
    ["admintuh", "admin17", "admin"],
    ["yatha", "123", "user"],
]

#Ini untuk Format Order [[id_pesanan, nama_pelanggan, berat, jenis_layanan, status], ...]
orders = [
    ["L001", "anna", "3 kg", "Cuci Kering", "Proses"],
    ["L002", "al", "5 kg", "Setrika Saja", "Siap Diambil"],
]

app_running = True

while app_running:
  print("APLIKASI SISTEM PENCATATAN STATUS LAUNDRY")
  print("1. Login")
  print("2. Register (Akun Pengguna Baru)")
  print("3. Keluar Program")

  pilihan_awal = int(input("Pilih menu (1-3): "))

  if pilihan_awal == 1:
    #Buat Login
    print("LOGIN")
    username_input = input("Username : ")
    password_input = input("Password : ")

    login_berhasil = False
    role_login = ""
    nama_login = ""

    for u in users:
      if u[0] == username_input and u[1] == password_input:
        login_berhasil = True
        role_login = u[2]
        nama_login = u[0]
        break

    if login_berhasil:
      print(f"Login berhasil! Selamat datang, {nama_login} ({role_login}).")
      input("Tekan Enter untuk masuk ke menu...")

      session_active = True
      while session_active:

        #Buat Admin
        if role_login == "admin":
          print(f"MENU ADMIN ({nama_login})")
          print("1. Lihat Daftar Pesanan (Read)")
          print("2. Tambah Pesanan Baru (Create)")
          print("3. Ubah Status Pesanan (Update)")
          print("4. Ambil/Hapus Pesanan (Delete)")
          print("5. Logout")

          menu_admin = int(input("Pilih menu admin (1-5): "))

          #Daftar Pesanan Laundry (R)
          if menu_admin == 1:
            print("DAFTAR PESANAN LAUNDRY")
            if len(orders) == 0:
              print("Belum ada pesanan laundry yang aktif.")
            else:
              print("ID | Nama Pelanggan | Berat | Layanan | Status")
              print("-" * 65)
              for o in orders:
                print(f"{o[0]} | {o[1]} | {o[2]} | {o[3]} | {o[4]}")
            input("Tekan Enter untuk kembali ke menu...")

          #Tambah Pesanan Baru (C)
          elif menu_admin == 2:
            print("TAMBAH PESANAN BARU")
            id_baru = input("Masukkan ID Pesanan (contoh L003) : ")
            nama_pelanggan = input("Masukkan Nama Pelanggan          : ")
            berat_laundry = input("Masukkan Berat (misal: 4 kg)     : ")
            layanan = input("Masukkan Jenis Layanan           : ")
            status_awal = "Proses"

            if (
                id_baru != ""
                and nama_pelanggan != ""
                and berat_laundry != ""
                and layanan != ""
            ):
              pesanan_baru = [
                  id_baru,
                  nama_pelanggan,
                  berat_laundry,
                  layanan,
                  status_awal,
              ]
              orders.append(pesanan_baru)
              print("Pesanan baru berhasil ditambahkan ke antrean!")
            else:
              print("Gagal! Semua kolom data wajib diisi.")
            input("Tekan Enter untuk kembali ke menu...")

          #Update Admin (U)
          elif menu_admin == 3:
            print("UBAH STATUS PESANAN")
            if len(orders) == 0:
              print("Belum ada pesanan.")
            else:
              print("Daftar Pesanan Saat Ini:")
              for o in orders:
                print(f"ID: {o[0]} | Nama: {o[1]} | Status: {o[4]}")

              cari_id = input(
                  "Masukkan ID Pesanan yang ingin diubah statusnya: "
              )
              ditemukan = False
              for o in orders:
                if o[0] == cari_id:
                  ditemukan = True
                  print("Pilih Status Baru:")
                  print("1. Proses")
                  print("2. Selesai")
                  print("3. Siap Diambil")
                  pilih_status = int(input("Pilihan status (1-3): "))

                  if pilih_status == 1:
                    o[4] = "Proses"
                    print("Status berhasil diubah menjadi 'Proses'.")
                  elif pilih_status == 2:
                    o[4] = "Selesai"
                    print("Status berhasil diubah menjadi 'Selesai'.")
                  elif pilih_status == 3:
                    o[4] = "Siap Diambil"
                    print("Status berhasil diubah menjadi 'Siap Diambil'.")
                  else:
                    print("Pilihan status tidak valid.")
                  break

              if not ditemukan:
                print("ID Pesanan tidak ditemukan.")
            input("Tekan Enter untuk kembali ke menu...")

          #Menghapus Admin (D)
          elif menu_admin == 4:
            print("AMBIL / HAPUS PESANAN")
            if len(orders) == 0:
              print("Belum ada pesanan.")
            else:
              print("Daftar Pesanan Saat Ini:")
              for o in orders:
                print(f"ID: {o[0]} | Nama: {o[1]} | Status: {o[4]}")

              cari_id = input(
                  "Masukkan ID Pesanan yang diambil/dibayar pelanggan: "
              )
              ditemukan = False
              target_hapus = []
              for o in orders:
                if o[0] == cari_id:
                  ditemukan = True
                  target_hapus = o
                  break

              if ditemukan:
                orders.remove(target_hapus)
                print(
                    "Data pesanan berhasil dihapus dari antrean menggunakan"
                    " .remove() (Laundry telah diambil)!"
                )
              else:
                print("ID Pesanan tidak ditemukan.")
            input("\nTekan Enter untuk kembali ke menu...")

          elif menu_admin == 5:
            session_active = False
          else:
            print("Pilihan menu tidak valid.")
            input("Tekan Enter untuk kembali...")

        #Memakai User
        elif role_login == "user":
          print(f"MENU PELANGGAN ({nama_login})")
          print("1. Lihat Status Laundry")
          print("2. Logout")

          menu_user = int(input("Pilih menu (1-2): "))

          if menu_user == 1:
            print("STATUS ANTREAN LAUNDRY")
            if len(orders) == 0:
              print("Belum ada pesanan aktif.")
            else:
              print("ID | Nama Pelanggan | Berat | Layanan | Status")
              for o in orders:
                print(f"{o[0]} | {o[1]} | {o[2]} | {o[3]} | {o[4]}")
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
    #Proses Register
    print("REGISTER AKUN PELANGGAN BARU")
    new_user = input("Buat Username : ")
    new_pass = input("Buat Password : ")

    sudah_ada = False
    for u in users:
      if u[0] == new_user:
        sudah_ada = True
        break

    if sudah_ada:
      print("Registrasi Gagal! Username sudah digunakan orang lain.")
    elif new_user == "" or new_pass == "":
      print("Registrasi Gagal! Username dan password tidak boleh kosong.")
    else:
      users.append([new_user, new_pass, "user"])
      print("Registrasi berhasil! Silakan login dengan akun baru Anda.")
    input("Tekan Enter untuk kembali ke menu...")

  elif pilihan_awal == 3:
    print("Terima kasih telah menggunakan Sistem Pencatatan Laundry Kiloan!")
    app_running = False
  else:
    print("Pilihan tidak valid.")
    input("Tekan Enter untuk kembali...")
