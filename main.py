from random import randrange
import cProfile
import time


# =================== Part One ===================
def incr_triple(lst):  # TODO: Check that it's O(n).
    temp = []
    for i, val in enumerate(lst):
        if len(temp) < 3:
            temp.append(val)
        else:
            temp = sort(temp)

            for j in range(len(temp), 0, -1):
                if val < temp[j - 1]:
                    temp[j - 1] = val
                    break

    return sort(temp)


def dac_triple(lst):  # TODO: Check that it's O(n).
    if len(lst) == 3:
        return sort(lst)

    mid = len(lst) // 2
    lst_l = dac_triple(lst[mid:])
    lst_r = dac_triple(lst[:mid])

    lst_l = sort(lst_l)
    lst_r = sort(lst_r)
    for i, val_r in enumerate(lst_r):
        for j, val_l in enumerate(lst_l):
            if val_l < val_r:
                lst_r[i], lst_l[j], val_r = val_l, val_r, val_l

    return sort(lst_r)


def sort(lst):  # Insertionsort, since data set contains 3 elements no fancier sort is needed. (O(n^2), n = 3 => O(27))
    for j, val in enumerate(lst):
        i = j - 1
        while i >= 0 and lst[i] > val:
            lst[i + 1] = lst[i]
            i -= 1
        lst[i + 1] = val
    return lst


# =================== Part Two ===================
def max_sum(lst):
    # if len(lst) > 1:
    #     mid = len(lst) // 2
    #     lst_l = max_sum(lst[:mid])
    #     lst_r = max_sum(lst[mid:])
    #     return lst_l if sum(lst_l) > sum(lst_r) else lst_r
    # return lst

    if len(lst) > 1:
        mid = len(lst) // 2
        lst_l = max_sum(lst[:mid])
        lst_r = max_sum(lst[mid:])

        sum_left = sum(lst_l)
        sum_right = sum(lst_r)
        sum_total = sum_left + sum_right

        if sum_left > sum_total:
            sum_total = sum_left
        if sum_right > sum_total:
            sum_total = sum_right

    return lst


# =============== Testing/Printing ===============
if __name__ == '__main__':
    # ------- List creation -------
    k = 3
    length = 3 * 2 ** (k - 1)  # Given in instructions, lenght of data set is always divisible by 3.
    a = [randrange(10) for i in range(length)]  # <---- TODO: Make elements in data set distinct.
    # b = [randrange(10) + 1 for i in range(2**k)]
    b = [1, -2, -4, 10, -7, 8, 7, 1, -1]

    # ---------- Testing ----------
    # Test code or calls to test functions..
    # total = 0
    # c = [total := total + i for i in b]  # If built in function sum can't be used.

    # ---------- Printing ----------
    # --- Part One ---
    # print("\nData set: ", a)
    # print("Smallest elements in set: ", incr_triple(a))
    # print("Smallest elements in set: ", dac_triple(a))

    # --- Part Two ---
    print("\nData set: ", b)
    print("Sum of largest sub-array: ", max_sum(b))
