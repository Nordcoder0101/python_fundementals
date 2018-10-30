class User:
    def __init__(self, username, email_address):
        self.name = username
        self.email = email_address
        self.account_balance = 0
    def makeDeposit(self, amount):
        self.account_balance += amount

    def makeWithdrawl(self, amount):
        self.account_balance -= amount

    def display_user_balance(self):
        print(self.account_balance)

    def transfer_money(self, amount, recipiant):
        self.account_balance -= amount
        recipiant.account_balance += amount  

greg = User("Greg", "nords3x4@gmail.com")
joe = User("Joe", "joe@joeshmo.com")
ned = User("Ned", "nedisneat@ned.com")


greg.makeDeposit(10000)
greg.makeDeposit(10000)
greg.makeDeposit(10000)
greg.makeWithdrawl(50)
greg.display_user_balance()

joe.makeDeposit(50)
joe.makeDeposit(50)
joe.makeWithdrawl(10)
joe.makeWithdrawl(10)
joe.display_user_balance()

ned.makeDeposit(100)
ned.makeWithdrawl(10)
ned.makeWithdrawl(10)
ned.makeWithdrawl(10)
ned.display_user_balance()

greg.transfer_money(20, ned)
greg.display_user_balance()
ned.display_user_balance()
