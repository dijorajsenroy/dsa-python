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
3. Equillibrium Index of Array:

The equillibrium index of an array is the index such that the sum of elements preceding it equals the sum of
elements following it. The naive solution would be to compute the subarray sums of all elements before and after
for each element. This would take O(n*n) time complexity. The better O(n) solution would be to first obtain the 
total sum of the array, then traverse the array and add elements to the left sum. The right sum would be the 
total - current element - left sum. When these values are equal we have our element index.
"""
def equillibrium(arr):
    total = sum(arr)
    leftsum = 0
    for i in range(len(arr)):
        rightsum = total - arr[i] - leftsum
        if leftsum == rightsum:
            return i
        else:
            leftsum += arr[i]

"""
4. Majority Element Problem:

An element in an array is called a majority if it appears more than n/2 times. The simple pythonic O(n*n) solution
is to use list count in a loop traversing the arrays. The efficient solution takes O(1) auxillary space and
O(n) time complexity. It is known as Murray's Voting Algorithm. The first phase of the algorithm, finds a candidate,
if there is a majority element the candidate is the majority element. The second phase checks if the candidate is 
the majority element in the array. The second phase is not required if there is always a majority element in the array.
In the first phase we intialise the first element as majority and take its count=1. Then we traverse the array and check
if the current element is the same as the majority. If same, we increment count, if its not then we decrement. if count is
0 we reset both the current majority and count
"""

def majority(arr):
    for i in range(len(arr)):
        if arr.count(arr[i]) > len(arr)//2:
            return i
    return -1


def MurraysVotingAlgorithm(arr):
    # 1st phase gives a candidate for majority element
    res = 0
    count = 1
    for i in range(1, len(arr)):
        if arr[res] == arr[i]:
            count += 1
        else:
            count -= 1
        if count == 0:
            # resetting
            res = i
            count = 1
    # 2nd phase to check majority element:
    if arr.count(arr[res]) > len(arr)//2:
        return res
    else:
        return -1

"""
6. Sliding Window Technique:
"""
"""
7. Prefix Sum Technique:
"""
"""
8. Maximum Sum Sub-Array:

Given an array we have to compute the maximum sum that a subarray of the array posesses, where a subarray is a subset of
contiguous elements present in the array. When there are negative elements the max sum is not the sum of all elements. Thus 
We have to generate all subarrays and check their sums. The naive solution is to use two loops to make all subarrays and store
the sum and maximum sum in two variables. for an ith element we run a loop i+1 to n, which gives all subset sums in O(n*n) time.

The efficient method to do this is using Kadane's algorithm to compute maximum subarray sum, in O(n) time complexity. Steps:
(i) We traverse the elements from left to right and for ith element we compute the max subarray sum, for subarrays ending with i.
(ii) To compute the max sum of i elements we add ith element to the max sum of i-1 elements and thus re-use the previous sum 
(iii) After computing the maximum ending sum of all i elements we find the max of these values and that gives the result.

Thus the recursive statement for this problem will be formed as:
Sum(i) = max(Sum(i-1) + arr[i], arr[i])
This works by starting a new subarray when the previous sum is smaller, or else adding to the same subarray. For example in 
the given array [-5, 2, -2, 4], the maxEnding sum is starting with -5 at 0th index. at 1st index since 2 > -5+2 its 2, at third
index its 0, and at 4th its 4. The idea of this algorithm is that the greatest maxEnding sums wuld produce the max sum. 
"""
import sys
def maxSumNaive(arr):
    res = - sys.maxsize
    for i in range(0, len(arr)):
        currsum = arr[i]
        for j in range(i+1,len(arr)):
            currsum += arr[j]
            res = max(res, currsum) 
    return res


def KadanesAlgorithm(arr):
    # max ending sum initialised with first element
    maxEndingSum = arr[0]
    maxSubarraySum = 0
    for i in range(1, len(arr)):
        # continuing subarray sum or starting a new one
        maxEndingSum = max(maxEndingSum + arr[i], arr[i])
        # saving max subarray sum
        maxSubarraySum = max(maxSubarraySum, maxEndingSum)
    return maxSubarraySum

"""
9. Longest Even Odd Sub-Array:
"""
"""
10. Maximum Circular Sum Sub-Array:
"""
