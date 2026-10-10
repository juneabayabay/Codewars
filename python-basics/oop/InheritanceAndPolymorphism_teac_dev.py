class Employee:
    def work(self):
        print("Employee is working")
    
class Developer(Employee):
    def work(self):
        print("Developer who is writing code.")

class Teacher(Employee):
    def work(self):
        print("Teacher is teaching studens. ")
        
dev1 = Developer()
tech1 = Teacher()

dev1.work()
tech1.work()
