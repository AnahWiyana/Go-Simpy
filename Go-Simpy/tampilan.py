# Import Library
import os
import sys

# Import file
from akun import akun
from prettytable import PrettyTable
from autentikasi import username_akun_sekarang

def bersihkan_layar():
	os.system('cls' if os.name == 'nt' else 'clear')

def tampilkan_menu_login():
	bersihkan_layar()
	print("Menu Login")
	print("1. Login")
	print("2. Registrasi")
	print("3. Keluar Program")

def menu_utama():
	bersihkan_layar()
	if akun_sekarang["role"] == "admin":
        	menu_admin()

	elif akun_sekarang["role"] == "manager":
		menu_manager()

	elif akun_sekarang["role"] == "customer":
		menu_customer()

	elif akun_sekarang["role"] == "driver":
		menu_driver()

	else:
		print("Role tidak dikenali.")
		input("Tekan Enter untuk keluar...")
		sys.exit()

def menu_admin():
	bersihkan_layar()
	print("=== MENU ADMIN ===")
	print("1. Edit Profil")
	print("2. Lihat daftar akun")
	print("3. Hapus akun")
	print("4. Buat akun baru")
	print("5. Logout")
	print("6. Keluar dari program")
	
def menu_manager():
	bersihkan_layar()
	print("=== MENU MANAGER ===")
	print("1. Lihat data pesanan")
	print("2. Lihat grafik pendapatan")
	print("3. Tambah pendapatan driver")
	print("4. Logout")
	print("5. Keluar dari program")
	
def menu_driver():
	print("=== MENU DRIVER ===")
	print("1. Lihat pesanan hari ini")
	print("2. Update status pesanan")
	print("3. Logout")
