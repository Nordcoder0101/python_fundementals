class BankAccount:
  def __init__(self, balance=0, interestRate=0.01):
      self.balance = balance
      self.interestRate = interestRate

  def deposit(self, amount):
      self.balance += amount
      return self

  def withdraw(self, amount):
      self.balance -= amount
      if self.balance < 0:
          print('Insufficient funds: Charging a $5 fee')
          self.balance -= 5
          return self
      return self

  def display_account_info(self):
      print(self.balance)
      return self

  def yield_interest(self):
      balance += (balance * amount)
      return self

checking = BankAccount(1000000, .05)
savings = BankAccount(1000000, .05)

checking.deposit(500).deposit(600).deposit(300).withdraw(20000).display_account_info()
savings.deposit(2000).deposit(4000).withdraw(10000).withdraw(10000).withdraw(5000000).display_account_info()