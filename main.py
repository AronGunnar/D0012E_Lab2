from random import randrange
import random
import cProfile
import time


# =================== Part One ===================
def incr_triple(lst):  # TODO: Check that it's O(n).
    temp = []
    for i, val in enumerate(lst): # körs n gånger
        if len(temp) < 3:         # körs n gåner
            temp.append(val)
        else:
            temp = sort(temp)     #sorten

            for j in range(len(temp), 0, -1):
                if val < temp[j - 1]: # ger 3 comparisons
                    temp[j - 1] = val
                    break

    return sort(temp) #antal i sort


def dac_triple(lst):  # TODO: Check that it's O(n).
    if len(lst) == 3: # så många gånger det tar att splita listan så att listan är 3
        return sort(lst)

    mid = len(lst) // 2
    lst_l = dac_triple(lst[mid:])
    lst_r = dac_triple(lst[:mid])

    lst_l = sort(lst_l) #antal i sort
    lst_r = sort(lst_r) #antal i sort
    for i, val_r in enumerate(lst_r): # körs 3 gånger
        for j, val_l in enumerate(lst_l): #körs 3 gånger
            if val_l < val_r: #körs 9 gånger (3*3)
                lst_r[i], lst_l[j], val_r = val_l, val_r, val_l

    return sort(lst_r) #antal i sort


def sort(lst):  # Insertionsort, since data set contains 3 elements no fancier sort is needed. (O(n^2), n = 3 => O(27))
    for j, val in enumerate(lst): #3 lista long allstå for loppen 3 gånger
        i = j - 1
        while i >= 0 and lst[i] > val: # kör worst case med reversed list
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
    #print("\nData set: ", a)
    #print(length)
    #print(len(dis_lst))
    #print(dis_lst)
    #print("Smallest elements in set: ", incr_triple(a))
    #print("Smallest elements in set: ", dac_triple(a))

    #cProfile.run("incr_triple(a)")
    #cProfile.run("dac_triple(a)")

    # --- Part Two ---

    print("\nData set: ", b)
    print(2**k)
    print("Sum of largest sub-array: ", max_sum(b, low, high).maxSum)
    cProfile.run("max_sum(b, low, high)")

