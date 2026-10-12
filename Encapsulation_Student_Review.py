
class Student:
    def __init__(self, name, age, course):
        self.name = name
        self.age = age
        self.course = course

    def introduce(self):
        print(f"Name: {self.name}\nAge: {self.age}\nCourse: {self.course}")


student1 = Student("Arjune", 26, "IT")
student2 = Student("Marc", 23, "IT")

student1.introduce()
print()
student2.introduce()
