from random import randrange
import random
import cProfile
import time


# =================== Part One ===================
def incr_triple(lst):
    temp = []
    for i, val in enumerate(lst):  # körs n gånger
        if len(temp) < 3:  # körs n gåner
            temp.append(val)
        else:
            temp = sort(temp)  # sorten

            for j in range(len(temp), 0, -1):
                if val < temp[j - 1]:  # ger 3 comparisons
                    temp[j - 1] = val
                    break

    return sort(temp)  # antal i sort


def dac_triple(lst):
    if len(lst) == 3:  # så många gånger det tar att splita listan så att listan är 3
        return sort(lst)

    mid = len(lst) // 2
    lst_l = dac_triple(lst[mid:])
    lst_r = dac_triple(lst[:mid])

    for i, val_r in enumerate(lst_r):  # körs 3 gånger
        for j, val_l in enumerate(lst_l):  # körs 3 gånger
            if val_l < val_r:  # körs 9 gånger (3*3)
                lst_r[i], lst_l[j], val_r = val_l, val_r, val_l

    return sort(lst_r)  # antal i sort


def sort(lst):  # Insertionsort, since data set contains 3 elements no fancier sort is needed. (O(n^2), n = 3 => O(27))
    for j, val in enumerate(lst):  # 3 lista long allstå for loppen 3 gånger
        i = j - 1
        while i >= 0 and lst[i] > val:  # kör worst case med reversed list
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


def max_sum(lst, lower, upper):
    if lower == upper:
        return Sum(lst[lower])

    mid = (lower + upper) // 2
    Left = max_sum(lst, lower, mid)
    Right = max_sum(lst, mid + 1, upper)

    optimalSum = Sum(0)

    optimalSum.total = Right.total + Left.total

    optimalSum.maxPrefix = max(Left.maxPrefix, Left.total + Right.maxPrefix, Left.total + Right.total)

    optimalSum.maxSuffix = max(Right.maxSuffix, Right.total + Left.maxSuffix, Right.total + Left.total)

    optimalSum.maxSum = max(optimalSum.maxPrefix, optimalSum.maxSuffix, optimalSum.total, Left.maxSum, Right.maxSum,
                            Left.maxSuffix + Right.maxPrefix)

    return optimalSum


# =============== Testing/Printing ===============
if __name__ == '__main__':
    # ------- List creation -------
    k = 3
    length = 3 * 2 ** (k - 1)  # Given in instructions, lenght of data set is always divisible by 3.
    a = random.sample(range(-10, 10), length)
    b = [(randrange(10) + 1) * (-1) if randrange(10) + 1 > 5 else randrange(10) + 1 for i in range(2 ** k)]
    low = 0
    high = len(b) - 1

    # ---------- Testing ----------
    # Test code or calls to test functions..

    # ---------- Printing ----------
    # --- Part One ---
    # print("\nData set: ", a)
    # print("Smallest elements in set: ", incr_triple(a))
    # print("Smallest elements in set: ", dac_triple(a))

    # cProfile.run("incr_triple(a)")
    # cProfile.run("dac_triple(a)")

    # --- Part Two ---
    print("\nData set: ", b)
    print("Sum of largest sub-array: ", max_sum(b, low, high).maxSum)

    # cProfile.run("max_sum(b, low, high)")
