
class Student:
    school_name = "Python Academy"

    def __init__(self, name, score):
        self.name = name
        self.score = score

    def display_info(self):
        print(f"My name is: {self.name}")
        print(f"My score is: {self.score}")
        print(f"My school is: {self.school_name}")

    @classmethod
    def change_school(cls, new_name):
        cls.school_name = new_name


student1 = Student("Alice", 90)
student2 = Student("Bob", 85)

# Display their information
student1.display_info()
student2.display_info()

# Change the school name
Student.change_school("Code Academy")

# Display their information again
student1.display_info()
student2.display_info()
