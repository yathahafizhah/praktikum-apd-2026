from prettytable import PrettyTable

def cetak_tabel_orders(data_orders):
    if not data_orders:
        print("Belum ada data pesanan.")
        return

    tabel = PrettyTable()
    tabel.field_names = ["ID", "Nama Pelanggan", "Berat (Kg)", "Layanan", "Status", "Estimasi Waktu"]
    
    # Format perataan teks
    tabel.align["Nama Pelanggan"] = "l"
    tabel.align["Layanan"] = "c"
    tabel.align["Status"] = "c"

    for order_id, detail in data_orders.items():
        tabel.add_row([
            order_id,
            detail["nama"],
            f"{detail['berat']} kg",
            detail["layanan"],
            detail["status"],
            f"{detail['estimasi']} Jam"
        ])
    
    print(tabel)