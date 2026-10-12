class Fruits:
    def __init__(self, name, shape, color, taste, stock):
        self.name = name
        self.shape = shape
        self.color = color
        self.taste = taste
        self.stock = stock

    def describe(self):
        print(f"Fruit: {self.name}")
        print(f"Shape: {self.shape}")
        print(f"Color: {self.color}")
        print(f"Taste: {self.taste}")
        print(f"Stock: {self.stock}")
        print(f"We can make salad, juice, and pudding with {self.name}")

    def make_salad(self):
        print(f"=== {self.name} Stock ===")
        print(f"Remaining stock before making salad is {self.stock} fruits")
        print(f"Fruit used to make salad : 2 fruits")
        self.stock -= 2
        print(f"Remaining fruit stock now is {self.stock} fruit")

# Object
fruits_1 = Fruits("Apple", "Round", "Red", "Sweet", 10)
fruits_2 = Fruits("Banana", "Curved", "Yellow", "Sweet", 20)
fruits_3 = Fruits("Orange", "Round", "Orange", "Sweet & sour", 10)

# Call object
print(Fruits)
print(fruits_1)
print(fruits_1.name)

# Call method
fruits_1.describe()
fruits_2.describe()
fruits_3.describe()

# Make salad method
fruits_1.make_salad()
fruits_1.make_salad()

