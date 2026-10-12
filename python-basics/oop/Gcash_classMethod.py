class Gcash:
    payment = "Gcash was already send"
    
    def __init__(self, pay):
        self.pay = pay
        
    @classmethod
    def pay(cls):
        print(cls.payment)

Gcash.pay()
