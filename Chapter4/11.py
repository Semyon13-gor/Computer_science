import math
n = int(input("n"))
mn = int(input("m"))
m = []
for i in range(n):
    m.append(int(input("Введите элемент массива")))
print(m)
for i in range(mn):
    l = int(input())
    r = int(input())
    k = int(input())
    for j in range(l - 1, r):
        n = j - (l - 1) + k
        c = math.comb(n, k)
        m[j] += c
print(m)
