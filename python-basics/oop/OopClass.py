class Employee:
  company = "ABC Corporation"

  def __init__(self, name, position, salary):
    self.name = name
    self.position = position
    self.salary = salary

em1 = Employee("John", "Programmer", 30000)
em2 = Employee("Sarah", "Manager", 45000)
em3 = Employee("Mike", "Designer", 35000)

print(em1.name)
print(em1.position)
print(em1.salary)

print(em2.name)
print(em2.position)
print(em2.salary)

print(em3.name)
print(em3.position)
print(em3.salary)

# 2. Print the original company
print("\n=== Original Company ===")

print(em1.company)
print(em2.company)
print(em3.company)


# 3. Change the class variable
Employee.company = "XYZ Corporation"


# 4. Print the updated company
print("\n=== Updated Class Variable ===")

print(em1.company)
print(em2.company)
print(em3.company)


# 5. Change only John's company
em1.company = "John's Startup"


# 6. Print the company for all employees again
print("\n=== Final Company Values ===")

print(em1.company)
print(em2.company)
print(em3.company)



