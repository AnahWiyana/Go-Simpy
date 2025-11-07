import os
import sys
from akun import akun

sudah_login = False
akun_sekarang = None

def clear():
    os.system("cls" if os.name == "nt" else "clear")

def login():
    global sudah_login, akun_sekarang
    maksimal_percobaan = 5
    percobaan = 0

    while percobaan < maksimal_percobaan:
        clear()
        print("=== SISTEM LOGIN GO-SIMPY ===")
        username = input("Masukkan Username : ").strip()
        password = input("Masukkan Password : ").strip()

        if username in akun and akun[username]["password"] == password:
            sudah_login = True
            akun_sekarang = akun[username]
            clear()
            print(f"Selamat datang, {akun_sekarang['nama_lengkap']} ({akun_sekarang['role'].capitalize()})!")
            input("Tekan Enter untuk melanjutkan...")
            menu_utama()
            return
        else:
            percobaan += 1
            print("Username atau password salah!")
            input("Tekan Enter untuk mencoba lagi...")

    print("\nTerlalu banyak percobaan gagal. Program keluar.")
    sys.exit()

def logout():
    global sudah_login, akun_sekarang
    sudah_login = False
    akun_sekarang = None
    print("Anda telah logout.")
    input("Tekan Enter untuk kembali ke menu login...")
    login()

def apakah_sudah_login():
	return sudah_login

def username_akun_sekarang():
	return akun_sekarang
	input("Tekan Enter...")
