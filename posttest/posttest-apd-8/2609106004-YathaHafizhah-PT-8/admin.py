from data import orders, hitung_estimasi_waktu
from tabel import cetak_tabel_orders
from transisi import clear_screen, pause

def tambah_pesanan():
    clear_screen()
    print("=== TAMBAH PESANAN LAUNDRY (CREATE) ===")
    nama = input("Nama Pelanggan : ").strip()
    try:
        berat = int(input("Berat Cucian (Kg) : "))
        if berat <= 0:
            print("Berat cucian harus lebih dari 0!")
            pause()
            return
    except ValueError:
        print("Input berat harus berupa angka!")
        pause()
        return

    print("Pilih Jenis Layanan:")
    print("1. Reguler")
    print("2. Kilat")
    pilih_layanan = input("Pilihan (1/2): ").strip()
    layanan = "Kilat" if pilih_layanan == "2" else "Reguler"

    new_id = max(orders.keys(), default=0) + 1
    estimasi = hitung_estimasi_waktu(berat)

    orders[new_id] = {
        "nama": nama,
        "berat": berat,
        "layanan": layanan,
        "status": "Proses",
        "estimasi": estimasi
    }
    print(f"\nPesanan ID {new_id} atas nama '{nama}' berhasil ditambahkan!")
    pause()

def lihat_semua_pesanan():
    clear_screen()
    print("=== DAFTAR SEMUA PESANAN (READ) ===")
    cetak_tabel_orders(orders)
    pause()

def ubah_status_pesanan():
    clear_screen()
    print("=== UBAH STATUS PESANAN (UPDATE) ===")
    cetak_tabel_orders(orders)
    if not orders:
        pause()
        return

    try:
        order_id = int(input("\nMasukkan ID Pesanan yang ingin diubah: "))
    except ValueError:
        print("ID harus berupa angka!")
        pause()
        return

    if order_id not in orders:
        print("ID Pesanan tidak ditemukan!")
        pause()
        return

    print(f"\nStatus saat ini: {orders[order_id]['status']}")
    print("Pilih Status Baru:")
    print("1. Proses")
    print("2. Selesai")
    pilihan = input("Pilihan (1/2): ").strip()

    if pilihan == "1":
        orders[order_id]["status"] = "Proses"
        print("\nStatus berhasil diubah menjadi 'Proses'.")
    elif pilihan == "2":
        orders[order_id]["status"] = "Selesai"
        print("\nStatus berhasil diubah menjadi 'Selesai'.")
    else:
        print("\nPilihan tidak valid!")

    pause()

def hapus_pesanan():
    clear_screen()
    print("=== HAPUS / AMBIL PESANAN (DELETE) ===")
    cetak_tabel_orders(orders)
    if not orders:
        pause()
        return

    try:
        order_id = int(input("Masukkan ID Pesanan yang ingin dihapus: "))
    except ValueError:
        print("ID harus berupa angka!")
        pause()
        return

    if order_id in orders:
        removed = orders.pop(order_id)
        print(f"\nPesanan ID {order_id} atas nama '{removed['nama']}' berhasil dihapus!")
    else:
        print("ID Pesanan tidak ditemukan!")

    pause()

def menu_admin():
    while True:
        clear_screen()
        print("=== MENU UTAMA ADMIN ===")
        print("1. Tambah Pesanan Baru (Create)")
        print("2. Tampilkan Semua Pesanan (Read)")
        print("3. Ubah Status Pesanan (Update)")
        print("4. Hapus Pesanan (Delete)")
        print("5. Logout")
        pilihan = input("Pilih menu (1-5): ").strip()

        if pilihan == "1":
            tambah_pesanan()
        elif pilihan == "2":
            lihat_semua_pesanan()
        elif pilihan == "3":
            ubah_status_pesanan()
        elif pilihan == "4":
            hapus_pesanan()
        elif pilihan == "5":
            print("Logout berhasil.")
            pause()
            break
        else:
            print("Pilihan tidak valid!")
            pause()