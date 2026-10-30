
# Parent Class
class Employee:

    def __init__(self, name, employee_id, salary):
        self.name = name
        self.employee_id = employee_id
        self.salary = salary

    def display_info(self):
        print("Name:", self.name)
        print("Employee ID:", self.employee_id)
        print("Salary:", self.salary)


# Child Class 1
class Manager(Employee):

    def __init__(self, name, employee_id, salary, bonus):

        # Call the parent constructor
        super().__init__(name, employee_id, salary)

        self.bonus = bonus

    def display_info(self):

        print("Name:", self.name)
        print("Employee ID:", self.employee_id)
        print("Salary:", self.salary)
        print("Bonus:", self.bonus)

        total_salary = self.salary + self.bonus

        print("Total Salary:", total_salary)


# Child Class 2
class Developer(Employee):

    def __init__(self, name, employee_id, salary, language):

        # Call the parent constructor
        super().__init__(name, employee_id, salary)

        self.language = language

    def display_info(self):

        print("Name:", self.name)
        print("Employee ID:", self.employee_id)
        print("Salary:", self.salary)
        print("Programming Language:", self.language)


# Creating Objects

employee1 = Employee("John", 101, 50000)

manager1 = Manager("Alice", 102, 70000, 15000)

developer1 = Developer("Mark", 103, 60000, "Python")


# Display Information

print("===== EMPLOYEE INFORMATION =====")
employee1.display_info()

print("\n===== MANAGER INFORMATION =====")
manager1.display_info()

print("\n===== DEVELOPER INFORMATION =====")
developer1.display_info()
