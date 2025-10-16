class InvalidAge(Exception):
    pass    
def validate_age(age):
    if age<=0:
        raise InvalidAge("Age cannot be negative")
    elif age<18:
        raise InvalidAge("No underage allowed")
    elif age>120:
        raise InvalidAge("Age seems unrealistic")
    else:
        print (f"Valid age!!! Your {age} is accepted")

try:    
    userage=int(input("Enter your age: "))
    validate_age(userage)
except InvalidAge as ia:
    print("Invalid age:", ia)
except Exception as e:
    print("An error occurred:", e)