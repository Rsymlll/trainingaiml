# price=num1=float(input("Enter product price: "))
# discount=price*0.10
# disPrice=price-discount
# print(f"Price: {price} \nDiscount {discount} \nDiscounted Price: {disPrice}")

# salary=50000.50
# bonus=5000.60
# print(f"Salary {salary} and Bonus {bonus}")
# salary+=bonus           #salary=salary+bonus
# print(f"Salary with Bonus: ",salary)

# salary=50000.50
# tds=salary*0.10
# print(f"Salary {salary} and TDS {tds}")
# salary-=tds           #salary=salary-tds
# print(f"Salary after TDS: ",salary)

#comparison operators: ==, >, >=, <, <=, !=

# age=int(input("Enter your age: "))
# if age>=18:
#     print("Eligible to vote")   
# else:
#     print("Not Eligible to vote")
# print("End of an application")

# marks=int(input("Enter marks percentage without %: "))
# if(marks<30):
#     print("Grade: E")
# else:
#     print("Passed")

#accessCode="wes12"
# accessCode=input("Enter access code: ")
# if(accessCode=="wes12"):
#     print("Welcome to your course")
# else:
#     print("Invalid Access Code")

#logical operators: and, or, not.
# phyMarks=int(input("Enter your marks obtained in Physics: "))
# cheMarks=int(input("Enter your marks obtained in Chemistry: "))
# mathMarks=int(input("Enter your marks obtained in Maths: "))

# if((mathMarks>=55) and  (phyMarks>=50) and (cheMarks>=60)):
#     print("You are eligible for admission")
# else:
#     print("You have not got the eligibility for admission")

# idProof=input("Enter ID Proof: ")
# if(idProof=="passport")or(idProof=="voterID")or(idProof=="drivingLicense"):
#     print(f"Valid id {idProof} we accept here")
# else:
#     print("Only passport, voterID and drivingLicense are accepted")
#     print(f"{id}: is not valid ID here")

mathMarks=int(input("Enter your marks obtained in Maths: "))
gapYear=int(input("Enter year gap if any otherwise zero: "))
if (mathMarks>=65) and (gapYear!=0):
    print("Not Eligible for BTech")
else:
    print("Elligible for BTech")