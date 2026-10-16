class Student:
    def __init__(self, name, age, grade1, grade2):
        self.name = name
        self.age = age
        self.grade1 = grade1
        self.grade2 = grade2

    def introduce(self):
        print(f"Hi, my name is {self.name} and I am {self.age} years old.")

    def calculate_average(self):
        return (self.grade1 + self.grade2) / 2

    def check_result(self):
        if self.calculate_average() >= 75:
            print("Passed!")
        else:
            print("Failed!")


# Create an object
student1 = Student("Alex", 18, 80, 90)

# Call the methods
student1.introduce()
print("My average grade is", student1.calculate_average())
student1.check_result()
