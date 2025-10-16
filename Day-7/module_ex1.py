import math
import inspect

# num=int(input("Enter a number to find out square root: "))
# print("The square root of", num, "is", round(math.sqrt(num)))

functions = inspect.getmembers(math, inspect.isbuiltin)
print('All function in math module')
for n, function in functions:
    print(n, end='\t')