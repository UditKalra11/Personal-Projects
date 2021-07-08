x=int(input())
y=str(x)
k=1
z=[]
for i in range(len(y)):
    k=int(y[i])
    z.append(k**len(y))
if sum(z)==x:
    print("YESS")
else:
    print("NO")