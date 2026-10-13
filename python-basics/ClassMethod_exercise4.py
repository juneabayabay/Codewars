class Calculator:
    def __init__(self, base_value):
        self.base_value = base_value

    # Instance Method
    def add_to_base(self, number):
        self.base_value += number
        return self.base_value

    # Static Method
    @staticmethod
    def multiply(x, y):
        return x * y

# --- Usage Examples ---

# 1. Using the instance method (requires an object)
calc = Calculator(10)
print(calc.add_to_base(5))  # Output: 15

# 2. Using the static method (called directly on the class)
print(Calculator.multiply(4, 5))  # Output: 20
