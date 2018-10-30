import bankAccount

class User:
    def __init__(self, username, email_address):
        self.name = username
        self.email = email_address
        self.accounts = []
    def makeDeposit(self, amount, account):
        for i in range(0, len(accounts)):
            if accounts[i].name == account:
                self.accounts[i].balance += amount
                return self

    def makeWithdrawl(self, amount, account):
        for i in range(0, len(accounts)):
            if accounts[i].name == account:
                self.accounts.balance -= amount
                return self

    def display_user_balance(self, account):
          for i in range(0, len(accounts)):
              if accounts[i].name == account:
                  print(self.accounts.balance)
                  return self

    def transfer_money(self, amount, recipiant, accountFrom, AccountTo):
        self.makeWithdrawl(amount)
        recipiant.makeDeposit(amount)
        return self

    def makeAccount(self, balance, interestRate, accountName):
        self.accounts.append(bankAccount.BankAccount(balance = 1000000, interestRate = 0.03, accountName = accountName))   

greg = User("Greg", "nords3x4@gmail.com")


greg.makeAccount(1000000, 0.05, 'savings')
greg.makeAccount(1000000, 0.05, 'checking')
for i in range(len(greg.accounts)):
    print(greg.accounts[i].name)


# joe = User("Joe", "joe@joeshmo.com")
# ned = User("Ned", "nedisneat@ned.com")


# greg.makeDeposit(10000).makeDeposit(10000).makeDeposit(10000).makeWithdrawl(50).display_user_balnce()

# joe.makeDeposit(50).makeDeposit(50).makeWithdrawl(10).makeWithdrawl(10).display_user_balance()

# ned.makeDeposit(100).makeWithdrawl(10).makeWithdrawl(10).makeWithdrawl(10).display_user_balance()

# greg.transfer_money(20, ned).display_user_balance()
# ned.display_user_balance()

