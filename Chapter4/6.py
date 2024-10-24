sharks = {}

with open("shark-species.txt", "rt") as file:
    s = ""
    r = ""
    v = ""
    for line in file:
        if line.count(" ") == 0:
            sharks[line.strip()] = {}
            s = line.strip()
        if line.count(" ") == 4:
            sharks[s][line.strip()] = {}
            r = line.strip()
        if line.count(" ") == 8:
            sharks[s][r][line.strip()] = {}
            v = line.strip()
        if line.count(" ") > 8:
            l = line.strip().split(":")
            sharks[s][r][v][l[0].strip()] = l[1].strip()
print(sharks['Lamniformes']['Lamnidae']['Carcharodon']['Carcharodon carcharias'])

