class Account:
    def __init___(self, balance, ac_holder):
        self.balance=balance
        self.ac_holder=ac_holder

    def get_balance(self):
        return self.balance
    
acc = Account(1000,'Syammil')
acc.balance = 34000
print(acc.balance)