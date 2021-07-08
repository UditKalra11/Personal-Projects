n=int(input("Enter The Number : "))

fact=1
while n<0:
    n=int(input("Please enter a positive value : "))

if n>=0:

    for i in range(1,n+1):
        fact=fact*i
    print("Factorial of %s = %s" %(n,fact))