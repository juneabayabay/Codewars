class Student:
    def __init__(self, name, grade):
        self.name = name
        self.__grade = grade # we made a class called Student and the attributes

    def get_grade(self): # method to get the grades 
        return self.__grade

    def set_grade(self, new_grade): # wmthod as well with conditions
        if 0 <= new_grade <= 100:
            self.__grade = new_grade
            print("Grade successfully updated!")
        else:
            print("Invalid grade! Grade must be between 0 and 100.")


# Create a student object
student = Student("Mark", 85)

# Display student information
print("Student:", student.name)
print("Grade:", student.get_grade())

# Update the grade
student.set_grade(95)

# Display updated grade
print("Updated Grade:", student.get_grade())
