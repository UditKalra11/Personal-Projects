def sum_rec(n):
    if n < 0:
        return "Enter a positive number"
    elif n == 0:
        return n
    else:
        return n+sum_rec(n-1)

print (sum_rec(16))