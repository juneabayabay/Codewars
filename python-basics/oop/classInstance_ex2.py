class Student:
  def __init__(self, name, age, course):
    self.name = name
    self.age = age
    self.course = course

  def introduce(self):
    print(f"My name is {self.name} my age is {self.age} with course of {self.course} ")
    
student1 = Student("June", 26, "IT")
student2 = Student("Marc", 23, "IT")

student1.introduce()
student2.introduce()
