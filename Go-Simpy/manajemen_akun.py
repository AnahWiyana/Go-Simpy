from prettytable import PrettyTable
from akun import akun

data_akun = []

def tambah_akun(username, password, nama_lengkap, umur, nomor_telepon, alamat_email, role="pengguna"):
    # Cek apakah username sudah ada
    for akun in data_akun:
        if akun["username"] == username:
            print("Username sudah digunakan, silakan pilih username lain.")
            return

    akun_baru = {
        "username": username,
        "password": password,
        "nama_lengkap": nama_lengkap,
        "umur": umur,
        "nomor_telepon": nomor_telepon,
        "alamat_email": alamat_email,
        "role": role
    }

    data_akun.append(akun_baru)
    print(f"Akun '{username}' berhasil ditambahkan sebagai {role}.")
    
# def hapus_akun(username):
# 	# Fungsi hapus akun berdasarkan username akun

# def edit_profil(username, password, nama_lengkap=None, umur=None, no_telepon=None, alamat_email=None):
# 	# Fungsi edit profil akun

# def tampilkan_daftar_akun():
# 	table = PrettyTable()
# 	table.field_names = ["Username", "Nama Lengkap", "Umur", "No. Telp", "Email", "Role"]
# 	for username, data in akun.items():
# 		table.add_row([
# 			username,
# 			data["nama_lengkap"],
# 			data["umur"],
# 			data["nomor_telepon"],
# 			data["alamat_email"],
# 			data["role"]
# 		])
# 	print("===Daftar User===")
# 	print(table)
# 	input("Tekan Enter untuk kembali...")
