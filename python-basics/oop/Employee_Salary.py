class Employee:
    salary_increase = 10

    @classmethod
    def change_increase(cls, new_rate):
        cls.salary_increase = new_rate

Employee.change_increase(15)

print(f"Salary increase rate: {Employee.salary_increase}%")
