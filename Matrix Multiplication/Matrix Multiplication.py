def mat (x,y):
    import numpy as np
    l1=[]
    for i in range (x):
        l=[]
        print("Enter Value of Row",i+1)
        for i in range(y):
            a=int(input())
            l.append(a)
        l1.append(l)
    m=np.array(l1)
    return m

print("Matrix 1 :")
r1=int(input("No. of Rows : "))
c1=int(input("No. of Columns : "))

m1=mat(r1,c1)

print("Matrix 2 :")
r2=int(input("No. of Rows : "))
c2=int(input("No. of Columns : "))

m2=mat(r2,c2)

print("\nMatrix 1 :\n\n%s\nMatrix 2 :\n\n%s" %(m1,m2))

def mul_mat(a,b):
    import numpy as np
    if a.shape[1] != b.shape[0]:
        print("Multiplication Not Possible")
    else:
        el1 = []
        for i in range(a.shape[0]):
            el = []

            for i in range(b.shape[1]):
                o = 0
                el.append(o)
            el1.append(el)

        em = np.array(el1)
        for i in range(len(m1)):
            for j in range(len(m2[0])):
                for k in range(len(m2)):
                    em[i][j] += m1[i][k] * m2[k][j]
        print("\n",em)

mul_mat(m1,m2)