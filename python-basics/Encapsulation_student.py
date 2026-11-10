class Student:
    def __init__(self, name):
        self.__name = name
        self.__grades = []

    def add_grade(self, grade):
        if 0 <= grade <= 100:
            self.__grades.append(grade)
        else:
            print("Grade must be between 0 and 100.")

    def get_average(self):
        if len(self.__grades) == 0:
            return 0

        return sum(self.__grades) / len(self.__grades)

    def get_grades(self):
        return self.__grades.copy()

    def set_name(self, name):
        if name.strip():
            self.__name = name
        else:
            print("Name cannot be empty.")

    def get_name(self):
        return self.__name


# Example
student = Student("John")

student.add_grade(85)
student.add_grade(90)
student.add_grade(78)

print(student.get_name())
print(student.get_grades())
print(student.get_average())

student.set_name("Mike")
print(student.get_name())
