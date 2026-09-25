class Student: # class called Student
  def __init__(self, name): # __init__ method called constructor
    self.name = name # self refers specific object
    # name" value will giving to the Class  when creating it
# self.name = name belong to the specific class object

st1 = Student("Arjune")
st2 = Student("Marc")

print(st1.name)
print(st2.name)
