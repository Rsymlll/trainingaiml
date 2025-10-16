def add(num1,num2):
    return num1+num2
def multi(num1,num2):
    return num1*num2
def minus(num1,num2):
    return num1-num2
def div(num1,num2):
    return num1/num2
def avg(num1,num2):
    return (num1+num2)/2

print('Welcome to mini calculator')
while True:
    print('Select Operation: \n1.Add \n2.Sub \n3.Multi \n4.Division \n5.Average \n6.Exit')
    op=int(input('Choose your operation(1-6):\t'))
    if(op==6):
        print('Adios')
        break
    if((op>6) or (op<=0)):
        print('Wrong operation choice, only 1 to 6 are allowed')
        continue
    fnum=float(input('Enter the first number:\t'))
    snum=float(input('Enter the second number:\t'))
    if(op==1):
        print(f'Result after adding {fnum} and {snum}:\t',add(fnum,snum))
    elif(op==2):
        print(f'Result after minus operation for {fnum} and {snum}:\t',minus(fnum,snum))
    elif(op==3):
        print(f'Result after multiplication for {fnum} and {snum}:\t',multi(fnum,snum))
    elif(op==4):
        print(f'Result after dividing for {fnum} and {snum}:\t',div(fnum,snum))
    elif(op==5):
        print(f'Result for average number between {fnum} and {snum}:\t',avg(fnum,snum))
    else:
        print("Beep beep beep\nsalah\nbuat lain")