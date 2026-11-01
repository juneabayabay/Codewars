class BankAccount:
  def withdraw(self):
    print("Withdraw money from a back account")

class SavingAccount(BankAccount):
  def withdraw(self):
    print("Withdraw money from the saving account with a withdrawal limit")

class CheckingAccount(BankAccount):
  def withdraw(self):
    print("Withdrawing money from checking account with no withdrawal limit")

bankaccount = BankAccount()
savingAccount = SavingAccount()
checkingAccount = CheckingAccount()

bankaccount.withdraw()
savingAccount.withdraw()
checkingAccount.withdraw()
