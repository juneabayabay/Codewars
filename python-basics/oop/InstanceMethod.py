class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        print(f"My name is {self.name}. I am {self.age} years old.")


student1 = Student("Alex", 20)
student2 = Student("Maria", 22)

student1.introduce()
student2.introduce()
