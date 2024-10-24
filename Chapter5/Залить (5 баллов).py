import copy
import math
arr = [None, 1, None, None, None, 2, None]
arr1 = [None, 1, None, None, None, 2, None]
arr2 = [None, 1, None, None, None, 2, None]
def fill(arr, com):
    for el in arr:
        if el is None:
            if com == -1:
                for i in range(arr.index(el), len(arr)):
                    if not(arr[i] is None):
                        arr[arr.index(el)] = arr[i]
                        break
        if not(el is None):
            if com == 1:
                for i in range(arr.index(el) + 1, len(arr)):
                    if arr[i] is None:
                        arr[i] = el
                    else:
                        break
    if com == 0:
        arrc = copy.deepcopy(arr)
        for i in range(len(arr)):
            if arr[i] is None:
                lel = [0, 0]
                rel = [0, 0]
                for j in range(len(arr)):
                    if not(arrc[j] is None) and j < i:
                        lel[0] = arrc[j]
                        lel[1] = j
                    if not(arrc[j] is None) and j > i:
                        rel[0] = arrc[j]
                        rel[1] = j
                        break
                if abs(i - rel[1]) < abs(i - lel[1]) or abs(i - lel[1]) == 0:
                    arr[i] = rel[0]
                elif abs(i - rel[1]) > abs(i - lel[1]) or abs(i - rel[1]) == 0:
                    arr[i] = lel[0]
                else:
                    if lel[1] == 0:
                        arr[i] = rel[0]
                    if rel[1] == 0:
                        arr[i] = lel[0]
                    else:
                        arr[i] = min(rel[0], lel[0])
    return arr
print(fill(arr, -1))  # None заменено ближайшим int справа
print(fill(arr1,  0))
print(fill(arr2, 1))  # None заменено ближайшим int слева