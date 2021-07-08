x=int(input("Enter number of terms : "))
n1=0
n2=1
c=2
l=[0,1]
while c<x:
    nth=n1+n2
    l.append(nth)
    n1=n2
    n2=nth
    c=c+1
print(l)