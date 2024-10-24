a = [1, 2 ,3]
p = [1]*len(a)
print(p)
for i in range(len(p)):
    for j in range(len(a)):
        if j == i:
            continue
        p[i] *= a[j]
print(p)