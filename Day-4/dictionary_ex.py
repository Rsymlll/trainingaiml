# employee={'id':1,'name':'Sam','age':23,'salary':25000,}
# print('Employee Details as follows: ')
# for key, value in employee.items():
#     print(key, '->',value)

# employee['city']="Muscat"
# print('\nUpdated Dictionary after adding city:')
# for key,value in employee.items():
#     print(key,'->',value)

# del employee["salary"]
# print('\n Employee Details after deleting salary \n')
# for key, value in employee.items():
#     print(key, '->', value)

employee={'id':1,'name':'Sam','age':23,'salary':25000,}
print('All value from employee')
for k in employee.keys():
    print(k,end='\t')

employee={'id':1,'name':'Sam','age':23,'salary':25000,}
print('\nAll value from employee')
for v in employee.values():
    print(v,end='\t')

print('\n Key: Values\n')
for k,v in employee.items():
    print(k,' :\t ',v)

print('\nDictionary as follows')
print(employee)