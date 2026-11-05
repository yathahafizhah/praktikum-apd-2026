import os

def clear_screen():
    """Poin Plus: Membersihkan terminal secara otomatis"""
    os.system('cls' if os.name == 'nt' else 'clear')

def pause():
    input("Tekan Enter untuk melanjutkan...")