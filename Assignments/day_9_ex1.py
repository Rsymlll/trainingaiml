# writer a program that using function to find greates of three numbers entered by user

n1=int(input("Enter first number: "))
n2=int(input("Enter second number: "))
n3=int(input("Enter third number: "))
def greatest_of_three(a, b, c):
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c
greatest = greatest_of_three(n1, n2, n3)
print("The greatest number is:", greatest)
