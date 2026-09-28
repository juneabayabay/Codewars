try:
    name = input("Enter your name: ")
    age = int(input("Enter your age: "))

except ValueError:
    print("Please enter valid data.")

else:
    print("Your name is", name, "and your age is", age)

finally:
    print("Great Job!")
