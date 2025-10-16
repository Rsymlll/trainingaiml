import calc
import ex2

x=float(input('Choose your operation:   '))
print('1. Addition \n2. Average \n3. Multiplication \n4. Division \n5. Exit')
print('***************************')
firstNum=float(input("Enter first number : "))
secondNum=float(input("Enter second number: "))


if x==1:
        print(f'Total of {firstNum} and {secondNum} is ',calc.add(firstNum,secondNum))
elif x==2:
        print(f'Average of {firstNum} and {secondNum} is ',calc.avg(firstNum,secondNum))
elif x==3:
        print(f'Multiplication of {firstNum} and {secondNum} is ',calc.multi(firstNum,secondNum))
elif x==4:
        print(f'Division of {firstNum} and {secondNum} is ',calc.div(firstNum,secondNum))
elif x==5:
    print('Exit')
else:
    print('Invalid input')
ex2.findWinner()
