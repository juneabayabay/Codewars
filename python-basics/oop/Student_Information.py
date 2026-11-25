class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age}")

class Student(Person):
    def __init__(self, name, age, course):
        super().__init__(name, age)
        self.course = course

    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age}, Course: {self.course}")

student = Student("June", 20, "BSIT")
student.display_info()

