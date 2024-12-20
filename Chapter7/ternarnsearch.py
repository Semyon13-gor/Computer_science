def ternary_search(arr, target):
    def search(arr, target, left, right):
        if left > right:
            return -1

        mid1 = left + (right - left) // 3
        mid2 = right - (right - left) // 3

        if arr[mid1] == target:
            return mid1
        elif arr[mid2] == target:
            return mid2
        elif target < arr[mid1]:
            return search(arr, target, left, mid1 - 1)
        elif target > arr[mid2]:
            return search(arr, target, mid2 + 1, right)
        else:
            return search(arr, target, mid1 + 1, mid2 - 1)

    return search(arr, target, 0, len(arr) - 1)


# Пример использования
sorted_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
index_of_five = ternary_search(sorted_numbers, 5)
print(index_of_five)  # Ожидаемый вывод: 4

index_of_ten = ternary_search(sorted_numbers, 10)
print(index_of_ten)  # Ожидаемый вывод: -1

# Тест 1
assert ternary_search([1, 2, 3, 4, 5, 6, 7, 8, 9], 5) == 4
# Тест 2
assert ternary_search([1, 2, 3, 4, 5, 6, 7, 8, 9], 3) == 2
# Тест 3
assert ternary_search([1, 2, 3, 4, 5, 6, 7, 8, 9], 1) == 0
# Тест 4
assert ternary_search([1, 2, 3, 4, 5, 6, 7, 8, 9], 10) == -1
# Тест 5
assert ternary_search([], 1) == -1  # Пустой массив
print("Все тесты пройдены!")