class Laptop:
    brand = "Lenovo"

    def __init__(self, model, price):
        self.model = model
        self.price = price


lap1 = Laptop("ThinkPad", 25000)
lap2 = Laptop("IdeaPad", 18000)

print(lap1.model)
print(lap2.model)

print(lap1.price)
print(lap2.price)

# Change lap1's price
lap1.price = 22000

print(lap1.price)
print(lap2.price)

# Change the shared class variable
Laptop.brand = "Dell"

print(lap1.brand)
print(lap2.brand)
