
class BankAccount:
    def __init__(self, balance):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposit: {amount}")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient balance!")
        else:
            self.balance -= amount
            print(f"Withdrawn: {amount}")

    def show_balance(self):
        print(f"Current balance: {self.balance}")


account = BankAccount(20000)

account.deposit(404)
account.withdraw(6007)
account.show_balance()
