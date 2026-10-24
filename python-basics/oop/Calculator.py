class Calculator:
    def add(self, a, b):
        return a + b

    def multiply(self, a, b):
        return a * b


# Create an object
calc = Calculator()

print("Sum:", calc.add(10, 5))
print("Product:", calc.multiply(10, 5))
