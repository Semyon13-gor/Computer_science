def move_zeros(lst):
    for i in range(len(lst)):
        if lst[i] == 0:
            del lst[i]
            lst.append(0)
    return lst
print(move_zeros([1, 0, 1, 2, 0, 1, 3])) # returns [1, 1, 2, 1, 3, 0, 0]