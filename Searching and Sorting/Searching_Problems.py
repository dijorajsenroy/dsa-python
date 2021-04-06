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

Given a number compute floor() of it's square root without using any library functions. A naive O(n) solution is to travserse an array
of i = 1 to n and check for i*i == n. This can be optimised to reduce numbers searched, for example, doing i = 1 to n//2 etc. To do it in
Theta(log X) we use binary search to traverse the array in the same way. The conditions for finding the square root for a mid:
(i) if arr[mid]**2 == n then return arr[mid]
(ii) if arr[mid]**2 < n then square root exists in right half, update low to mid + 1
(iii) if arr[mid]**2 > n then square root exists in left half, update high to mid - 1
"""
def sqrootBS(x):
    low = 0; high = x - 1
    while low <= high:
        mid = (low + high) // 2
        sq = mid*mid
        # check for square root at mid
        if sq == x:
            return mid
        # update low and high otherwise
        elif sq > x:
            # sq root in left half
            high = mid - 1
        else:
            # sq root in right half
            low = mid + 1
            ans = mid
    return ans

"""
4. Find peak element:

The Naive solution would be to slide a triplet window over the array in O(n) time, checking for peak. This problem can be solved in
O(log N) time by using binary search. Here, we check if a mid is the peak element, meaning the following condition has to hold true:
arr[mid] > arr[mid - 1] and arr[mid] > arr[mid + 1] for mid in range (1, N - 2). Here, the side where the element is greater than mid,
has the peak and we will shift the subarray in the direction of the greater element accordingly. 
"""
def peakElement(arr):
    low = 0; high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        # check if mid is a peak
        c1 = mid == 0 or arr[mid - 1] <= arr[mid]
        c2 = mid == len(arr) - 1 or arr[mid + 1] <= arr[mid]
        if c1 and c2:
            return mid
        elif arr[mid - 1] >= arr[mid]:
            # peak exists in 0 to mid - 1
            high = mid - 1
        else:
            # peak exists in mid + 1 to len(arr) - 1
            low = mid + 1
    return - 1 

"""
5. Missing and Repeating Numbers :

The most obvious solution would be to search for each element in O(nlog N) time using a loop to traverse the array along with binary search,
But using hashtable/count array this can be done in constant time.
"""
def miss_rep_optimal(n, arr):
    countarr = [0] * n
    for i in range(len(arr)):
        countarr[arr[i]] += 1
    for i in countarr:
        if i == 0:
            yield "Missing: {i}" 
        if i > 1:
            yield "Repeating: {i}"

"""
6. Allocate minimum pages:
"""
