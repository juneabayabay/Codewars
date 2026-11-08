# OPERATOR OVERLOADING IN PYTHON
# this is the I did last yesterday but I just want to push this for my last lessons of overlading method of OOP

class Student:

    # Constructor: receives the student's score
    def __init__(self, score):

        # Store the score inside the object
        self.score = score

    # Special method for the + operator
    def __add__(self, other):

        # Add the scores of two Student objects
        return self.score + other.score


# Creating two Student objects
student1 = Student(90)
student2 = Student(85)

# Using the + operator between two objects
# Python automatically calls the __add__() method
total = student1 + student2

# Display the result
print("Total Score:", total)
