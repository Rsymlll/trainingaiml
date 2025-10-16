import random
def findWinner():
    name=input("Enter your name: ")
    luckyNumber=random.randint(1,10)
    print("Hello", name, "Your lucky number is", luckyNumber)
    if luckyNumber==2:
        print("You won a lottery of $1000")
    elif luckyNumber==4:
        print("You won a lottery of $500")
    elif luckyNumber==6:
        print("You won a lottery of $100")
    else:
        print("Sorry you won nothing, better luck next time")