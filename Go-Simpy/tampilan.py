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
	print("Menu Login")
	print("1. Login")
	print("2. Registrasi")
	print("3. Keluar Program")

def tampilkan_menu_utama():
	bersihkan_layar()
	username = dapatkan_data_akun()
	data_akun = akun[username]
	print(f"Selamat datang, {data_akun['nama_lengkap']} ({username})")

	if data_akun["role"] == "admin":
		print("Anda adalah admin.")
		print("\n=== MENU ADMIN ===")
	
	else:
		print("\n=== MENU ===")
    
	if data_akun["role"] == "admin":
		print("1. Tambah User")
		print("2. Hapus User")
		print("3. Lihat Daftar User")
		print("4. Edit Profil")
		print("5. Logout")
		print("6. Keluar")
    
	else:
		print("1. Edit Profil")
		print("2. Logout")
		print("3. Keluar")
