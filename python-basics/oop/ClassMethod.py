class Student:
    school = "STI College"

    def __init__(self, name):
        self.name = name

    @classmethod
    def show_school(cls):
        print(cls.school)

Student.show_school()
