class EWallet: # class
    def __init__(self, owner, balance, pin): # method runs automatically when we create a class
        self.__owner = owner
        self.__balance = balance # this are the 3 attributes when whem they are stored data
        self.__pin = pin

    def deposit(self, amount): # we create a loop
        if amount > 0:
            self.__balance += amount
            print(f"Deposited: {amount}")
        else:
            print("Deposit amount must be greater than 0.")

    def withdraw(self, amount, pin):
        if pin != self.__pin:
            print("Incorrect PIN.")
        elif amount <= 0:
            print("Withdrawal amount must be greater than 0.")
        elif amount > self.__balance:
            print("Insufficient balance.")
        else:
            self.__balance -= amount
            print(f"Withdrawn: {amount}")

    def check_balance(self, pin):
        if pin == self.__pin:
            return self.__balance
        else:
            print("Incorrect PIN.")
            return None

    def change_pin(self, old_pin, new_pin):
        if old_pin != self.__pin:
            print("Incorrect old PIN.")
        elif len(new_pin) != 4 or not new_pin.isdigit():
            print("PIN must be exactly 4 digits.")
        else:
            self.__pin = new_pin
            print("PIN changed successfully.")

    def get_owner(self):
        return self.__owner


wallet = EWallet("Alex", 1000, "1234") # this is the example of the method init at the top

wallet.deposit(500)

wallet.withdraw(200, "1234")

print(wallet.check_balance("1234"))

wallet.withdraw(100, "9999")

wallet.change_pin("1234", "5678")

print(wallet.check_balance("5678"))
