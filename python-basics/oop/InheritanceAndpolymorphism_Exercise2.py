class Product:
    def display_info(self):
        print()
class Laptop(Product):
     def display_info(self):
         print("Laptop: Used for programming ")

class Phone(Product):
    def display_info(self):
        print("Phone: Used for communication ")

class Tablet(Product):
    def display_info(self):
        print("Tablet: Used for reading and drawing")
    
laptop = Laptop()
phone = Phone()
tablet = Tablet()

products = [laptop, phone, tablet]

for product in products:
    product.display_info()
