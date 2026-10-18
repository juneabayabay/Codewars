class Student:
    student_count = 0

    def __init__(self, name):
        self.name = name
        Student.student_count += 1

    @classmethod
    def get_student_count(cls):
        return cls.student_count


student1 = Student("Alice")
student2 = Student("Bob")
student3 = Student("Charlie")

print("Total students:", Student.get_student_count())
