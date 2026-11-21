class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.__balance = balance

    # Get the balance
    def get_balance(self):
        return self.__balance

    # Deposit money
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print("Deposit successful!")
        else:
            print("Invalid deposit amount!")

    # Withdraw money
    def withdraw(self, amount):
        if amount > 0 and amount <= self.__balance:
            self.__balance -= amount
            print("Withdrawal successful!")
        else:
            print("Insufficient balance or invalid amount!")


# Create an object
account = BankAccount("John", 1000)

# Access the balance
print("Balance:", account.get_balance())

# Deposit money
account.deposit(500)

# Withdraw money
account.withdraw(200)

# Check the updated balance
print("Final Balance:", account.get_balance())
