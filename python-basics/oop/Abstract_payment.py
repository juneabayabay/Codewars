from abc import ABC, abstractmethod

class Payment(ABC):
    @abstractmethod
    def pay(self):
        print()

class Gcash(Payment):
    def pay(self):
        print("Payment through Gcash ")

gcash = Gcash()
gcash.pay()
