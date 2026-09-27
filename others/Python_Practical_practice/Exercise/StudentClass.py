class Student:
  def __init__(self,name, age):
    self.name = name
    self.age = age

  def introduce(self):
   print(f" My name is: {self.name} " + "and"   + f"I am{self.age}")
  
student1 = Student("June",26)



student1.introduce()
