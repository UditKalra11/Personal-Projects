from math import factorial
n = int(input("Enter a number : "))
for i in range(n):
    for k in range(n + 1 - i):
        print(end=" ") # for left spacing

    for j in range(1 + i):
        print(factorial(i) // (factorial(j) * factorial(i - j)), end=" ")
    print() # for new line
