from ourpack import calc
while True:
    try:
        firstNum=float(input("Enter a number: "))
        secondNum=float(input("Enter another number: "))
        op=input('Choose operation (+,-,*,/): ')
        if op=='+':
            result=calc.add(firstNum,secondNum)
        elif op=='-':
            result=calc.sub(firstNum,secondNum)
        elif op=='*':
            result=calc.mul(firstNum,secondNum)
        elif op=='/':
            result=calc.div(firstNum,secondNum)
        else:
            print('Invalid operation')
            exit()
        print('The result is: ',(round(result,4)))
    except ZeroDivisionError as z:
        print("Division by zero is not allowed.", z)
    except ValueError as v:
        print("Invalid input. Please enter numeric values.", v)
    except Exception as e:
        print("An error occurred:", e)
    finally:
        print("Execution completed.")
    cont=input("Do you want to continue (y/n)? ").lower()
    if cont!='y':
        break