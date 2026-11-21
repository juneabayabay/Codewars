
from abc import ABC, abstractmethod

# Abstract Class
class Employee(ABC):

    def __init__(self, name, employee_id):
        self.name = name
        self.employee_id = employee_id

    @abstractmethod
    def calculate_salary(self):
        pass

    def display_info(self):
        print(f"Employee Name: {self.name}")
        print(f"Employee ID: {self.employee_id}")


# Child Class 1
class FullTimeEmployee(Employee):

    def __init__(self, name, employee_id, monthly_salary):
        super().__init__(name, employee_id)
        self.monthly_salary = monthly_salary

    def calculate_salary(self):
        return self.monthly_salary


# Child Class 2
class PartTimeEmployee(Employee):

    def __init__(self, name, employee_id, hours_worked, hourly_rate):
        super().__init__(name, employee_id)
        self.hours_worked = hours_worked
        self.hourly_rate = hourly_rate

    def calculate_salary(self):
        return self.hours_worked * self.hourly_rate


# Child Class 3
class CommissionEmployee(Employee):

    def __init__(self, name, employee_id, basic_salary, commission):
        super().__init__(name, employee_id)
        self.basic_salary = basic_salary
        self.commission = commission

    def calculate_salary(self):
        return self.basic_salary + self.commission


# Main Program
employees = [
    FullTimeEmployee("John", 101, 25000),
    PartTimeEmployee("Mark", 102, 80, 150),
    CommissionEmployee("Anna", 103, 15000, 5000)
]

for employee in employees:
    employee.display_info()
    print(f"Total Salary: ₱{employee.calculate_salary():,.2f}")
    print("-------------------------")
