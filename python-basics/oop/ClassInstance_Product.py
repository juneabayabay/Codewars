class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def calculate_total_value(self):
        return self.price * self.quantity

    def sell(self, amount):
        if amount > 0 and amount <= self.quantity:
            self.quantity -= amount
            print(f"Sold {amount} {self.name}(s).")
        else:
            print("Invalid amount or not enough stock.")

# Create three product instances
product1 = Product("Laptop", 50000, 10)
product2 = Product("Mouse", 500, 20)
product3 = Product("Keyboard", 1500, 15)

# Display total stock value
print(product1.name, "Total Value:", product1.calculate_total_value())
print(product2.name, "Total Value:", product2.calculate_total_value())
print(product3.name, "Total Value:", product3.calculate_total_value())

# Sell products
product1.sell(2)
product2.sell(5)
product3.sell(20)

# Display updated quantities
print("\nUpdated Stock:")
print(product1.name, "Quantity:", product1.quantity)
print(product2.name, "Quantity:", product2.quantity)
print(product3.name, "Quantity:", product3.quantity)
