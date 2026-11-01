import math

# Parent class
class Shape:
    def calculate_area(self):
        pass

# Child class 1
class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def calculate_area(self):
        return self.length * self.width


# Child class 2
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        return math.pi * self.radius ** 2


# Child class 3
class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def calculate_area(self):
        return 0.5 * self.base * self.height


# Creating objects
rectangle = Rectangle(10, 5)
circle = Circle(7)
triangle = Triangle(8, 6)


# Displaying calculated areas
print("Rectangle Area:", rectangle.calculate_area())
print("Circle Area:", circle.calculate_area())
print("Triangle Area:", triangle.calculate_area())
