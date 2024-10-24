ls = []
mxh = 0
mxd = 0
with open("wood.txt", "rt") as file:
    h = []
    d = []
    for line in file:
        ls.append(line)
        st = line.split()
        h.append(st[-1])
        d.append(st[-2])
    del h[0]
    del h[0]
    del d[0]
    del d[0]
    mxh = max(h)
    mxd = max(d)
for i in ls:
    if str(mxh) in i or str(mxd) in i:
        print(i)
