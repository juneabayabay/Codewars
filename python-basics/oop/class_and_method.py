# This a review of my yesterday lessons
# Object and Class

class Number: # creating a class
  def __init__(self,odd, even): # def means creating a function __init__special methods that python run automatically when we create an object

    # self refers to the current object something gateway, we dont manual pass
    self.odd = odd
    self.even = even

  def result(self): # we create a new funtion called result
    print(f"Sample of numbers {self.odd}.")
    print(f"This is samples of even {self.even}.")

Numberodd = Number(1,3) # we create a new object and called the main this then we add the value
Numbereven =Number(2,4)

Numberodd.result() #  We get the new object which had already default value one we called the result
Numbereven.result()
