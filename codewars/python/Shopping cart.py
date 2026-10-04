class ShoppingCart:
    def __init__(self):
        self.__items = []

    def add_item(self, item):
        self.__items.append(item)

    def remove_item(self, item):
        if item in self.__items:
            self.__items.remove(item)
        else:
            print(f"{item} is not in the cart.")

    def get_items(self):
        return self.__items

    def get_total_items(self):
        return len(self.__items)


# Create a shopping cart
cart = ShoppingCart()

# Add items
cart.add_item("Apple")
cart.add_item("Bread")
cart.add_item("Milk")

# Display items
print("Items:", cart.get_items())

# Display number of items
print("Total items:", cart.get_total_items())

# Remove an item
cart.remove_item("Bread")

print("After removing Bread:")
print("Items:", cart.get_items())
print("Total items:", cart.get_total_items())
