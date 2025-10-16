#default parameter in function

# def info(id,name,city='KL'):
#     print(f'Details as follows \n ID: {id} Name: {name} City: {city}')

# info(1,'Sam','New Delhi')
# info(101,'Xi')
# info(103,'Chong')

# def add(n1=0,n2=0,n3=0,n4=0,n5=0):
#     return n1+n2+n3+n4+n5
# print("Result:\t",add(1,2))
# print("Result:\t",add(13,4,10,9,5))
# print('Result:\t',add(75,98,100))

def findMax(*nums):
    return max(nums)
def findMin(*nums):
    return min(nums)
def findAvg(*nums):
    return findAvg(nums)

print('Max of 1,10,11 is: \t',max(1,10,11))
print('Max of 5,2 is: \t',max(5,2))
print('Max of 10,10,100,100,200,219,19 is: \t',max(10,10,100,100,200,219,19))

print('Min of 1,10,11 is: \t',min(1,10,11))
print('Min of 5,2 is: \t',min(5,2))
print('Min of 10,10,100,100,200,219,19 is: \t',min(10,10,100,100,200,219,19))

