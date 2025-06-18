

from accounts import Account

class SavingsAccount(Account):  
    def __init__(self, initial_balance=50000):
        super().__init__()  
        self.balance = initial_balance  
        self.withdrawal_limit = 10000

    def savingsWithdraw(self, amount):
        if amount > 10000:
            return "Withdrawal amounts exceeds the limit."
        if amount > self.balance:
            return "Insufficient balance."
        else:
            self.balance -= amount
            return f"Withdrew {amount}. New balance: {self.balance}"


savings = SavingsAccount(50000)
savings.savingsWithdraw(0)
savings.deposit(0)          
