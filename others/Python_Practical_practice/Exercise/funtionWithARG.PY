def add_numbers(*numbers):
    total = 0

    for number in numbers:
        total += number

    return total

print(add_numbers(10, 20))
print(add_numbers(10, 20, 30, 40))
