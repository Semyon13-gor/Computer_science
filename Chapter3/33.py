def fac(n):
    if n > 0 and n % 2 != 0:
        return fac(n - 2) * n
    elif n > 0 and n % 2 == 0:
        return fac(n - 2) * n
    else:
        return 1
print(fac(6))
