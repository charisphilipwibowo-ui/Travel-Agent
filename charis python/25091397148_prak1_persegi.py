class Square:
    def __init__(self, sisi):
        self.sisi = sisi

    def luas(self):
        return self.sisi + self.sisi

    def keliling(self):
        return 4 * self.sisi

# Object
persegi1 = Square(5)
persegi2 = Square(7)
persegi3 = Square(10)

# Calling method
print("=== Persegi 1 ===")
print(f"Panjang sisi : {persegi1.sisi}")
print(f"Luas         : {persegi1.luas()}")
print(f"Keliling     : {persegi1.keliling()}")

print("=== Persegi 2 ===")
print(f"Panjang sisi : {persegi2.sisi}")
print(f"Luas         : {persegi2.luas()}")
print(f"Keliling     : {persegi2.keliling()}")

print("=== Persegi 3 ===")
print(f"Panjang sisi : {persegi3.sisi}")
print(f"Luas         : {persegi3.luas()}")
print(f"Keliling     : {persegi3.keliling()}")

