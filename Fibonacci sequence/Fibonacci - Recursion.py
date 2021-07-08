def fib_rec (n):
    if n<=1:
        return n
    else:
        return fib_rec(n-1)+fib_rec(n-2)

n=int(input("Enter a number : "))
while n <=0:
    n=int(input("Please enter a positive integer : "))
print("Fibonacci series of",n,"is :")
for i in range(n):
    print(fib_rec(i))