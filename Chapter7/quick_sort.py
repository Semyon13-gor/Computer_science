import random # Using for  random.choice(deck)
def S(deckv):
	for i in range(len(deckv)):
		for j in range(len(deckv)):
			if deckv[i] < deckv[j]:
				el = deckv[j]
				deckv[j] = deckv[i]
				deckv[i] = el
	return deckv
def quick_sort_deck(deck):
	if len(deck) < 4:
		ndeck = S(deck)
		return ndeck
	else:
		deckr = []
		deckl = []
		op = deck[len(deck) // 2]
		for i in range(len(deck)):
			if op >= deck[i]:
				deckl.append(deck[i])
			if op < deck[i]:
				deckr.append(deck[i])
		deckr = S(deckr)
		deckl = S(deckl)
		ndeck = deckl + deckr
		return ndeck

# Пример использования
deck = [4, 2, 7, 1, 3, 5]
sorted_deck = quick_sort_deck(deck)
print(sorted_deck)  # Ожидаемый вывод: [1, 2, 3, 4, 5, 7]
# Тест 1
assert quick_sort_deck([4, 2, 7, 1, 3, 5]) == [1, 2, 3, 4, 5, 7]
# Тест 2
assert quick_sort_deck([10, 5, 3, 8]) == [3, 5, 8, 10]
# Тест 3
assert quick_sort_deck([1]) == [1]
# Тест 4
assert quick_sort_deck([3, 2]) == [2, 3]
# Тест 5
assert quick_sort_deck([7, 3, 3, 4, 1, 2, 5]) == [1, 2, 3, 3, 4, 5, 7]
print("OK!")
