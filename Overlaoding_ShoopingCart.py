class ShoppingCart:

    def calculate_total(self, price, quantity=1, discount=0):
        subtotal = price * quantity
        total = subtotal - discount

        return total


cart = ShoppingCart()

print(cart.calculate_total(100))
print(cart.calculate_total(100, 3))
print(cart.calculate_total(100, 3, 20))
