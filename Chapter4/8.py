
def f(k1):
    k2 = k1 + 1
    for i in range(1, 10000000):
       n1 = i * k1
       n2 = i * k2
       nl = list(str(n1))
       f = True
       for j in range(len(nl)):
           if str(n1).count(nl[j]) != str(n2).count(nl[j]):
               f = False
       if f == True:
           return i

print(f(100))
print(f(325))