def factorial(num):
    if((num==0)or(num==1)):
        return 1
    else:
        return num*factorial(num-1)
num=int(input('Enter a number to find out factorial '))
print(f'Factorial of {num} is= {factorial(num)}')