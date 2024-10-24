l1 = [2, -3, 4]
l2 = [3, 1, -6]
l3 = [5, 1, 3]
def f1(a, b):
    return a[0]*b[0] + a[1]*b[1] + a[2] * b[2]
print(f1(l1, l2))
def f2(a, b):
    i = a[1]*b[2] - b[1]*a[2]
    j = (a[0]*b[2] - b[0]*a[2]) * -1
    k = a[0]*b[1] - b[0]*a[1]
    l = [i, j, k]
    return l
print(f2(l1, l2))
print(f2(l2, l3))
print(f1(f2(l2, l3), l1))
