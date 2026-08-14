class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __gt__(self, other):# greater than, competition
        return self.price > other.price# automotically choose which is prod1, which is prod2


prod1 = Product("A", 1000)
prod2 = Product("B", 500)

print(prod1 > prod2)
print(f"{prod1.name}, {prod1.price}")
print(f"{prod2.name},{prod2.price}")