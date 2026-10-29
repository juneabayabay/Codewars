
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def show_info(self):
        print(f"Name: {self.name}")
        print(f"Salary: {self.salary}")


class Developer(Employee):
    def __init__(self, name, salary, programming_language):
        # Call the parent's constructor
        super().__init__(name, salary)
        self.programming_language = programming_language

    def show_info(self):
        # Call the parent's show_info() method
        super().show_info()

        # Add the developer's own information
        print(f"Programming Language: {self.programming_language}")


dev = Developer("Alex", 50000, "Python")

dev.show_info()
