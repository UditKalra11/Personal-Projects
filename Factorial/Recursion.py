def fac_rec(n):
    if n==1 or n==0:
        return 1
    elif n<0:
        return "ERROR : Negative Integer given"
    else:
        return n*fac_rec(n-1)

n=int(input())
print(fac_rec(n))