class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

class Manager(Employee):
    def __init__(self, name, salary, department):
        super().__init__(name, salary)
        self.department = department

    def display_info(self):
        print(f"Name: {self.name}, Salary: {self.salary}, Department: {self.department}")  

manager = Manager("John", 50000, "IT")
manager.display_info()

# My understanding of the super() function is that it allows a child class to inherit the attributes and methods of a parent class.
# we created a parent class called Employee and a child class called Manager.
# then we can use the super() function to initialize the parent's attributes.
# and we can also use the super() function to call the parent's methods.

