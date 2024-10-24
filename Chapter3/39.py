import random
s = "Four score and seven years ago our fathers brought forth on this continent a new nation, conceived in liberty, and dedicated to the proposition that all men are created equal."

l = s.split()

for i in range(len(l)):
    if len(l[i]) > 4:
            lis = list(l[i])
            f = random.randint(1, len(l[i]) // 2)
            sec = 0
            if "," in l[i]:
                sec = random.randint(-1*(len(l[i]) // 2), -3)
            else:
                sec = random.randint(-1 * (len(l[i]) // 2), -2)
            p = lis[f]
            lis[f] = lis[sec]
            lis[sec] = p
            l[i] = "".join(lis)

news = " ".join(l)
print(news)