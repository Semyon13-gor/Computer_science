# 1. Стоимость предмета.
# 2. Время, которое грабитель тратит на укладку этого предмета в рюкзак.
# 3. Вес предмета.
def f(items, weight, time):
    best = 0
    weight_it = 0
    time_it = 0
    for item in items:
        weus = item[2]
        d = item[0]
        tius = item[1]
        for jtem in items:
            if (weus + jtem[2]) <= weight and not(item is jtem) and (tius + jtem[1]) <= time:
                d += jtem[0]
                weus += jtem[2]
                tius += jtem[1]
            else:
                if item is jtem:
                    continue
                if weight >= weus:
                    if best < d:
                        weight_it = weus
                        best = d
                        time_it = tius
                    d = 0
                    weus = 0
                    tius = 0
    return best,time_it ,weight_it

items_1 = [(10, 5, 2), (15, 4, 3), (30, 7, 5)]
time_limit_1 = 10
weight_limit_1 = 10

items_2 = [(20, 6, 4), (15, 3, 3), (25, 5, 5), (10, 2, 2), (12, 4, 3)]
time_limit_2 = 12
weight_limit_2 = 10

items_3 = [(15, 5, 3), (12, 4, 2), (30, 7, 5), (25, 6, 4), (20, 3, 3)]
time_limit_3 = 15
weight_limit_3 = 12

items_4 = [(10, 4, 2), (20, 5, 3), (15, 3, 2), (25, 6, 4), (18, 4, 3)]
time_limit_4 = 13
weight_limit_4 = 11

print(f(items_1,weight_limit_1 , time_limit_1))
print(f(items_2,weight_limit_2 , time_limit_2))
print(f(items_3,weight_limit_3 , time_limit_3))
print(f(items_4,weight_limit_4 , time_limit_4))