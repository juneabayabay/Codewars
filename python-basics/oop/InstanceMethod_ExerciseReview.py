
class BankAccount:
    bank_name = "Python Bank"

    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    # Instance method
    def deposit(self, amount):
        if BankAccount.is_valid_amount(amount):
            self.balance += amount
            print(f"Deposit: {amount}")
        else:
            print("Invalid deposit amount")

    # Class method
    @classmethod
    def change_bank_name(cls, new_name):
        cls.bank_name = new_name

    # Static method
    @staticmethod
    def is_valid_amount(amount):
        return amount > 0


account = BankAccount("Arjune", 2000)

account.deposit(500)
print(account.balance)  # 2500

BankAccount.change_bank_name("BPI")
print(BankAccount.bank_name)  # BPI

print(BankAccount.is_valid_amount(100))   # True
print(BankAccount.is_valid_amount(-10))   # False
