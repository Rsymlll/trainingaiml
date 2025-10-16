class Account:
    def __init__(self,ac_holder,bal):
        self.ac_holder=ac_holder
        self.bal=bal
    
    def deposit(self,amount):
        self.bal+=amount
        print('Balance after deposit: RM',self.bal)

    def withdraw(self,amount):
        if (self.bal>=amount):
            self.bal-=amount
            print('Balance after withdraw: RM' ,self.bal)
        else:
            print('Insufficient amount in account')
            print('Transaction Failed!!!')
    def show(self):
        print(f'Account Holder Name: {self.ac_holder} Account Balance {self.bal}')

ac = Account('Sam', 15000)
x=int(input('Please choose \n 1.Deposit 2.Withdraw '))

if x==1:
    amount=float(input('Please enter your amount to deposit: '))
    ac.deposit(amount)
elif x==2:
    amount=float(input('Please enter your amount to withdraw: '))
    ac.withdraw(amount)
else:
    print('Invalid choice')