
# username=input("Enter your name: ")
# age=int(input("Enter your age: "))
# salary=float(input("Enter your salary: "))
# databaseKn=bool(input("Do you know database?"))
# print("Welcome Mr.\\Ms. ",username)
# print("Your age is ",age)
# print("Your salary is ",salary)
# print("Database Knowledge: ",databaseKn)

# adding 2 numbers
# num1=int(input("First Number: \t"))
# num2=int(input("Second Number: \t"))
# result=num1+num2
# print(f"Result after adding {num1} and {num2} = \t {result}")

# multiply two numbers
# num1=int(input("First Number: \t"))
# num2=int(input("Second Number: \t"))
# result=num1*num2
# print(f"Result after multiplication {num1} and {num2} = \t {result}")

# division two numbers
# num1=int(input("First Number: \t"))
# num2=int(input("Second Number: \t"))
# result=num1/num2
# print(f"Result after dividing {num1} by {num2} = \t {result}")

# % finding remainder example
# num1=int(input("First Number: \t"))
# num2=int(input("Second Number: \t"))
# result=num1%num2
# print(f"Remainder after dividing {num1} and {num2} = \t {result}")

# taking more than one input using single line
num1,num2=input("Enter two number seperated by space ").split()
result=int(num1)+int(num2)
print(f"Numbers Entered by you are {num1} and {num2} and the addition of two number is {result}")