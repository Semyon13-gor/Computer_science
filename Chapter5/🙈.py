import random
import time

# Реализация сортировки слиянием
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left_list = merge_sort(arr[:mid])
    right_list = merge_sort(arr[mid:])

    return merge(left_list, right_list)
def merge(left, right):
    result = []
    left_index = right_index = 0
    left_length, right_length = len(left), len(right)

    for _ in range(left_length + right_length):
        if left_index < left_length and right_index < right_length:
            if left[left_index] <= right[right_index]:
                result.append(left[left_index])
                left_index += 1
            else:
                result.append(right[right_index])
                right_index += 1
        elif left_index == left_length:
            result.append(right[right_index])
            right_index += 1
        elif right_index == right_length:
            result.append(left[left_index])
            left_index += 1
    return result

# Реализация сортировки выбором
def selection_sort(arr):
    for i in range(len(arr)):
        mn = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[mn]:
                mn = j
            sw = arr[i]
            arr[i] = arr[mn]
            arr[mn] = sw


# Функция для генерации случайного списка заданной длины
def generate_random_list(length):
    return [random.randint(1, 1000) for i in range(length)]

def test():
    for size in [100, 1000, 10000, 100000]:
        arr = generate_random_list(size)
        start_time = time.time()
        merge_sort(arr.copy())
        merge_sort_time = time.time() - start_time

    # Измерение времени выполнения сортировки выбором
        start_time = time.time()
        selection_sort(arr.copy())
        selection_sort_time = time.time() - start_time

        print(f"Размер списка: {size}")
        print(f"Время выполнения сортировки слиянием: {merge_sort_time:.5f} сек")
        print(f"Время выполнения сортировки выбором: {selection_sort_time:.5f} сек")
        print("="*50)
if __name__ == "__main__":
    test()
