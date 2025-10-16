#take user marks from user witg in 0 to 50
#if user enters [0-50] raise error invalidmarks using custom exception
#give chance to the user till, he/she enters valid marks

from ourpack import mark

while True:
    try:
        usermarks=int(input("Enter your marks (0-50): "))
        mark.validate_marks(usermarks)
        break
    except mark.InvalidMarks as im:
        print("Invalid marks:", im)

    choice=input("Do you want to try again? (yes/no): ").lower()
    if choice != 'y':
        print("Bereh")
        break
