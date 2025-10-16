#inheritance
class Account:
    def __init__(self,ac_holder,bal):
        self.ac_holder=ac_holder
        self.bal=bal
    
    def deposit(self,amount):
        self.bal+=amount
        print('Balance after deposit',self.bal)

    def withdraw(self,amount):
        if (self.bal>=amount):
            bal-=amount
            print('Balance after withdraw: ' ,bal)
        else:
            print('Insufficient amount in account')
            print('Transaction Failed!!!')
    def show(self):
        print(f'Account Holder Name: {self.ac_holder} Account Balance {self.bal}')

# ac1=Account('Senayan', 45000)
# ac2=Account('Sepiah', 14000)
# ac1.show()
# ac2.show()

ac1=Account('Jebat', 50000)
ac1.show()
wamount=float(input('Enter amount to withdraw'))
ac1.withdraw(wamount)
