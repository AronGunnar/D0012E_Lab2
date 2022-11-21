from random import randrange
import cProfile
import time


# =============== Part One ===============
def incr_triple(lst):  # Todo: Check that its O(n).
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


def dac_triple(lst):  # Todo: Check that its O(n).
    if len(lst) == 3:
        return sort(lst)
    else:
        mid = len(lst) // 2
        lst_l = dac_triple(lst[mid:])
        lst_r = dac_triple(lst[:mid])

    lst_l = sort(lst_l)
    lst_r = sort(lst_r)
    for i, val_r in enumerate(lst_r):
        for j, val_l in enumerate(lst_l):
            if val_l < val_r:
                lst_r[i] = val_l
                lst_l[j] = val_r
                val_r = val_l

    return sort(lst_r)


def sort(lst):  # Insertionsort, since data set contains 3 elements no fancier sort is needed. (O(n^2), n = 3 => O(27))
    for j, val in enumerate(lst):
        i = j - 1
        while i >= 0 and lst[i] > val:
            lst[i + 1] = lst[i]
            i -= 1
        lst[i + 1] = val
    return lst


# =============== Part Two ===============


# =============== Testing/Printing ===============
if __name__ == '__main__':
    k = 3
    length = 3 * 2 ** (k - 1)  # Given in instructions, lenght of data set is always divisible by 3.
    a = [randrange(10) for i in range(length)]  # <---- Todo: Make elements is data set distinct.
    # a = [2, 6, 9, 3, 4, 7]  # For testing

    # ---------- Testing ----------

    # ---------- Printing ----------
    print("\nData set: ", a)
    # print("Smallest elements in set: ", incr_triple(a))
    print("Smallest elements in set: ", dac_triple(a))
