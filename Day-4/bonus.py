def bonus(salary):
    return 0.1*salary

salary=float(input('Enter your salary to know your bonus: RM '))
bon=0.1*salary
total=salary+bon
print(f'Your bonus for this month is RM {bon}')
print(f'The total of your salary RM {salary} and bonus RM {bon} are: RM {total}')