grid = []
with open("setka.txt", "rt") as file:
    for line in file:
        li = []
        for i in line:
            if i != "*" and i != " " and i != "\n":
                li.append(i)
        grid.append(li)
print(grid)
gridst = []

for i in range(len(grid[1])):
    l = []
    for j in range(len(grid)):
        l.append(grid[j][i])
    gridst.append(l)
print(gridst)

gridd = []
with open("setka.txt", "rt") as file:
    m = []
    for line in file:
        li = []
        for i in line:
            if i != " " and i != "\n":
                li.append(i)
        m.append(li)
    mst = []
    for i in range(len(m[1])):
        l = []
        for j in range(len(m)):
            if m[j][i] != '*':
                l.append(m[j][i])
        mst.append(l)
    print(mst)
