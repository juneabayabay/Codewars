# _init_() Constructor

class Student:

  def __init__(self, name, age, course): # _init_() runs automatically. self means "this particular object or something specific"
    self.name = name
    self.age = age
    self.course = course

    # we can create a student easiy

student1 = Student("Arjune", 26, "BS Information Technology")
student2 = Student("Marc", 23, "BS Information Technology")

  # we can print easily the attributes in our class objects

print(student1.name)
print(student1.age)

print(student2.name)
print(student2.age)
print(student2.course)
