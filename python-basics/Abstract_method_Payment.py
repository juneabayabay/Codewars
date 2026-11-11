
from abc import ABC, abstractmethod

class Payment(ABC):

    @abstractmethod
    def pay(self, amount):
        pass


class GCash(Payment):

    def pay(self, amount):
        print(f"Paid {amount} using GCash")


class BankTransfer(Payment):

    def pay(self, amount):
        print(f"Paid {amount} using Bank Transfer")


payment1 = GCash()
payment1.pay(500)

payment2 = BankTransfer()
payment2.pay(1000)
