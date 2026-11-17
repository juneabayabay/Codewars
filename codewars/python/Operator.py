class Numbers:
    def __init__(self, num):
        self.num = num

    def __add__(self, other):
        return self.num + other.num


num1 = Numbers(10)
num2 = Numbers(20)

result = num1 + num2

print(result)
