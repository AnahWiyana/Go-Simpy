import os
import sys
from akun import akun

# Variabel global
sudah_login = False
akun_sekarang = None

def login():
	from tampilan import bersihkan_layar
	global sudah_login, akun_sekarang
	maksimal_percobaan = 5
	percobaan = 0

	while percobaan < maksimal_percobaan:
		bersihkan_layar()
		print("=== LOGIN ===\n")
		username = input("Masukkan Username: ").strip()
		password = input("Masukkan Password: ").strip()
        
		if username in akun and akun[username]["password"] == password:
			sudah_login = True
			akun_sekarang = username
			bersihkan_layar()
			print("Login berhasil!")
			input("\nTekan Enter untuk melanjutkan...")
			return True
      
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
	print("Anda telah logout, silahkan login kembali")
	input("Tekan Enter untuk kembali...")	

def apakah_sudah_login():
	return sudah_login

def dapatkan_data_akun():
	return akun_sekarang

