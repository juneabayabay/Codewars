class Employee:
    company = "Tech Solutions."
    
    @classmethod
    def show_company(cls):
        print(cls.company)

Employee.show_company()
