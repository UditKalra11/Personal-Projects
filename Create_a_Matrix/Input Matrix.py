import numpy as np
r=int(input("No. of Rows :"))
c=int(input("No. of Colmns :"))
l=[]
for i in range(r):
    print("Elements of Row %s" %(i))
    s=[]
    for i in range(c):
        x=int(input())
        s.append(x)
    l.append(s)
print(np.array(l))