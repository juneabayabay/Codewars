class Car # Car is the class
  def __init__(self):
    self.__speed = 0 # __speed is variable

  def accelerate(self, amount): # we create a new method called accelerate with an identifier called amount
    self.__speed += amount # the speed default is 0, with assignment operator

  def get_speed(self): # we create again a new method called get_speed
    return self.__speed # we get the value of speed we used return statement t

car = Car() # we create a new class name with class value of original class name
  
car.accelerate(20) # we get the new method class with calling the method with already had a value
print(car.get_speed()) # we print the value with using the return statemate and method name

car.accelerate(50)
print(car.get_speed())
  
 

