import random

while True :
    print("Choices : ")

    print("Rock : 1")
    print("Paper : 2")
    print("Scissor : 3")
    print("Exit : 0")

    x = int(input("Enter Choice : "))

    if x==0 :
        break
    while x > 3 or x < 1:
        x = int(input("Enter Valid Choice : "))

    if x == 1:
        print("User Choice : Rock")
    elif x == 2:
        print("User Choice : Paper")
    elif x == 3:
        print("User Choice : Scissor")

    cc = random.randint(1, 3)
    if cc == 1:
        print("C Choice : Rock")
    elif cc == 2:
        print("C Choice : Paper")
    elif cc == 3:
        print("C Choice : Scissor")

    if x == 1:
        if cc == 1:
            print("Tie")
        if cc == 2:
            print("Lose")
        if cc == 3:
            print("Win")
    if x == 2:
        if cc == 1:
            print("Win")
        if cc == 2:
            print("Tie")
        if cc == 3:
            print("Lose")
    if x == 3:
        if cc == 1:
            print("Lose")
        elif cc == 2:
            print("Win")
        else:
            print("Tie")