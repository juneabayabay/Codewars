class Employee # blue print for an employee
  def __init__(self, name, position, salary): # 

    self.name = name
    self.position = position
    self.__salary =salary

  def get_salary(self): # get access the private salary
    return self.__salary # return the private salary

  def increase_salary(self, amount): # this method comes from privaete tell how much you add
    if amount > 0:
      self.__salary += amount

  def display_info(self):
    print("Name:", self.name)
    print("Position:", self.position)
    print("salary:", self.__salary)

employee = Employee("Arjune", "Developer", 30000) # creating an obeject wit values

employee.increase_salary(12222)

print("After salary increase:")
employee.display_info()
    
  
