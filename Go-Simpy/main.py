from akun import akun
from tampilan import tampilkan_menu_login
from autentikasi import (login, logout, apakah_sudah_login, username_akun_sekarang)

if __name__ == "__main__":
	while True:
		if not apakah_sudah_login():
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
			username = username_akun_sekarang()
			role = dapatkan_data_akun(username)["role"]

			if role == "admin":
				menu_admin()

			elif role == "manager":
				menu_manager()

			elif role == "pelanggan":
				menu_customer()

			elif role == "driver":
				menu_driver()
