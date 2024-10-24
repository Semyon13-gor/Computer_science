a = [2, 4, 10, 6, 8, 4]
s = list(set(a))
d = 1 / (len(s) - 1)
dic = {}
for i in range(len(s)):
    dic[s[i]] = d*i
for i in range(len(a)):
    a[i] = dic[a[i]]
print(a)
