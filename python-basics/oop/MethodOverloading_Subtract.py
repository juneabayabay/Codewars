class Calculator: 
  def subtract(self, a, b, c=0): # method and parameter
    return a - b - c # return with conditions

calculator = Calculator() # new object of class

print(calculator.subtract(10, 5)) # we get the new object name and nethod then we add the value
print(calculator.subtract(20, 5, 3))
