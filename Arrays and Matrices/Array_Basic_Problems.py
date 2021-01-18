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
1. Merging two sorted arrays:

Two sorted arrays of sizes m, n have to be merged into an array of size m+n. We need to ensure that the
resulting array is sorted as well. For this purpose we traverse the two arrays and compare the ith index
simultaneously and choose the the smaller option. When we reach the end of one of the arrays we copy the
remaining elements to the final array. The time complexity of this solution is O(m+n).
"""
def merge(arr1, arr2):
    m = len(arr1); n = len(arr2)
    # creating an array of m+n dims
    arr3 = a.array('i', [0] * (m+n))
    i = 0; j = 0; k = 0
    # while the two loop variables are smaller than lengths
    while(i < m and j < n):
        # checking smaller element
        if arr1[i] < arr2[j]:
            # copying and incrementing arr3 and arr1 elements
            arr3[k] = arr1[i]
            k += 1; i += 1
        else:
            # copying and incrementing arr3 and arr2 elements
            arr3[k] = arr2[j]
            k += 1; j += 1
    # copying the remaining elements:
    # of 1st array:
    while i < m:
        arr3[k] = arr1[i]
        k += 1; i += 1
    # of second array
    while j < m:
        arr3[k] = arr2[j]
        k += 1; j += 1
    return arr3

"""
2. Array Rotations (by 1 or D places): 

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
3. Remove Duplicates from sorted array:

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
4. Largest and second largest elements:
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
5. Move Zeroes to the right end of the array:

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
6. Leaders in an Array Problem:

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
7. Maximum Difference Problem:
"""

