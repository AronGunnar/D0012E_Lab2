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


class Sum:
    def __init__(self, val):
        self.total = val
        self.maxSum = val
        self.maxSuffix = val
        self.maxPrefix = val

def max_sum(lst, low , high):

    if (low == high):
        return Sum(lst[low])
    
    mid = (low + high) // 2
    Left = max_sum(lst, low, mid)
    Right = max_sum(lst, mid+1, high)
    
    optimalSum = Sum(0)

    optimalSum.total = Right.total + Left.total

    optimalSum.maxPrefix = max(Left.maxPrefix, Left.total + Right.maxPrefix, Left.total + Right.total)

    optimalSum.maxSuffix = max(Right.maxSuffix, Right.total + Left.maxSuffix, Right.total + Left.total)

    optimalSum.maxSum = max(optimalSum.maxPrefix, optimalSum.maxSuffix, optimalSum.total, Left.maxSum, Right.maxSum, Left.maxSuffix + Right.maxPrefix)
    
    return optimalSum
  


# =============== Testing/Printing ===============
if __name__ == '__main__':
    # ------- List creation -------
    k = 3
    length = 3 * 2 ** (k - 1)  # Given in instructions, lenght of data set is always divisible by 3.
    a = [randrange(-10,10) for i in range(length)]  # <---- TODO: Make elements in data set distinct.
    # b = [randrange(10) + 1 for i in range(2**k)]
    b = [(randrange(10) + 1)*(-1) if randrange(10) + 1 > 5 else randrange(10) + 1 for i in range(2**k)]
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
    print(2**k)
    print("Sum of largest sub-array: ", max_sum(b, low, high).maxSum)
    cProfile.run("max_sum(b, low, high)")

