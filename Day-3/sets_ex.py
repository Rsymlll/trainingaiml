# set_one={'laptop','mobile','tablet','mobile','headphone'}
# print('Number of items in the set:', len(set_one))
# for item in set_one:
#     print(item, end=" ")

#clear(): remove all the items from set
# set_one={'laptop','mobile','tablet','mobile','headphone'}
# set_one.clear()
# print("\nAfter clear the set items are:\t",len(set_one))
# for item in set_one:
#     print(item, end=" ")

# set_one={'laptop','mobile','tablet','mobile','headphone','ipad'}
# print('Number of items in the set:', len(set_one))
# for item in set_one:
#     print(item, end=" ")
# #set_one.remove(item): Update the set and removes item from the set
# set_one.remove('mobile')
# print('\nAfter removing one item from the set:',len(set_one))
# for item in set_one:
#     print(item, end=" ")

#union, intersection, difference
# set_one={100,200,300,400,500,700,900,1500}
# set_two={100,200,300,400,600,800,1000,1200}
# print(f'set_one contains: {len(set_one)}')
# print(f'set_two contains: {len(set_two)}')
# print(set_one)
# print(set_two)
# unionSet=set_one.union(set_two)
# print(f'Union of the set_one and set_two contains: {len(unionSet)} following items:')
# print(unionSet)

# set_one={100,200,300,400,500,700,900,1500}
# set_two={100,200,300,400,600,800,1000,1200}
# print(f'set_one contains: {len(set_one)}')
# print(f'set_two contains: {len(set_two)}')
# print(set_one)
# print(set_two)
# intersectionSet=set_one.intersection(set_two)
# print(f'Union of the set_one and set_two contains: {len(intersectionSet)} following items:')
# print(intersectionSet)

set_one={100,200,300,400,500,700,900,1500}
set_two={100,200,300,400,600,800,1000,1200}
print(f'set_one contains: {len(set_one)} items')
print(f'set_two contains: {len(set_two)} items')
print(set_one)
print(set_two)
newSet=set_one.difference(set_two)
print(f'Union of the set_one and set_two contains: {len(newSet)} following items:')
print(newSet)