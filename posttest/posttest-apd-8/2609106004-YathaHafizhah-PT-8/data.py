#data

users = {
    "admintuh": {"password": "17", "role": "admin"},
    "yatha": {"password": "123", "role": "customer"}
}

orders = {
    1: {"nama": "yatha", "berat": 3, "layanan": "Kilat", "status": "Proses", "estimasi": 6},
    2: {"nama": "al", "berat": 5, "layanan": "Reguler", "status": "Selesai", "estimasi": 10}
}

def hitung_estimasi_waktu(n):
    """
    Fungsi Rekursif: Menghitung estimasi pengerjaan (2 jam per Kg)
    """
    if n <= 1:
        return 2
    return 2 + hitung_estimasi_waktu(n - 1)
