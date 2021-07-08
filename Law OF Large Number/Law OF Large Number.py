import numpy
from numpy.random import randn
n=int(input("Input:"))

y=randn(n)
c=0
for x in y:
    if x<1 and x>-1:
        c=c+1
print(c/n)