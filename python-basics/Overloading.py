class Student:
  def introduce(self, name, age, course = "Not specified"):
    print("name:", name)
    print("Age:", age)
    print("Course:", course)
    print()

# Create an object
student = Student()

# Call the method
student.introduce("Alex", 20)

student.introduce("Maria", 21, "BSIT")
    
