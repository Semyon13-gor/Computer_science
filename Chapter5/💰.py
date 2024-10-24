gold_prices_1 = [100, 120, 140, 160, 180, 200, 220]
gold_prices_2 = [200, 180, 220, 160, 240, 260, 210]
gold_prices_3 = [250, 230, 210, 190, 170, 150, 130]
gold_prices_4 = [200, 200, 200, 200, 200, 200, 200]
gold_prices_5 = [150, 160, 155, 170, 180, 175, 165]

def f(week):
    for i in range(len(week)):
        if week.index(min(week)) < week.index(max(week)):
            return (week.index(min(week)) + 1, week.index(max(week)) + 1, max(week) - min(week))
        else:
            del week[week.index(min(week))]
    return "Прибыли нет"

print(f(gold_prices_1))
print(f(gold_prices_2))
print(f(gold_prices_3))
print(f(gold_prices_4))
print(f(gold_prices_5))