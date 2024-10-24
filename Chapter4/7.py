def f(n, k):
    res = 0
    for i in range(1, 100):
        s = n // k**i
        res += s
        if s == 1:
            break
    return f"{k}^{res}"
print(f(10, 2))
