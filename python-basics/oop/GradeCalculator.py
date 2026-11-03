class GradeCalculator: 

    def calculate_grade(self, grade1, grade2=None, grade3=None): # function and method  and the parameters

        if grade2 is None and grade3 is None: # we create a condtions
            return grade1

        elif grade3 is None:
            return (grade1 + grade2) / 2

        else:
            return (grade1 + grade2 + grade3) / 3


student = GradeCalculator() # new object

print("Grade:", student.calculate_grade(90))

print("Average of 2 grades:", student.calculate_grade(80, 90))

print("Average of 3 grades:", student.calculate_grade(85, 90, 95))
