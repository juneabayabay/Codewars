class Student:
  def introduce(self, name, age = 18, course = "Not specified"): # we create a default value and not specified value
    return f"Name: {name}\nAge: {age}\ncourse:{course}" # here we return the parameter itself

student = Student() # new object class

print(student.introduce("John")) # First student is john with default
print()
print(student.introduce("Mary", 20, "BSIT")) # second student we created a unique value
print()
print(student.introduce("Arjune",26,"BSIT")) 
