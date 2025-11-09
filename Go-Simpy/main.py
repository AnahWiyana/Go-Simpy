from akun import akun
from tampilan import (tampilkan_menu_login, tampilkan_menu_utama)
from autentikasi import (login, logout, apakah_sudah_login, dapatkan_data_akun)
from manajemen_akun import (username_akun_sekarang)

def menu_admin():
	akun_sekarang = dapatkan_data_akun
	while True:
		tampilkan_menu_utama()
		pilihan = input("Pilih menu: ").strip()
	

if __name__ == "__main__":
	while True:
		if apakah_sudah_login() == False: 
			tampilkan_menu_login()
			pilihan = input("Pilih menu: ")

			if pilihan == "1":
				login()
			
			elif pilihan == "2":
				registrasi()
			
			elif pilihan == "3":
				print("Terimakasih telah menggunakan program ini.")
				sys.exit()
			
			else:
				print("Pilihan tidak valid")
				input("Tekan Enter untuk kembali")

		else:
			akun_sekarang = dapatkan_data_akun()
			role = username_akun_sekarang(akun_sekarang)["role"]

			if role == "admin":
				menu_admin()

			elif role == "manager":
				menu_manager()

			elif role == "pelanggan":
				menu_customer()

			elif role == "driver":
				menu_driver()
