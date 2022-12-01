from random import randrange
import random
import cProfile


# =================== Part One ===================
def incr_triple(lst):
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


def dac_triple(lst):
    if len(lst) == 3:
        return sort(lst)

    mid = len(lst) // 2
    lst_l = dac_triple(lst[mid:])
    lst_r = dac_triple(lst[:mid])

    for i, val_r in enumerate(lst_r):
        for j, val_l in enumerate(lst_l):
            if val_l < val_r:
                lst_r[i], lst_l[j], val_r = val_l, val_r, val_l

    return sort(lst_r)  # antal i sort


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


def max_sum(lst, lower, upper):
    if lower == upper:
        return Sum(lst[lower])

    mid = (lower + upper) // 2
    Left = max_sum(lst, lower, mid)
    Right = max_sum(lst, mid + 1, upper)

    optimalSum = Sum(0)

    optimalSum.total = Right.total + Left.total

    if Left.maxPrefix >= Left.total + Right.maxPrefix and Left.maxPrefix >= Left.total + Right.total:
        optimalSum.maxPrefix =  Left.maxPrefix
    
    elif Left.total + Right.maxPrefix >= Left.maxPrefix and Left.total + Right.maxPrefix >= Left.total + Right.total:
        optimalSum.maxPrefix = Left.total + Right.maxPrefix
    
    else:
        optimalSum.maxPrefix = Left.total + Right.total



    if Right.maxSuffix >= Right.total + Left.maxSuffix and Right.maxSuffix >= Right.total + Left.total:
        optimalSum.maxSuffix =  Right.maxSuffix
    
    elif Right.total + Left.maxSuffix >= Right.maxSuffix and Right.total + Left.maxSuffix >= Right.total + Left.total:
        optimalSum.maxSuffix = Right.total + Left.maxSuffix
    
    else:
        optimalSum.maxSuffix = Right.total + Left.total



    if optimalSum.maxPrefix >= optimalSum.maxSuffix and optimalSum.maxPrefix >= optimalSum.total and optimalSum.maxPrefix >= Left.maxSum and optimalSum.maxPrefix >= Right.maxSum and optimalSum.maxPrefix >= Left.maxSuffix + Right.maxPrefix:
        optimalSum.maxSum = optimalSum.maxPrefix
    
    elif optimalSum.maxSuffix >= optimalSum.maxPrefix and optimalSum.maxSuffix >= optimalSum.total and optimalSum.maxSuffix >= Left.maxSum and optimalSum.maxSuffix >= Right.maxSum and optimalSum.maxSuffix >= Left.maxSuffix + Right.maxPrefix:
        optimalSum.maxSum = optimalSum.maxSuffix
    
    elif optimalSum.total >= optimalSum.maxPrefix and optimalSum.total >= optimalSum.maxSuffix and optimalSum.total >= Left.maxSum and optimalSum.total >= Right.maxSum and optimalSum.total >= Left.maxSuffix + Right.maxPrefix:
        optimalSum.maxSum = optimalSum.total
    
    elif Left.maxSum >= optimalSum.maxPrefix and Left.maxSum >= optimalSum.maxSuffix and Left.maxSum >= optimalSum.total and Left.maxSum >= Right.maxSum and Left.maxSum >= Left.maxSuffix + Right.maxPrefix:
        optimalSum.maxSum = Left.maxSum
    
    elif Right.maxSum >= optimalSum.maxPrefix and Right.maxSum >= optimalSum.maxSuffix and Right.maxSum >= Left.maxSum and Right.maxSum >= Left.maxSum and Right.maxSum >= Left.maxSuffix + Right.maxPrefix:
        optimalSum.maxSum = Right.maxSum
    
    else:
        optimalSum.maxSum = Left.maxSuffix + Right.maxPrefix

    
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

    #cProfile.run("incr_triple(a)")
    #cProfile.run("dac_triple(a)")

    # --- Part Two ---
    print("\nData set: ", b)
    print("Sum of largest sub-array: ", max_sum(b, low, high).maxSum)

    cProfile.run("max_sum(b, low, high)")
