kom = "FFFFFLFFFLFFFFRRRFXFFFFFFS"
pole=[]
for i in range(30):
    l = [" "]*30
    pole.append(l)
pole[14][14] = "0"
ug = 0
posx = 14
posy = 14
for k in kom:
    if k == "R":
        if ug >= 180:
            ug -= 90
        if ug < 180:
            ug += 90
        continue
    if k == "L":
        if ug >= 180:
            ug += 90
        if ug < 180:
            ug -= 90
        continue
    if k == "F" and ug == 0:
        posy -= 1
        pole[posy][posx] = "*"
    if k == "F" and ug == -90:
        posx -= 1
        pole[posy][posx] = "*"
    if k == "F" and ug == -180 or ug == 180:
        posy += 1
        pole[posy][posx] = "*"
    if k == "F" and ug == 90:
        posx += 1
        pole[posy][posx] = "*"
    if k == "S":
        break
for i in pole:
    print(*i)
