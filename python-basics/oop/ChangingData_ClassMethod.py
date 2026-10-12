class Student:
    school = "ABC College"

    @classmethod
    def change_school(cls, new_name):
        cls.school = new_name

Student.change_school("XYZ University")

print(Student.school)
