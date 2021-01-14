"""
1.
There are two odd occurring elements in an array find them:
1. find xor of all array elements = xor
2. find rightmost set bit of xor = rsb
3. divide array into groups having 0 or 1 where xor has rsb, because 0 ^1 = 1 ^ 0 = 1
4. find xor of all of either groups which gives one odd occurring
"""
def two_odd_occur(arr):
    xor = 0
    for i in arr:
        xor ^= i
    rsb = xor & (~ ( xor - 1 ))
    group1 = 0; group2 = 0
    for i in arr:
        if i & rsb != 0:
            group1 ^= i
        else:
            group2 ^= i

    return group1, group2

print(two_odd_occur([3, 4, 3, 4, 5, 4, 4, 6, 7, 7]))

"""
2.
There is one odd occurring number in an array of numbers. Doing XOR of the entire array gives you
that number because all even occurring numbers become 0. since X^X=0.
"""
from functools import reduce
def one_odd_occurr(arr):
    return reduce(lambda a,b: a^b, arr)

"""
3.
Find if a number is a power of two or not. A power of two in binary is in the form of 100....0, and the
number before that would have 0 where it has set bit, thus performing and of both gives 0, as the only 
set bit is reduced to 0. the expression n & (n-1) makes the leftmost set bit 0 whereas n & ~(n-1) makes
the rightmost set bit 0
"""
def pow_of_2(n):
    return bool(n & (n-1) == 0)


