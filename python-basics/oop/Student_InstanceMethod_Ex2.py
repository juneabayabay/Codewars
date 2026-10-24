class Student:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def introduce(self):
      print(f"name: {self.name}, age: {self.age}")

p1 = Student("June", 26)
p2 = Student("Marc", 23)

p1.introduce()
p2.introduce()
