import datetime
import inspect
dtclassess = inspect.getmembers(datetime, inspect.isclass)

print('All Classes in datetime module')
for n, func in dtclassess:
    print(n, end='\t')

print('\n---Current time---\n')
print(datetime.datetime.now().time())

cttime=datetime.datetime.now().time()
formattedtime=datetime.datetime.now().strftime("%I %M %S %p")
print('Current time is:', cttime)
print('Formatted time is:', formattedtime)
