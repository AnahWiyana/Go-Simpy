import sys
from akun import akun

sudah_login = False
akun_sekarang = None

def login():
	global sudah_login, akun_sekarang
	maksimal_percobaan = 5
	percobaan = 0
	while percobaan < maksimal_percobaan:
		# Fungsi loginnya disini

def logout():
	global sudah_login, akun_sekarang
	sudah_login = False
	user_sekarang = None
	print("Anda telah Logout")
	input("Tekan Enter untuk kembali...")
