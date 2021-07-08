import random
x = "y"
while x == "y":
    no = random.randint(1, 6)
    if no == 1:
        print("[     ]")
        print("[  0  ]")
        print("[     ]")
    if no == 2:
        print("[ 0   ]")
        print("[     ]")
        print("[   0 ]")
    if no == 3:
        print("[     ]")
        print("[0 0 0]")
        print("[     ]")
    if no == 4:
        print("[0   0]")
        print("[     ]")
        print("[0   0]")
    if no == 5:
        print("[0   0]")
        print("[  0  ]")
        print("[0   0]")
    if no == 6:
        print("[0 0 0]")
        print("[     ]")
        print("[0 0 0]")
    x = input("press y to roll again and n to exit:")
    print("\n")