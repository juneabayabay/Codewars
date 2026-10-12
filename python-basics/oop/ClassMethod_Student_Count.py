class Student:
    student_count = 0

    def __init__(self, name):
        self.name = name
        Student.student_count += 1

    @classmethod
    def show_count(cls):
        print(f"Total students: {cls.student_count}")

student1 = Student("Arjune")
student2 = Student("Marc")
student3 = Student("John")

Student.show_count()
