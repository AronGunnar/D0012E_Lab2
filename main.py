from random import randrange
import cProfile
import time


# =============== Part One ===============
def incr_triple(lst):  # <---- Should be O(n)?
    temp = []
    for i, val in enumerate(lst):
        if len(temp) < 3:
            temp.append(val)
        else:
            temp = sort(temp)

            j = len(temp) - 1
            while j > 0:
                if val < temp[j]:
                    temp[j] = val
                    break
                j -= 1

    return sort(temp)


def dac_triple(lst):  # WIP
    sublsts = []
    # for i, val in enumerate(lst):
    #     sublsts.append([val])

    mid = len(lst) // 2

    if len(lst) >= 3:
        lst = dac_triple(lst[0:mid])

    if len(lst) > 1:
        return lst[0] if lst[0] < lst[1] else lst[1]

    return lst


def sort(lst):  # Insertionsort, since data set contains 3 elements no fancier sort is needed.
    for j, val in enumerate(lst):  # n-1
        i = j - 1
        while i >= 0 and lst[i] > val:
            lst[i + 1] = lst[i]
            i -= 1
        lst[i + 1] = val
    return lst


# =============== Part Two ===============


# =============== Testing/Printing ===============
if __name__ == '__main__':
    lst = [randrange(10) for i in range(10)]  # <---- Make elements is data set distinct.
    # lst = [9, 8, 2, 7, 3, 8, 9, 7, 0, 6]  # For testing

    # ---------- Printing ----------
    print(lst)
    print("Smallest elements in set: ", incr_triple(lst))
    # print("Smallest elements in set: ", dac_triple(lst))
