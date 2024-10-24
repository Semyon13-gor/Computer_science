d = {
    "bk": ['0', 1, None],
    "br": ['1', 10, 1],
    "rd": ['2', 10**2, 2],
    "or": ['3', 10**2, None],
    "yl": ['4', 10**4, 5],
    "gr": ['5', 10**5, 0.5],
    "bl": ['6', 10**6, 0.25],
    "vi": ['7', 10**7, 0.1],
    "gy": ['8', 10**8, 0.05],
    "wh": ['9', 10**9, None],
    "au": [None, None, 5],
    "ag": [None, None, 10],
    "No": [None, None, 20]
}
def R(l):
    try:
        n1 = 0
        n2 = 0
        n3 = 1
        if d[l[0]][0] != None:
            n1 = d[l[0]][0]
        if d[l[1]][0] != None:
            n2 = d[l[1]][0]
        if d[l[2]][1] != None:
            n3 = d[l[2]][1]

        if d[l[3]][2] != None:
            return (int(n1 + n2) * n3, d[l[3]][2] )
        else:
            return (int(n1 + n2) * n3)
    except KeyError:
        print("Unidentified or invalid band colour in bands: ", l)
        return (None, None)
    except IndexError:
        print("Fewer than four colours provided in bands: ", l)
        return (None, None)
print(R(['br', 'bk', 'yl', 'ag']))
print(R(['yl', 'vi', 'rd', 'au']))
print(R(['vi', 'yl', 'rd', 'gr']))
print(R(['ws', 'yl', 'rd', 'rd']))
print(R(['vi', 'yl', 'rd']))
