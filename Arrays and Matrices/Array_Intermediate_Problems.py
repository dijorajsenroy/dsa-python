"""
1. Stocks Buy and Sell Problem:

We have an array containing stock prices. Find the maximum profit made for all pairs of cost and selling price of 
stock that are present in the array. Simply we have to find the peaks and the bottom points, we buy stock at bottom
points and sell at peak, and thus we make maximum profit. The O(n) solution of this problem is as follows:

This solution is based on the simple idea that we don't need to keep track of peaks and troughs, we can add the diff
of all the consecutive elements uphill and cumulatively that will give us the diff between trough and peak, and over
all such troughs and peaks we get max profit easily.
"""
def stocks(arr):
    profit = 0
    for i in range(1, len(arr)):
        if arr[i] > arr[i-1]:
            # adds to profit as long as we are uphill
            profit += arr[i] - arr[i-1]
    return profit

"""
2. Trapping Rain Water:

We have an array, whose values represent heights of bars. If the bars are arranged in the order of the array elements,
we have to compute how much water can be trapped between the first and last bar. We take the value of elements as one
unit of measurement of quantity. Thus an array arr = [2, 0, 2] would look like,
[ ]--[ ]
[ ]  [ ] 
and arr = [3, 0, 1, 2, 5] would look like,
           [ ]
           [ ]
[ ]--------[ ]
[ ]     [ ][ ]
[ ]  [ ][ ][ ]
Some usable facts about this problem: We can never store the water in leftmost(0) or rightmost(n-1) bars, all water has
to be enclosed in between. Hence we can iterate i=1 to n-1. for the above problem i takes values i = 1,2,3. To compute 
how much water can be stored in the ith bar, we see the largest bar to its right and left, which in this case is 0 and n-1.
We compute the height of lmax and rmax, the maximum amount of water cant be bigger than min(lmax, rmax) otherwise it would
overflow. Thus the water contained at ith bar = min(lmax, rmax) - arr[i](height of the bar). Then we sum all the units of 
water, this solution takes O(n*n) time. We can optimise this solution and make it O(n) time by making two arrays to store
lmax and rmax of all elements, thus making space complexity O(n).

trapwater = lambda arr: sum([min(max(arr[i:]), max(arr[:i+1])) - arr[i] for i in range(1, len(arr)-1)])
"""
def rainwater(arr):
    water = 0
    for i in range(1, len(arr)-1):
        # find largest bar to the right of i
        rmax = max(arr[i:])
        # find largest bar to the left of i
        lmax = max(arr[:i+1])
        water += min(rmax, lmax) - arr[i]
    return water

def rainwaterOn(arr):
    # initialising arrays to store lmax and rmax for all i's
    lmax = [0 for i in range(len(arr))]
    rmax = [0 for i in range(len(arr))]
    lmax[0] = arr[0]
    rmax[-1] = arr[-1]
    # computing maximum left bar for each ith element:
    for i in range(1, len(arr)):
        lmax[i] = max(lmax[i-1], arr[i])
    # computing maximum right bar for each ith element:
    for i in reversed(range(0, len(arr)-1)):
        rmax[i] = max(rmax[i+1], arr[i])
    # computing the sum of water contained in ith positions:
    res = 0
    for i in range(1, len(arr)-1):
        res += min(lmax[i], rmax[i]) - arr[i]

    return res
        
"""
3. Majority Element Problem:
"""
"""
4. Frequencies in a Sorted Array:
"""
def freqsorted(arr):
    count = 0
    arr.append(-1) # dummy element
    for i in range(1, len(arr)):
        if arr[i-1] == arr[i]:
            count += 1
        else:
            print(arr[i-1], count+1)
            count = 0

"""
5. Frequencies in an Unsorted Array
"""
# O(n*n) pythonic solution

def freqsorted1(arr):
    # obtain the list of unique numbers in arr
    uniq = list(set(arr))
    for i in uniq:
        print(i, arr.count(i))

"""
6. Sliding Window Technique:
"""
"""
7. Prefix Sum Technique:
"""
"""
8. Maximum Sum Sub-Array:
"""
"""
9. Longest Even Odd Sub-Array:
"""
"""
10. Maximum Circular Sum Sub-Array:
"""
