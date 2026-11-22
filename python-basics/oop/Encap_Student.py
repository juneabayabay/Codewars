class Student:
    def __init__(self):
        self.name = "John"
        self.age = 20

student = Student()

print(student.name)
print(student.age)

# Changing the values
student.name = "Mark"
student.age = 22

print(student.name)
print(student.age)
