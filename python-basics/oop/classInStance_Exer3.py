class Student:
  school = "Central High"

  def __init__(self, name):
    self.name = name

name1 = Student("Alice")
name2 = Student("Bob")

Student.school = "West High"

print(name1.name)
print(name1.school)
print()
print(name2.name)
print(name2.school)
