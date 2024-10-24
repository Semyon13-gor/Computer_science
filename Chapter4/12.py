import math
s = int(input("Кол-во тестов"))
for t in range(0, s):
    n = int(input())
    k = int(input())
    sum = 0
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if j >= i:
                y = j - i
            else:
                y = i - j
            c = (math.factorial(k + y)) // (math.factorial(k)*math.factorial(y))
            sum += c
    print(sum)
