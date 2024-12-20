def sort_twisted37(arr):
    maska = [1, 2, 7, 4, 5, 6, 3, 8, 9]
    for i in range(len(arr)):
        for j in range(len(arr)):
            if maska.index(arr[i]) < maska.index(arr[j]):
                el = arr[j]
                arr[j] = arr[i]
                arr[i] = el
    return arr

# Тест 1
print(sort_twisted37([1, 2, 3, 4, 5, 6, 7, 8, 9]))
print(sort_twisted37([7, 3, 3, 3, 7]))
assert sort_twisted37([1, 2, 3, 4, 5, 6, 7, 8, 9]) == [1, 2, 7, 4, 5, 6, 3, 8, 9]



# Тест 2
assert sort_twisted37([9, 2, 4, 7, 3]) == [2, 7, 4, 3, 9]

# Дополнительные тесты
# Тест 3
assert sort_twisted37([3, 7, 1, 2]) == [1, 2, 7, 3]

# Тест 4
assert sort_twisted37([7, 3, 3, 3, 7]) == [7, 7, 3, 3, 3]

# Тест 5
assert sort_twisted37([1, 2, 5, 3, 7]) == [1, 2, 7, 5,3]
print("Ok!")