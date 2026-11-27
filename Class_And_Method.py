class Car:
  def __init__(self, brand):
    self.brand = brand # the constaractore

  def start_engine(self):
    print(self.brand, "engine is starting!") # we add a description while calling the parameter

car1 = Car("Toyota") # Object with value
car1.start_engine() # we call the method to print

