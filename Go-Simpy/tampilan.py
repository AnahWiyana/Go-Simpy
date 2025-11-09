# Import Library
import os

# Import file
from akun import akun
from manajemen_akun import username_akun_sekarang
from autentikasi import dapatkan_data_akun
from prettytable import PrettyTable

def bersihkan_layar():
    os.system('cls' if os.name == 'nt' else 'clear')

def tampilkan_menu_login():
    bersihkan_layar()
    print("=== MENU LOGIN ===")
    print("1. Login")
    print("2. Registrasi")
    print("3. Keluar Program")

def tampilkan_menu_utama():
    bersihkan_layar()
    username = dapatkan_data_akun()
    data_akun = akun[username]
    role = data_akun["role"]

    print(f"Selamat datang, {data_akun['nama_lengkap']} ({role.capitalize()})")
    print("=" * 40)

    # ==== MENU ===========
    if role == "admin":
        print("=== MENU ADMIN ===")
        print("1. Tambah User")
        print("2. Hapus User")
        print("3. Lihat Daftar User")
        print("4. Edit Profil")
        print("5. Logout")
        print("6. Keluar Program")

    elif role == "customer":
        print("=== MENU CUSTOMER ===")
        print("1. Pesan Layanan")
        print("2. Lihat Riwayat Pesanan")
        print("3. Edit Profil")
        print("4. Logout")
        print("5. Keluar Program")

    elif role == "manager":
        print("=== MENU MANAGER ===")
        print("1. Naikkan Gaji Driver")
        print("2. Grafik Penghasilan Driver")
        print("3. Edit Profil")
        print("4. Logout")
        print("5. Keluar Program")

    elif role == "driver":
        print("=== MENU DRIVER ===")
        print("1. Lihat Daftar Order Masuk")
        print("2. Konfirmasi Order")
        print("3. Lihat Penghasilan")
        print("4. Edit Profil")
        print("5. Logout")
        print("6. Keluar Program")

    else:
        print("Role tidak dikenal!")

    pilihan = input("\nPilih menu: ").strip()
    return pilihan
