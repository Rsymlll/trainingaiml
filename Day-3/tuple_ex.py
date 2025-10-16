# subjects=('python','java','d'
# 'otnet','javascript','html','css')
# print("\nAll subjects are: \n")
# print('\nNumber of subjects: ', len(subjects))
# for sub in subjects:
#     print(sub, end="\t")

# numbers=(1,2,3,4,10,2,3,2,3,5,50)
# print("All numbers are: ",len(numbers))
# for num in numbers:
#     print(num, end="\t")
#tupleName.index(item) will return the index of first occurrence of tupleName
# search_num=int(input("\nEnter number to search in the tuple:\t"))
# if search_num in numbers:
#     print(f'Index of {search_num} is:', numbers.index(search_num))
# else:
#     print(f'No such number {search_num} in the tuple')

#tupleName.count(item) tupleName to count(item) will return the count of item in the tuple

# numbers=(1,2,3,4,10,2,3,2,3,5,50)
# print("All numbers are: ",len(numbers))
# for num in numbers:
#     print(num, end="\t")
# search_num=int(input("\nEnter number to find out the frequency:\t"))
# if search_num in numbers:
#     print(f'Number: {search_num} frequency is: {numbers.count(search_num)}\t')
# else:
#     print(f'No such number {search_num} in the tuple')

#write a program to sum a list with 4 numbers.

numbers=(10,20,30,40)
total=0
for num in numbers:
    total+=num
print("\nTotal of all numbers in the list is:\t", total)