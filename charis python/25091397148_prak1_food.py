class MenuItem:
    def __init__(self, name, price, details):
        self.name = name
        self.price = price
        self.details = details

    def info(self):
        print("=== Informasi menu ===")
        print(f"Nama menu: {self.name}")
        print(f"Harga: {self.price}")
        print(f"Detail menu: {self.details}")

    def hitung_total(self, jumlah):
        total = self.price * jumlah
        if jumlah >= 3:
            discount = total * 0.10
            total -= discount
            print(f"Anda mendapatkan diskon {discount} karena memesan {jumlah} porsi.")
        return total

daftar_menu = [
    MenuItem("Nasi Goreng Spesial", 25000, "Nasi goreng dengan telur, ayam suwir, dan kerupuk"),
    MenuItem("Mie Ayam Bakso", 20000, "Mie ayam dengan topping ayam kecap dan 2 bakso sapi"),
    MenuItem("Ayam Bakar Madu", 30000, "Ayam bakar bumbu madu manis gurih + sambal lalapan"),
    MenuItem("Es Teh Manis", 5000, "Es teh manis segar")
]

print("=== DAFTAR MENU FOOD ===")
for index, menu in enumerate(daftar_menu, start=1):
    print(f"Nomor pilihan: {index}")
    menu.info()

print(" Silakan lakukan pemesanan:")
try:
    pilihan = int(input("Masukkan nomor pilihan menu yang ingin dipesan: "))
    
    # Validasi jika nomor pilihan ada di dalam daftar menu
    if 1 <= pilihan <= len(daftar_menu):
        jumlah_pesanan = int(input("Masukkan jumlah pesanan (porsi/gelas): "))
        
        if jumlah_pesanan > 0:
            menu_terpilih = daftar_menu[pilihan - 1]
            print("\n" + "="*30)
            print("RINGKASAN PESANAN")
            print("="*30)
            print(f"Menu yang dipilih: {menu_terpilih.name}")
            print(f"Jumlah pesanan   : {jumlah_pesanan} porsi")
            
            # 8. Hitung jumlah biaya yang perlu dibayar dan menampilkan harganya.
            total_bayar = menu_terpilih.hitung_total(jumlah_pesanan)
            print(f"Total yang harus dibayar: Rp {total_bayar:,}")
            print("="*30)
            print("Terima kasih telah memesan!")
        else:
            print("Jumlah pesanan minimal harus 1.")
    else:
        print("Nomor menu tidak valid. Silakan jalankan ulang program.")

except ValueError:
    print("Input harus berupa angka/bilangan bulat!")

