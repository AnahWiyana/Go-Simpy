from prettytable import PrettyTable
from akun import akun

def tambah_akun(username, password, nama_lengkap, umur, nomor_telepon, alamat_email, role="pengguna"):
	# Fungsi tambah akun baru

def hapus_akun(username):
	# Fungsi hapus akun berdasarkan username akun

def edit_profil(username, password, nama_lengkap=None, umur=None, no_telepon=None, alamat_email=None):
	# Fungsi edit profil akun

def tampilkan_daftar_akun():
	table = PrettyTable()
	table.field_names = ["Username", "Nama Lengkap", "Umur", "No. Telp", "Email", "Role"]
	for username, data in akun.items():
		table.add_row([
			username,
			data["nama_lengkap"],
			data["umur"],
			data["nomor_telepon"],
			data["alamat_email"],
			data["role"]
		])
	print("===Daftar User===")
	print(table)
	input("Tekan Enter untuk kembali...")
