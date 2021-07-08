print("1.Add\n2.Subtract\n3.Multiply\n4.Divide")
op=int(input("Choose : "))

x=int(input("Enter 1st No. : "))
y=int(input("Enter 2nd No. : "))

if op == 1:
    z=x+y
elif op==2:
    z=x-y
elif op==3:
    z=x*y
else:
    z=x/y

print("Answer : ",z)