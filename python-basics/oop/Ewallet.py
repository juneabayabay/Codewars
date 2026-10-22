class Ewallet:
  def __init__(self, balance): # In the constructor we used parameter called balance 
    self.balance = balance # we stored it using self.balance

  def cash_in(self, amount): # we created method called cash_in
    self.balance += amount # add the amount to the current balance
    print(f"Cash in {amount}") # printing

  def pay(self, amount): # we created a method called pay() and we create a condition
    if amount > self.balance:
      print("Insufficient balance")

    else:
      self.balance -= amount
      print(f"Withdrwan: {amount}")

  def show_balance(self): # method for showing the balance
      print(f"Current balance: {self.balance}")

account = Ewallet(5000) # starting balance

account.cash_in(1500) # cash in we add amount 
account.pay(2000) # we pay 2000
account.show_balance() # the balance will show depend on the action of users
