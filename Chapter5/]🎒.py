# 1. Вес предмета
# 2. Стоимость предмета

def f(items, weight):
    best = 0
    weight_it = 0
    for item in items:
        weus = item[0]
        d = item[1]
        for jtem in items:
            if (weus + jtem[0]) <= weight and not(item is jtem):
                d += jtem[1]
                weus += jtem[0]
            else:
                if item is jtem:
                    continue
                if weight >= weus:
                    if best < d:
                        weight_it = weus
                        best = d
                    d = 0
                    weus = 0
    return best, weight_it




items_1 = [(2, 10), (3, 15), (5, 30)]
weight_limit_1 = 5

items_2 = [(2, 10), (3, 15), (5, 30), (7, 20), (1, 5), (4, 10)]
weight_limit_2 = 10

items_3 = [(2, 20), (3, 15), (5, 30), (1, 25), (4, 10)]
weight_limit_3 = 7

items_4 = [(2, 5), (3, 8), (5, 15), (1, 3), (4, 10)]
weight_limit_4 = 7

items_5 = [(6, 10), (8, 15), (12, 30)]
weight_limit_5 = 5

print(f(items_1, weight_limit_1))
print(f(items_2, weight_limit_2))
print(f(items_3, weight_limit_3))
print(f(items_4, weight_limit_4))
print(f(items_5, weight_limit_5))