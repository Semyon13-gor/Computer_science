import math
for n in range(1, 1000):
    f = math.factorial(n)
    l = list(str(f))
    s = 0
    for i in l:
        s += int(i)
    if f % s != 0:
        print(n)
        break