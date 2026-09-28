class BankAccount: # class name BankAccount
    def __init__(self, balance): # when you create a new object it will automatically called
        self.__balance = balance # __balance or  __ object name is private variable

    def deposit(self, amount): # new method called deposit variable call amount
        self.__balance += amount # we get the private variable and we a assignment operator, the same with withdraw

    def withdraw(self, amount):
        self.__balance -= amount

    def get_balance(self):
        return self.__balance # we create a new method to get and show the current balance


account = BankAccount(1000)

account.deposit(500)
account.withdraw(200)

print(account.get_balance()) # rpint the balance
