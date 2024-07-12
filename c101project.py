import random
print("do you want to roll a dice?")
answer=input("yes or no?")
while(answer=="yes"):
    no=random.randint(1,6)
    if no==1:
        print("|     |")
        print("|  X  |")
        print("|     |")
    if no==2:
        print("| X   |")
        print("|     |")
        print("|   X |")
    if no==3:
        print("| X X |")
        print("|     |")
        print("|  X  |")
    if no==4:
        print("| X X |")
        print("|     |")
        print("| X X |")
    if no==5:
        print("| X X |")
        print("|  X  |")
        print("| X X |")
    if no==6:
        print("|X X X|")
        print("|     |")
        print("|X X X|")
    print("do you want to roll a dice?")
    answer=input("yes or no?")