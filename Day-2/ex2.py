# ourNum=1
# print("Printing numbers from 1 to 100")
# while ourNum<=100:
#     print(ourNum,end=" ")
#     ourNum+=1

#break example
# num=1
# print("Printing numbers from 1 to 100")
# while num<=100:
#     if(num%11==0):
#         break
#     print(num,end=" ")
#     num+=1

# num=1
# while num<=100:
#     if(num%2==0):
#         num+=1
#         continue    
#     print(num,end="\t")
#     num+=1

# for i in range(1,100):
#     if(i%5==0):
#         continue
#     print(i,end="\t")

correctPwd='syammil123'
counter=0
while True:
    pwd=input("Enter your password: ")
    if(correctPwd==pwd):
        print("You are logged in")
        print ('***Game Started!!!***')
        break
    else:
        counter+=1
        if (counter>=3):
            print('You have exceeded the maximum number of attempts')
            print('Blocked by system')
            break
        print('Wrong Password,Try Again')
        

    