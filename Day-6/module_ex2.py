# import datetime
# import inspect
# print('Today is (date): ',datetime.date.today())
# dtclasses = inspect.getmembers(datetime, inspect.isclass)
# print('All classes inside datetime module')
# for n, func in dtclasses:
#     print(n)

# print('Today date is :',datetime.date.today())

# functions = inspect.getmembers(datetime.date, inspect.isbuiltin)
# for n, func in functions:
#     print(n)

# import os
# import inspect
# functions = inspect.getmembers(os, inspect.isbuiltin)
# for n, func in function:
#     print(n)
# print(os.listdir())

import os 
listDirs=os.listdir()
for dir in listDirs:
    print(dir)