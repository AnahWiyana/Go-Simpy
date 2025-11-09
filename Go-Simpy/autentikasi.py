import os
import sys
from akun import akun

# Variabel global
sudah_login = False
akun_sekarang = None


def clear():
    os.system("cls" if os.name == "nt" else "clear")


def menu_utama():
    while True:
        clear()
        print("=== SISTEM LOGIN GO-SIMPY ===\n")
        print("1. Login")
        print("2. Register")
        print("3. Keluar")

        pilihan = input("\nPilih menu (1-3): ").strip()

        if pilihan == "1":
            login()
        elif pilihan == "2":
            register()
        elif pilihan == "3":
            print("\nTerima kasih telah menggunakan GO-SIMPY!")
            sys.exit()
        else:
            print("Pilihan tidak valid!")
            input("Tekan Enter untuk mencoba lagi...")


def login():
    global sudah_login, akun_sekarang
    maksimal_percobaan = 5
    percobaan = 0

    while percobaan < maksimal_percobaan:
        clear()
        print("=== LOGIN ===\n")
        username = input("Masukkan Username: ").strip()
        password = input("Masukkan Password: ").strip()

        if username in akun and akun[username]["password"] == password:
            sudah_login = True
            akun_sekarang = akun[username]
            clear()
            print(f"Selamat datang, {akun_sekarang['nama_lengkap']} ({akun_sekarang['role'].capitalize()})!")
            input("\nTekan Enter untuk melanjutkan...")
            return
        else:
            percobaan += 1
            print("Username atau password salah!")
            input("Tekan Enter untuk mencoba lagi...")

    print("\nTerlalu banyak percobaan gagal. Program keluar.")
    sys.exit()


def register():
    clear()
    print("=== REGISTER ===\n")
    username = input("Masukkan Username baru: ").strip()
    if username in akun:
        print("Username sudah digunakan!")
        input("Tekan Enter untuk kembali...")
        return

    password = input("Masukkan Password: ").strip()
    nama = input("Masukkan Nama Lengkap: ").strip()
    umur = input("Masukkan Umur: ").strip()
    no_telp = input("Masukkan Nomor Telepon: ").strip()
    email = input("Masukkan Email: ").strip()
    role = input("Masukkan Role (admin/driver/pengguna): ").strip() or "pengguna"

    akun[username] = {
        "password": password,
        "nama_lengkap": nama,
        "umur": umur,
        "nomor_telepon": no_telp,
        "alamat_email": email,
        "role": role
    }

    print(f"\nAkun '{username}' berhasil dibuat sebagai {role}.")
    input("Tekan Enter untuk kembali ke menu utama...")


if __name__ == "__main__":
    menu_utama()
