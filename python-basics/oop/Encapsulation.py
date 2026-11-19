class BankAccount:
    def __init__(self, balance):
        self.__balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
        else:
            print("Invalid amount!")

    def get_balance(self):
        return self.__balance


account = BankAccount(1000)

account.deposit(-5000)

print(account.get_balance())
