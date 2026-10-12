class Mahasiswa:
    def __init__(self, nama, kelas, nim):
        self.__nama = nama
        self.kelas = kelas
        self._nim = nim

    def set_nama(self, nama):
        if not nama.strip():
            raise ValueError("Nama tidak boleh kosong")
        self.__nama = nama

    def get_nama(self):
        return self.__nama