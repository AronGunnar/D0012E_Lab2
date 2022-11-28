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
def max_sum(lst, low , high):
    if (low == high):
        return lst[low]
    mid = (low + high) // 2
    maxLeft = max_sum(lst, low, mid)
    maxRight = max_sum(lst, mid+1, high)
    
    leftSum = -2147483647
    sum = 0

    for i in range(mid, low - 1, -1):
        sum = sum + lst[i]

        if sum > leftSum:
            leftSum = sum

    sum = 0
    rightSum = -2147483647

    for i in range(mid + 1, high + 1):
        sum = sum + lst[i]

        if sum > rightSum:
            rightSum = sum
    
    maxCross = leftSum + rightSum

    if maxLeft >= maxRight and maxLeft >= maxCross:
        return maxLeft
    elif maxRight >= maxLeft and maxRight >= maxCross:
        return maxRight
    else:
        return maxCross


        


# =============== Testing/Printing ===============
if __name__ == '__main__':
    # ------- List creation -------
    k = 3
    length = 3 * 2 ** (k - 1)  # Given in instructions, lenght of data set is always divisible by 3.
    a = [randrange(10) for i in range(length)]  # <---- TODO: Make elements in data set distinct.
    # b = [randrange(10) + 1 for i in range(2**k)]
    b = [4, 3, -10, 3, -1, 2, 2, -3, 5, 7, -4, -8, -10, 4, 7, -30]
    low = 0
    high = len(b) - 1

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
    print("Sum of largest sub-array: ", max_sum(b, low, high))
