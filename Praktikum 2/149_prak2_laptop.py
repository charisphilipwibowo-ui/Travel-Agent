# Kelas untuk merepresentasikan sebuah novel
class Novel:
    def __init__(self, judul, nama_pengarang, tahun_terbit, deskripsi, harga_beli):
        self.__judul = judul
        self.__nama_pengarang = nama_pengarang
        self.__tahun_terbit = tahun_terbit
        self.__deskripsi = deskripsi
        self.__harga_beli = harga_beli

    # Method untuk menghitung harga jual novel dengan diskon 20%
    def hitung_harga_jual(self):
        return self.__harga_beli - (0.2 * self.__harga_beli)

    # Method untuk mendapatkan harga beli novel
    def harga_beli(self):
        return self.__harga_beli

    # Method untuk menampilkan detail novel
    def detail_novel(self):
        harga_jual = self.hitung_harga_jual()
        return (
            f"Judul: {self.__judul}\n"
            f"Nama Pengarang: {self.__nama_pengarang}\n"
            f"Tahun Terbit: {self.__tahun_terbit}\n"
            f"Deskripsi: {self.__deskripsi}\n"
            f"Harga Beli: Rp{self.__harga_beli}\n"
            f"Estimasi Jual: Rp{harga_jual}"
        )

# Membuat objek Novel
novel1 = Novel(
    judul="Catatan Kasus Sherlock Holmes",
    nama_pengarang="Arthur Conan Doyle",
    tahun_terbit=1892,
    deskripsi="Kumpulan petualangan detektif legendaris Sherlock Holmes bersama Dr. Watson dalam memecahkan misteri pelik di London.",
    harga_beli=85000
)

novel2 = Novel(
    judul="Pembunuhan di Orient Express",
    nama_pengarang="Agatha Christie",
    tahun_terbit=1934,
    deskripsi="Detektif Hercule Poirot harus mengungkap kasus pembunuhan misterius di dalam kereta mewah yang terjebak badai salju.",
    harga_beli=95000
)

novel3 = Novel(
    judul="Detektif Conan Vol. 1",
    nama_pengarang="Gosho Aoyama",
    tahun_terbit=1994,
    deskripsi="Kisah Shinichi Kudo, detektif SMA jenius yang tubuhnya menyusut menjadi anak-anak setelah meminum racun misterius.",
    harga_beli=45000
)

# Membuat daftar novel
daftar_novel = [novel1, novel2, novel3]

# Menampilkan detail novel dan ringkasan finansial
print("========= Daftar Novel =========")
for i, novel in enumerate(daftar_novel, start=1):
    print(f"\nBuku ke-{i}:")
    print(novel.detail_novel())

# Menghitung total harga beli dan estimasi harga jual seluruh novel
total_harga_beli = sum(novel.harga_beli() for novel in daftar_novel)
total_harga_jual = sum(novel.hitung_harga_jual() for novel in daftar_novel)

# Menampilkan ringkasan finansial
print("=" * 43)
print("===RINGKASAN FINANSIAL===")
print(f"Total Harga Beli seluruh novel: Rp{total_harga_beli:,.0f}")
print(f"Total Estimasi Jual seluruh novel: Rp{total_harga_jual:,.0f}")