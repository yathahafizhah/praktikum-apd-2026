#BANKDIGITAL

username_benar = "yatha"
password_benar = "004"
pin_benar = "004004"   
saldo = 5000000

# ===== LOGIN =====
percobaan = 0
login_berhasil = False

while percobaan < 3:
    print("\n=== LOGIN ===")
    username = input("Username: ")
    password = input("Password: ")

    if username == username_benar and password == password_benar:
        login_berhasil = True
        print("Login berhasil!")
        break
    elif username != username_benar and password != password_benar:
        print("Username dan Password anda salah")
    elif username != username_benar:
        print("Username anda salah")
    else:
        print("Password anda salah")

    percobaan = percobaan + 1

if login_berhasil == False:
    print("Akun anda diblokir.")
    exit()

# ===== MENU UTAMA =====
while True:
    print("\n=== MENU UTAMA ===")
    print("1. Transfer Uang")
    print("2. Logout")
    pilihan = input("Pilihan: ")

    if pilihan == "1":

        # ===== TRANSFER =====
        while True:
            print("\nSaldo saat ini: Rp", saldo)

            if saldo < 50000:
                print("Saldo tidak cukup untuk transfer.")
                break

            penerima = input("Username penerima: ")

            #TENTUKANNOMINAL
            while True:
                teks = input("Nominal transfer: ")
                if teks.isdigit() == False:
                    print("Nominal harus berupa angka!")
                    continue

                nominal = int(teks)
                if nominal < 50000:
                    print("Nominal minimal Rp50000!")
                elif nominal > 1000000:
                    print("Nominal maksimal Rp1000000!")
                elif nominal > saldo:
                    print("Saldo anda tidak mencukupi!")
                else:
                    break

            #VALIDASIPIN3XKESEMPATAN
            salah = 0
            pin_benar_input = False
            while salah < 3:
                pin = input("Masukkan PIN: ")
                if pin == pin_benar:
                    pin_benar_input = True
                    break
                print("PIN salah!")
                salah = salah + 1
            if pin_benar_input == False:
                print("PIN salah 3x. Akun anda diblokir.")
                exit()

            #JIKATRANSFERBERHASIL
            saldo = saldo - nominal
            print("\n===== STRUK TRANSFER =====")

            print("Pengirim  :", username_benar)
            print("Penerima  :", penerima)
            print("Nominal   : Rp", nominal)
            print("Sisa saldo: Rp", saldo)
            print("==========================")

            #TANYAMAUTRANSFERLAGI?
            while True:
                lagi = input("Transfer lagi (y/n)? ")
                if lagi == "y" or lagi == "n":
                    break
                print("Masukkan y atau n!")

            if lagi == "n":
                break

    elif pilihan == "2":
        print("Anda telah logout. Terima kasih!")
        break
    else:
        print("Pilihan tidak valid!")