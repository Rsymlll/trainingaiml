#write function from inches to cms
# 1 inch = 2.5cm

# def inch_to_cm(inch):
#     return inch * 2.5

# inch_value = float(input("Enter length in inches: "))
# cm_value = inch_to_cm(inch_value)
# print(f"{inch_value} inches is equal to {cm_value} centimeters.")

def gen_table(num):
    for i in range(1,11):
        print(f'{num}*{i}=\t{(num*i)}')
number=int(input('Enter number to findout table'))
gen_table(number)