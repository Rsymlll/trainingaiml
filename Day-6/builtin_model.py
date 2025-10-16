#modules and package
# import math
# import random
# my_num=int(input('Enter your number to find out the square root :'))
# print(f'Square root of {my_num} is : ',math.sqrt(my_num))
# print('Your lucky random number ranged from 0 to 100 is :' ,random.randint(0,100))

#to check function inside module
# import math
# import inspect
# print(math.sin(45))
# functions = inspect.getmembers(math, inspect.isbuiltin)

# for n, func in functions:
#     print(n)

import math
import inspect

print('Sin 90 is: ',math.sin(90))
print('Cos 90 is: ',math.cos(90))
print('Tan 90 is: ',math.tan(90))

deg=int(input('Degree to find out cos'))
print(f'Cos{deg} is:    ',math.cos(deg))