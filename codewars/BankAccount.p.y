
class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.__balance = balance  # Private attribute

    # Getter method
    def get_balance(self):
        return self.__balance

    # Setter method
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited: ₱{amount}")
        else:
            print("Invalid deposit amount!")

    def withdraw(self, amount):
        if amount > 0 and amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrawn: ₱{amount}")
        else:
            print("Insufficient balance or invalid amount!")


# Create an object
account = BankAccount("Juan", 5000)

# Access public attribute
print("Account Owner:", account.owner)

# Access balance using getter
print("Balance:", account.get_balance())

# Deposit money
account.deposit(2000)

# Withdraw money
account.withdraw(1000)

# Check updated balance
print("Final Balance:", account.get_balance())
