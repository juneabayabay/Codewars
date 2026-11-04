class Calculator:
    def add(self, *args):
        total = 0

        for num in args:
            total += num

        return total


calc = Calculator()

print("Sum:", calc.add(5, 10))

print("Sum:", calc.add(10, 10, 10))

print("Sum:", calc.add(25, 25, 25, 25))
