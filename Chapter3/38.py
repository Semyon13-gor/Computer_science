n = "4799 2739 8713 6272"
n = "".join(reversed(n))
m = []
for i in n:
    if i != " ":
        m.append(int(i))
print(m)
for i in range(0, len(m)):
    if i % 2 != 0:
        m[i] *= 2
        if m[i] > 9:
            s = 0
            for j in str(m[i]):
                s += int(j)
            m[i] = s
s = sum(m)
if s % 10 == 0:
    print("это номер кредитной карты")
else:
    print("это не номер кредитной карты")
