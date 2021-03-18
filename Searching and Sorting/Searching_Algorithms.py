"""
1. Binary Search:

The array is required to sorted. We find the index of a key taken as argument and if not found -1 is returned. The algorithm takes
O(log2(N)) time compexity. The steps involved are:
(i) Divide the array into two halves at mid. 
(ii) If key is smaller than arr[mid] then the element is contained in first half. Check in the first half by use of pointer.
(iii) If key is larger than arr[mid] then the element is contained in second half. Check in the second half by use of pointer.

This can be done iteratively and recursively in the same time complexity however the recursive implementation takes extra auxillary
space for the recursion call stack, which is called [log N] times where [] represents the ceil function. 
"""


def binarySearchIterative(arr, k):
    l = 0; r = len(arr) - 1
    while l<=r:
        mid = (l + r) // 2
        # checking if k is at mid
        if arr[mid] == k:
            return mid
        # checking in only first subarray
        if k < arr[mid]:
            r = mid - 1
        # checking in second subarray
        if k > arr[mid]:
            l = mid + 1
    return -1

def binarySearchRecursive(arr, l, r, k):
    if l <= r:
        mid = (l + r) // 2
        # checking if k is at mid
        if arr[mid] == k:
            return mid
        # checking in only first subarray
        if k < arr[mid]:
            return binarySearchRecursive(arr, l, mid - 1, k)
        if k > arr[mid]:
            return binarySearchRecursive(arr, mid + 1, r, k)
    return -1

"""
2. Ternary Search:

It is similar to binary search in logic but here we make 3 parts of the array instead of 2. This algorithm takes
O(log3(N)) time complexity. The steps involved are:
(i) Divide the array into 3 parts, using two divisions at mid1 and mid2. The formulae for mid1 and mid2 are:
    mid1 = l + (r - l) // 3
    mid2 = r - (r - l) // 3
(ii) Check if k is present at mid1 or mid2 and return accordingly
(iii) If not, check that k is smaller than mid1 and thus search in the subarray of 0 to mid1
(iv) If not, check if k is larger then mid2 and thus search in the subarray of mid2 to N
(v) if neither then check for k in the subarray of mid1 to mid2
"""

def ternarySearchIterative(arr, k):
    l = 0; r = len(arr) - 1
    while l <= r:
        mid1 = l + (r - l) // 3
        mid2 = r - (r - l) // 3
        if arr[mid1] == k:
            return mid1
        elif arr[mid2] == k:
            return mid2
        elif k < arr[mid1]:
            r = mid1 - 1
        elif k > arr[mid2]:
            l = mid2 + 1
        else:
            l = mid1 + 1
            r = mid2 - 1
    return -1


def ternarySearchRecursive(arr, l, r, k):
    if l <= r:
        mid1 = l + (r - l) // 3
        mid2 = r - (r - l) // 3
        if arr[mid1] == k:
            return mid1
        elif arr[mid2] == k:
            return mid2
        elif k < arr[mid1]:
            return ternarySearchRecursive(arr, l, mid1 - 1, k)
        elif k > arr[mid2]:
            return ternarySearchRecursive(arr, mid2 + 1, r, k)
        else:
            return ternarySearchRecursive(arr, mid1 + 1, mid2 - 1, k)
    return -1




