s1 = "adadadadffffaaa"
s2 = "adadfgggfffaahh"
c = 0
for i in range(len(s1)):
    if s1[i] != s2[i]:
        c += 1
print(c)
