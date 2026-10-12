class Mahasiswa:
	def __init__(self, nama, kelas, nim):
		self.__nama = nama       # private: hanya diakses melalui setter/getter
		self.kelas = kelas       # public: dapat diakses langsung
		self._nim = nim          # protected: digunakan oleh class dan turunannya

	# Setter dan Getter untuk atribut private __nama
	def set_nama(self, nama):
		if not nama.strip():
			raise ValueError("Nama tidak boleh kosong")
		self.__nama = nama

	# Getter untuk atribut private __nama
	def get_nama(self):
		return self.__nama

	# Method public untuk menampilkan data mahasiswa
	def tampilkan_data(self):
		print("========= Data Mahasiswa =========")
		print(f"Nama  : {self.get_nama()}")
		print(f"Kelas : {self.kelas}")
		print(f"NIM   : {self._nim}")
		self.__tampilkan_status()

	# Method protected untuk menampilkan NIM
	def _tampilkan_nim(self):
		print(f"NIM dari method protected: {self._nim}")

	# Method private untuk menampilkan status
	def __tampilkan_status(self):
		print("Status: data mahasiswa tersimpan dengan enkapsulasi")

# Contoh penggunaan class Mahasiswa
charis = Mahasiswa("Charis Philip Wibowo", "D", 25091397148)

# Mengakses atribut dan method
charis.set_nama("Charis Philip Wibowo")
print(f"Getter private __nama: {charis.get_nama()}")

# Mengubah atribut public kelas
charis.kelas = "D"
print(f"Atribut public kelas: {charis.kelas}")

# Mengakses atribut protected _nim
charis._tampilkan_nim()

# Menampilkan data mahasiswa menggunakan method public tampilkan_data
charis.tampilkan_data()
