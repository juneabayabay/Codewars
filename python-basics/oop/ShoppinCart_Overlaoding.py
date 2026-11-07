class ShoppingCart: # class or blue print
  def __init__(self, items): # constructor
    self.items = items # attribute assignment

  def __add__(self, other): # new method and parameter
    combined_items = self.items + other.items # Combinig partial data

    return ShoppingCart(combined_items) # we call the class then the variable name who adding the all parameters 

cart1 = ShoppingCart(["Laptop", "Mouse"]) # we create a new obejct of the class then we add the value based on the parameters 

cart2 = ShoppingCart(["Keyboard","Monitor"])

merged_cart = cart1 + cart2 #  we created a new object and we comnbined the objects

print(merged_cart.items) # the nwe called the merged_card to call out all the object from items
