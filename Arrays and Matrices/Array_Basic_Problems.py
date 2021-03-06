"""
Basic Operations:

1. Insert an element at index I O(n):
2. Delete at element at index I O(n):
3. Updating elements at index I O(1):
4. Traversal of the array:
5. Reversing the array (O(n)):
6  Maximum element and Minimum element O(n):
"""

# Using lists in python :
lis = [1,2,3,4,5,6,7,8,9]
lis.insert(3, 54)
lis.append(10)
lis.remove(9)
lis[2] = 24
for i in lis: i
lis[::-1]

# Using array module (faster method)
import array as a 
arr = a.array('i', lis)
arr.insert(len(arr), 11)
arr.remove(arr[5])
arr[3] = 69
for i in arr: i
arr[::-1]

# O(nlogn) sorting in python(Timsort - adaptive merge sort):
sorted(arr)

# O(n) searching in python:
arr.index(69)

# Maximum and minimum is found using python inbuilt functions:
max(arr)
min(arr)

"""
1. Array Rotations (by 1 or D places): 

Left rotating an array by one place means simply adding the 0th element to the end of the array.
In fixed sized arrays append operations don't exist. So we need to copy the 0th element in a temp variable,
shift all the elements to the left by one position and swap the temp variable with the last index. This
takes one traversal of the array and thus O(n) time. Using the pythonic methods, would help us write a simpler code
but with the same time complexity, and using list makes appending quicker in constant time.

Left rotating by D places can be done Naively, in O(nd) time by repeating leftRotateby1 d times. Alternatively,
we can do this in a method that takes O(n) time and O(1) auxillary space. The steps involved in this are:
(i) Reverse the first D elements
(ii) Reverse Dth element to last element
(iii) Reverse the entire array
We use pythonic reversal and list concatenation for simpler code in the same time complexity
"""
def leftRotateby1(arr):
    # arr = arr[1:] + [arr[0]] if arr is list: constant time
    # arr.insert(len(arr), arr[0])[1:] if arr is array: O(n) time
    temp = arr[0]
    for i in range(1,len(arr)):
        arr[i-1] = arr[i]
    arr[len(arr)-1] = temp
    return arr

def leftRotatebyD(arr, d):
    # reverse the first d elements
    arr = arr[0:d][::-1] + arr[d:]
    # reverse the d to n elements
    arr = arr[0:d] + arr[d:][::-1]
    # reverse the whole array
    arr = arr[::-1]
    return arr

"""
2. Remove Duplicates from sorted array:

The first method has O(n^2) time because of 'in' operator being used on an unhashable
sequential data type, and O(n) space complexity because new array is being created.

In the second method we create a dummy array and initialise with copying the first element.
Then we traverse the array and check if the k-1th element in the result array is equal to the 
kth element of the array (duplicate). if its not then we add the item in position k. The rest remain 0.
the loop variable k records the position where the element is last filled and hence rest must be empty.
This method takes O(n) time complexity and O(n) space complexity.

In the third method, we copy the elements within the array itself. We dont use a buffer array thus it 
takes O(n) time complexity and O(1) space complexity.
"""
def removedups1(arr):
    res = []
    for i in arr:
        # in performs search taking O(n) time
        if i not in res: 
            res.append(i)
    return len(res)

def removedups2(arr):
    res = a.array('i', [0 for i in range(len(arr))])
    res[0] = arr[0]
    k = 1
    for i in arr:
        if res[k-1] != i:
            res[k]=i
            k += 1
    return k 

def removedups3(arr):
    res = 1
    for i in range(1, len(arr)):
        if arr[res-1] != arr[i]:
            arr[res] = arr[i]
            res += 1
    return res

"""
3. Largest and second largest elements:
"""
import sys
def max2(arr):
    fmax = max(arr) # O(n) time
    smax = - sys.maxsize
    for i in arr: # O(n) time
        if smax < i and i != fmax:
            smax = i
    return fmax, smax

"""
4. Move Zeroes to the right end of the array:

The Naive solution is simple and uses two loops. The first one is to find a ai = 0, the second
one is to swap it with the first non-zero element to its right. This takes O(n*n) time, and instead,
we will make a variable to remove the function of the loop here. We make a variable count, which is 
incremented whenever we encounter a non-zero element and used to keep track of non zero elements.
We swap the current element with the element at count:
(i) if its a non-zero element before any zero is encountered, its swapped with itself.
(ii) if its a non-zero element after x zeros have been encountered it is swapped with the position which contains 0,
which is count. Thus count keeps track of the element that is to be swapped.

"""
def moveZeros(arr):
    count = 0
    for i in range(len(arr)):
        if arr[i] != 0:
            arr[i], arr[count] = (arr[count], arr[i])
            count += 1
    return arr

"""
5. Leaders in an Array Problem:

An element is a leader in an array if there is no element to its right that is greater than itself. A
naive solution is to find the maximum element in the sum array of each index. Thus it takes O(n*n) time.
The efficient method is to start traversing from the last element (which is always a leader), this is stored
as a current leader. Then we traverse a loop from right to left to check if current element is greater than
stored leader, which means that the current element is also a leader. This takes O(n) time complexity.
"""
def leader(arr):
    curr_leader = arr[-1]
    print(curr_leader)
    # loop to access in reverse order
    for i in range(len(arr)-2,-1,-1):
        if arr[i] > curr_leader:
            curr_leader = arr[i]
            print(curr_leader)

"""
6. Maximum Difference Problem:

We are required to find the largest value of arr[j] - arr[i] considering j > i at all times. A simple pyhonic O(n)
solution is to divide into two arrays and subtract the min of the left subarray from the max of the right subarray. 
Slicing in python arr[a:b] takes time complexity O(b-a). Hence all slicing here is O(n/2 - 0) = O(n), computing max/min
occurs in O(n) time as well, However this solution uses O(n) auxillary space. To further optimise this solution, we can
keep track of only minimum value in array and check if diff is larger than current diff. This would take O(1) space.
"""

def maxdiff1(arr):
    if len(arr) % 2 != 0:
        arr1 = arr[:(len(arr)//2)+1]
        arr2 = arr[(len(arr)//2):]
    else:
        arr1 = arr[:(len(arr)//2)]
        arr2 = arr[(len(arr)//2):]
    return max(arr2) - min(arr1)

def maxdiff2(arr):
    diff = arr[1] - arr[0] # initial difference
    minval = arr[0] # initial min val
    for i in range(2, len(arr)):
        # saving current difference in diff if its better
        diff = max(diff, arr[i]- minval)
        # updating minval if its smaller
        minval = min(minval, arr[i])
    return diff


"""
7. Maximum Consecutive 1s in a Binary Array:

We will make a naive O(n*n) solution first, which first checks if current element is 1, then goes into a loop,
for checking if there are consecutive 1s. Alternatively we can easily reset the count each time the loop encounters
a 0 and thus incrementing the count on each 1 would give the length of streaks. the max one is saved in O(n) time and
Theta(1) auxillary space.
"""
def max1(arr):
    res = 0
    # loop to traverse through elements
    for i in range(0, len(arr)):
        count = 0
        # if current element is 1
        if arr[i] == 1:
            # checking consecutive 1s and breaking if not
            for j in range(i, len(arr)):
                if arr[j] == 1:
                    count += 1
                else:
                    break
        # computing max number of consecutive 1s
        res = max(res, count)
    return res

def max1opt(arr):
    count = 0; res = 0
    for i in range(0,len(arr)):
        if arr[i] == 0:
            # reset the count when 0 is encountered
            count = 0
        else:
            count += 1
            res = max(res, count)
    return res
    

"""
8. Frequencies in a Sorted Array:

Simply adding a dummy element to make sure last element is considered, and checking consecutive pairs to count
frequencies. Count is set to 0 when new element is encountered. Since array is sorted, this gives the count
of the groups of elements and thus the frequencies in O(n) time complexity and O(1) auxillary space.
"""

def freqsorted(arr):
    count = 0
    arr.append(-1)  # dummy element
    for i in range(1, len(arr)):
        if arr[i-1] == arr[i]:
            count += 1
        else:
            print(arr[i-1], count+1)
            count = 0

"""
9. Two Sum and Three Sum Problems:

Given a sorted array and a sum k find a pair/triplet of numbers with the sum k. The O(n) approach is to use 2 pointers
l = 0 and r = N-1
(i) When the sum arr[r] + arr[l] < k, we need to increase the sum by incrementing l
(ii)When the sum arr[r] + arr[l] > k, we need to decrease the sum by decrementing r
For triplets problem we use the pairs function for every ith element. This takes O(n^2) time
"""

def pairSum(arr, k, start, end):
    l  = start; r = end
    while l < r :
        s = arr[r] + arr[l]
        if s == k:
            return True
        elif s < k:
            l += 1
        else:
            r -= 1
    return False

def tripletSum(arr, k):
    for i in range(len(arr)):
        if pairSum(arr, k - arr[i], i + 1, len(arr) - 1):
            return True
    return False

"""
10. Stocks Buy and Sell Problem:

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
