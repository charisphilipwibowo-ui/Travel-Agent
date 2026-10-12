# Student Personal data
class personal_data:
    def __init__(self, nama, kelas, nim, department, fakultas, kampus):
        self.nama = nama
        self.kelas = kelas
        self.nim = nim
        self.department = department
        self.fakultas = fakultas
        self.kampus = kampus

    def describe(self):
        print("=========Data Pribadi Mahasiswa=========")
        print("Nama: ", self.nama)
        print("Kelas: ", self.kelas)
        print("NIM: ", self.nim)
        print("Departement: ", self.department)
        print("Fakultas: ", self.fakultas)
        print("Kampus: ", self.kampus)

# Create object
charis = personal_data("Charis Philip Wibowo", "D", 25091397148, "D4 Manajemen Informatika", "Vokasi", "Universitas Negeri Surabaya")

# Object Access
print(charis.nama)

charis.describe()

