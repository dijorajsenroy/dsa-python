"""
1. A. Index of first occurrence in a sorted array:

For a given element we have to find the first occurrence of it in a sorted array. The naive solution is O(n) And takes one iteration thru
the array. A binary search based implementation can be used to optimise this problem. In binary search if the element at mid is not the 
first occurence then the previous element would be the same as arr[mid]. If this is true then we recursively call function on that subarray
such that the next position of mid is mid - 1, till the first occurrence is reached. We handle the corner case for mid = 0 by returning mid,
else we shift the mid to the first half of the subarray where k is found by passing low = low and high = mid - 1. 
"""

def binarySearchFirstOcc(arr, low, high, k):
    if low <= high:

        mid = (low + high) // 2

        # found at mid (check for first occurrence)
        if arr[mid] == k:
            if mid == 0 or arr[mid - 1] != arr[mid]:
                # no previous occurrence
                return mid
            else:
                # shift subarray to the left
                return binarySearchFirstOcc(arr, low, mid - 1, k)

        # recursive call 2nd half
        if arr[mid] < k:
            return binarySearchFirstOcc(arr, mid + 1, high, k)

        # recursive call 1st half
        if arr[mid] > k:
            return binarySearchFirstOcc(arr, low, mid - 1, k)
    else:
        return -1 

"""
1. B. Index of last occurence in a sorted array:

Similar to first occurrence we check for the last occurrence when k is found at mid. In this case we handle corner case if mid is len(arr),
and we check id arr[mid] is the same as arr[mid + 1], in which case mid is not the last occurrence of k. To shift mid, to mid + 1 we have
to pass low = mid + 1 and high = high hence shifting the subarray where mid of was found.   
"""

def binarySearchLastOcc(arr, low, high, k):
    if low <= high:
        mid = (low + high) // 2

        # found at mid (check for last occurrence)
        if arr[mid] == k:
            if mid == len(arr) - 1 or arr[mid + 1] != arr[mid]:
                # no next occurrence
                return mid
            else:
                # shift subarray to right
                return binarySearchLastOcc(arr, mid + 1, high, k)

        # k is in second half
        if arr[mid] < k:
            return binarySearchLastOcc(arr, mid + 1, high, k)

        # k is in first half
        if arr[mid] > k:
            binarySearchLastOcc(arr, low, mid - 1, k)
    else:
        return -1

"""
1.C. Count occurrences in a sorted array:

The naive approach is to do this in O(n) time by travering the entire loop and count the occurrences of a given element k. However
We can implement binary search to solve this problem in O(log N). Since the array is sorted all the same element would exist sequentially.
Using this fact we can compute the first and lasy occurrences using binary search. The number of occurrences is lastOcc - firstOcc + 1
"""
def countOcc(arr, k):
    firstOcc = binarySearchFirstOcc(arr, 0, len(arr) - 1, k)
    lastOcc = binarySearchLastOcc(arr, 0, len(arr) - 1, k)
    if firstOcc != -1 and lastOcc != -1:
        return lastOcc - firstOcc + 1
    else:
        return -1

"""
2. A. Search in an Infinite Sized Array:
"""

"""
2. B. Search in a Sorted Rotated Array:
"""
"""
3. Square Root Problem:
"""
"""
4. Find peak elements:
"""
"""
5. Repeating Elements:
"""
"""
6. Allocate minimum pages:
"""
"""
7. Two pointer approach:
"""
