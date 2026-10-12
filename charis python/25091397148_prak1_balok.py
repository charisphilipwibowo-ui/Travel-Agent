class Balok:
    def __init__(self, panjang, lebar, tinggi):
        self.panjang = panjang
        self.lebar = lebar
        self.tinggi = tinggi

    # Volume method
    def volume(self):
        return self.panjang * self.lebar * self.tinggi

    # Area method
    def area(self):
        return 2 * ((self.panjang * self.lebar) + (self.panjang * self.tinggi) + (self.lebar * self.tinggi))

# Create object
balok_1 = Balok(25, 15, 20)
balok_2 = Balok(40, 35, 55)
balok_3 = Balok(56, 40, 200)

# Create object
print(f"Volume balok 1: {balok_1.volume()}")
print(f"Luas balok 1: {balok_1.area()}")
print(f"Volume balok 2: {balok_2.volume()}")
print(f"Luas balok 2: {balok_2.area()}")
print(f"Volume balok 3: {balok_3.volume()}")
print(f"Luas balok 3: {balok_3.area()}")

