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
5.A. Sliding Window Technique:

We are given an array, we need to find the maximum sum of k consecutive elements. The naive solution is simple, for every
beginning point at i we compute the next j<i+k elements and find their sum. We save the max sum in a variable. Using pythonic
array slicing method, this becomes more efficient. Slicing is O(k) for every element, thus, the time complexity is O(k*n).
We can however to this in O(n) time complexity using the sliding window technique. The steps in this algorithm ar as follows:
(i) Compute the sum of the first window, ie from 0 to k elements of the array. Initialise the current sum variable and the 
variable that stores the maximum sum of all windows (ie, maxsum), with this value.
(ii) Run a loop from i=k to i=n elements to traverse through the rest of the windows. To make a window for currsum slide, we
have to add the ith element to it so the window moves forward and subtract the first element of the previous window (i-k th).
[1,2,3,4,5], k=3
first window = [[1,2,3], 4, 5] currsum = 1+2+3 
to currsum add 4 subtract 1:
second window = [1,[2,3,4], 5] currsum = 1+2+3+4-1 = 2+3+4 and so forth.
(iii) Compare the currsum (window sum) with maximum and save it. If the problem is to find a given sum, this step would be to
check equality and return True if the window sum is equal to the given sum.
"""

import sys
def maxksum(arr,k):
    res  = - sys.maxsize
    for i in range(k, len(arr)+1):
        res = max(res, sum(arr[i-k: i])) # O(k)
    return res

def SlindingWindow(arr, k):
    # sum of first window elements:
    currsum = sum(arr[:k]); maxsum = currsum
    for i in range(k, len(arr)):
        currsum += arr[i] - arr[i-k]
        maxsum = max(currsum, maxsum)
    return maxsum

"""
5.B. Find subarray with specified sum (Positive Arrays): 

A variation of the sliding window problem is the value of k not being specified, For example, for a given array of 
non-negative integers, we have to find if the array contains a subarray whose sum is equal to the given value of sum. 
We can do this in O(n) time, but only if all the elements are positive. The efficient O(n) solution is a modified
Sliding window approach, where we compare the sum of the window with the given sumval and if its smaller then we add 
the next element, if its lesser then we subtract the previous elements of the window. In this way we need not compute
the k window when all elements are positive and our objective is just to find the sum.
"""
def findSubarraySum(arr, n, sumval):
    curr_sum = arr[0]; start = 0
    for i in range(1, len(arr)+1):
        # If curr_sum exceeds the sum, then remove the starting elements
        while (curr_sum > sumval and start < i-1):
            curr_sum -= arr[start]
            start += 1
        # If curr_sum becomes equal to sum, then return true
        if (curr_sum == sumval):
            print("Sum found between indexes %d and %d", start, i-1)
            return True
        # Add this element to curr_sum
        if (i < n):
            curr_sum += arr[i]
    # If we reach here, then no subarray
    print("No subarray found")
    return False

"""
5.C. N-bonacci Problem:

The N-bonacci problem is the larger version of fibonacci(n=2). Thus every element in an N-bonacci series, is the sum of the
previous n elements. in fibonacci since n=2 we take sum of previous two elements. We need to print m N-bonacci numbers.
We initialise the first n-1th and nth numbers as 0 and 1. Then we use the sliding window technique to form a window that
computes the sum of the previous n elements. for example in {0,0,1,1,X} where n = 3, we have ith element X = 1+1+0, and i-1th
element 1 = 1+0+0. We derive the relation that ith element = 2* i-1th element - i-n-1th element.
"""
def nBonacci(n, m):
    # initialise result array
    a = [0 for i in range(m)]
    a[n-1] = 1; a[n] = 1
    # Using sliding window
    for i in range(n+1, m):
        a[i] = 2 * a[i - 1] - a[i - n - 1]
    return a


"""
6.A. Prefix Sum Technique:

Given a fixed array we are required to find the most efficient way to process multiple sum queries. For example a function
getSum(start, end) should return the sum off arr[start:end+1]. The pythonic method is to do it using list/array slicing,
thus getSum(start, end) = sum(arr[start:end+1]) in O(n) time complexity. Another method would be to use the prefix sum 
technique, which is useful when there are many queries on the same array. We preprocess the array so that the multiple
queries made to the array take O(1) time complexity. To do this we compute the prefix sum array, where prefixsum(i) = 
sum of arr[0:i]. Each element is just the sum of the array ending with it. Thus when a query is made we can just index the sum.
For example, Array = [2,8,3,9,6,5,4], Prefix Sum Array = [2, 10, 13, 22, 28, 33, 37]. The code to perform this is given here:

To answer queries we need to keep in mind that every arr[i] now stores sum of all elements till i. Thus asking for the sum of 
elements in range (m,n) will be the nth element - the m-1th element. if m is zero then m-1 is also taken to be zero.
"""
def prefixsum(arr):
    # O(n) preprocessing 
    for i in range(1, len(arr)):
        arr[i] = arr[i-1] + arr[i]
    return arr

def sumqueries(arr):
    # for a large number of queries
    arr = prefixsum(arr)
    ip = input("Enter start and end: ").split(" ")
    start = int(ip[0]); end = int(ip[1])
    start = 0 if start == 0 else start - 1
    return arr[end] - arr[start]

"""
6.B. Given n ranges [(x1,y1), (x2,y2)...(xn, yn)] find the most commony appearing element in the n ranges:

The Naive solution is to compute the frequencies of m elements in n ranges in a hash table. This gives the most commonly
appearing element in O(n) time. A pythonic method can be to extend all the lists to compute one list comprising of mxn elements,
Then using Murrays Voting algorithm we can compute the most commonly appearing element in O(m*n) time. We can implement the
Prefix Sum Technique when the ranges are limited, as in 0 <= (xn,yn) <= 1000. We can solve this problem in O(n) time complexity.
The steps involved in this process:
(i) Make a dynamic array(list) of size 1000. For each index, we mark presence of the start of ranges in the array by incrementing
the corresponding index in the list. Then we mark the end of the ranges by decrementing its corresponding index in the list.
(ii) Thus when we compute prefix sum array of the list, at each element we would end up with the frequency of the index.
(iii) To get the index of the max element we can use pythonic functions or Murray's Voting Algorithm.
"""

def maxInNranges(x,y):
    n = len(x)
    maxOcc = [0 for _ in range(1000)]
    for i in range(n):
        maxOcc[x[i]] += 1
        maxOcc[y[i]+ 1] -= 1
    maxOcc = prefixsum(maxOcc)
    return maxOcc.index(max(maxOcc))

"""
7. Maximum Sum Sub-Array:

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
8. Longest Even Odd Sub-Array:

Find the length of the longest subarray that has alternating even-odd elements. The elements should be contiguous in nature.
The naive solution takes O(n*n) time and we traverse the whole loop to check all the subarrays of the array. We use modulus
conditions to check if the numbers are alternating even-odd or odd-even. The efficient solution of this problem can be done
in one traversal of the array. For every ith element we either extend the previous subarray (if it is alternating with i-1),
or start a new subarray by resetting the subarray length count variable. This would take O(n) time complexity.
"""
def evenOddSubarraySumN(arr):
    res = 0
    for i in range(len(arr)):
        count = 0
        for j in range(i+1, len(arr)):
            # condition to check alternating j-1th and jth elements.
            if((arr[j-1] % 2 == 0 and arr[j] % 2 != 0) or (arr[j-1] % 2 != 0 and arr[j] % 2 == 0)):
                count += 1
        res = max(res, count)
    return res

def evenOddSubarraySum(arr):
    count = 1; maxcount = 1
    for i in range(1, len(arr)):
        # continuing the subarray from i-1 th element
        if((arr[i-1] % 2 == 0 and arr[i] % 2 != 0) or (arr[i-1] % 2 != 0 and arr[i] % 2 == 0)):
            count += 1
            maxcount = max(count, maxcount)
        # starting a new subarray by resetting the count variable
        else:
            count = 1
    return maxcount

"""
9. Maximum Sum of Circular Sub-Arrays:

A circular sub array includes normal subarrays but also the subarrays formed by connecting the last element of the array with
the first element. For the Naive O(n*n) solution we take every i element and compute all subarrays for it, including the circular
subarrays and compute the current subarray sum. Then we take the maximum of these values. The i loop is to traverse the elements,
and j is used to generate subarrays of ith element. 

The efficient solution utilises Kadanes algorithm to compute sum for all normal subarrays. We treat the sum of circular subarrays
separately and then find the maximum of the two values. To solve this problem in O(n) time complexity the steps are as follows:
(i) Find normal max subarray sum using Kadane's algorithm
(ii) To compute max sum of circular subarrays the result is equal to the sum of the array - the min sum of normal subarrays
This is because we see that in circular subarrays we dont include the minimum sum normal subarrays, and the elements of circular
subarrays usually remain the same. Thus the total sum - minimum normal subarray sum gives the max circular subrray sum.
(iii) To compute minimum subrray sum, we invert the sign of all array elements and then use Kadane's max sum algorithm. On inverted
numbers the max sum is the min sum for the original array numbers.
"""

def circularSubarraySum1(arr):
    res = arr[0]
    for i in range(0, len(arr)):
        currsum = 0
        for j in range(1, len(arr)):
            idx = (i+j) % len(arr) # starts again from 0 for values > n
            currsum += arr[idx] # computing circular subarray sum for ith element
        res = max(res, currsum)
    return res

def circularSubarraySum(arr):
    normalMaxSubarraySum = KadanesAlgorithm(arr = arr) # O(n) time
    total = sum(arr)
    normalMinSubarraySum = KadanesAlgorithm(arr = [-i for i in arr])
    return max(normalMaxSubarraySum, total + normalMinSubarraySum)
