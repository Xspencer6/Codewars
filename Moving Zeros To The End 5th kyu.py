"""
Write an algorithm that takes an array and moves all of the zeros to the end, preserving the order of the other elements.

move_zeros([1, 0, 1, 2, 0, 1, 3]) # returns [1, 1, 2, 1, 3, 0, 0]

"""


def move_zeros(lst):
    if len(lst) == 0:
        return []
    k = 0    # a pointer where the number of index of zeroes will start
    for i in range(len(lst)):
        if lst[i] != 0:
            # swap
            lst[k] = lst[i]
            k += 1
    # change all the remaining from k to last element to zero
    for j in range(k, len(lst)):
        lst[j] = 0
    return lst
