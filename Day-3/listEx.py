# print("List Example One")

# champions = ["Garen", "Teemo", "Ahri", "Lux", 67, True]
# print('Number of items in the list:' ,len(champions))
# for lol in champions:
#     print(lol)

#sort example
# print("Sorting Example")
# names=["John", "Alice", "Bob", "Diana"]
# print("Before Sorting:", names)
# names.sort()
# print("After sorting:", names)

# print("Second Example of the list")
# emps=["Zaki", "John", "Azam", "Sara"]
# emps.sort()
# print("Number of employees:", len(emps))
# print("All Employees")
# for e in emps:
#     print(e, end=" ")
# print("\nEmployees in reverse order:")
# emps.reverse()
# for e in emps:
#     print(e, end=" ")

#append : adds the item at the end of the list

# emps=["Zaki", "John", "Azam", "Sara", "Mina", "Lina", "Lee", "Chong", "Wei"]
# print("Number of employee:", len(emps))
# for emp in emps:
#     print(emp, end=" ")
# newEmp=input("\nEnter new employee name to add:\t")
# emps.append(newEmp)
# print("\nAfter adding new employee: Number of employees are: ", len(emps))
# for emp in emps:
#     print(emp, end=" ")

#insert(index,item) mean it will add item at given index

# emps=["Zaki", "John", "Azam", "Sara", "Mina", "Lina", "Lee", "Chong", "Wei"]
# print("Number of employee:", len(emps))
# for emp in emps:
#     print(emp, end=" ")
# newEmp=input("\nEnter new employee name to add:\t")
# pos=int(input("Enter the position where you want to insert inside list :\t"))
# emps.insert(pos,newEmp)
# print("\nAfter adding new employee: Number of employees are: ", len(emps))
# for emp in emps:
#     print(emp, end=" ")

# emps=["Zaki", "John", "Azam", "Sara", "Mina", "Lina", "Lee", "Chong", "Wei"]
# print("Number of employee:", len(emps))
# for emp in emps:
#     print(emp, end=" ")
# #listName.remove(item): Will remove item from the list
# delEmp=input("\nChoose employee to remove from the list:\t")
# if delEmp in emps:
#     emps.remove(delEmp)
#     print(f"Number of employees after deleting {delEmp} in the list are:", len(emps))
#     for emp in emps:
#         print(emp, end=" ")
# else:
#     print(f"{delEmp} not found in the list")


#pop() example
emps=["Zaki", "John", "Azam", "Sara", "Mina", "Lina", "Lee", "Chong", "Wei"]
print("Number of employee:", len(emps))
for emp in emps:
    print(emp, end=" ")
#listName.pop(index): Will delete at given index and return its value
del_index=int(input("\nEnter the index to pop the items:\t"))
print(f"Item popped is: {emps.pop(del_index)}")

print(f"Number of employees after popping item at index {del_index} in the list are:", len(emps))
for emp in emps:
    print(emp, end=" ")