class User:
    def __init__(self, username, email_address):
        self.name = username
        self.email = email_address
        self.account_balance = 0
    def makeDeposit(self, amount):
        self.account_balance += amount
        return self

    def makeWithdrawl(self, amount):
        self.account_balance -= amount
        return self

    def display_user_balance(self):
        print(self.account_balance)
        return self

    def transfer_money(self, amount, recipiant):
        self.makeWithdrawl(amount)
        recipiant.makeDeposit(amount)
        return self

greg = User("Greg", "nords3x4@gmail.com")
joe = User("Joe", "joe@joeshmo.com")
ned = User("Ned", "nedisneat@ned.com")


greg.makeDeposit(10000).makeDeposit(10000).makeDeposit(10000).makeWithdrawl(50).display_user_balance()

joe.makeDeposit(50).makeDeposit(50).makeWithdrawl(10).makeWithdrawl(10).display_user_balance()

ned.makeDeposit(100).makeWithdrawl(10).makeWithdrawl(10).makeWithdrawl(10).display_user_balance()

greg.transfer_money(20, ned).display_user_balance()
ned.display_user_balance()
