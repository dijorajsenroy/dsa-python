"""
1. Merge two sorted arrays:

We have to write a program to take two sorted arrays and merge them in a way that the resultant array is sorted as well. A naive pythonic
solution is to extend the list and then sort the list. Extending arr1[l1] and arr2[l2] has time complexity O(l2) and sorting the list has
time complexity O((l1+l2)*log(l1+l2)). Without using lists we cant use the dynamic extend function and would have to create a Theta(n) arr
The efficient solution works in linear time complexity and works in Theta(l1+l2) time with constant auxillary space. the idea is to 
traverse the two arrays together using two different index variables and compare the two values simultaneously. The smaller value is printed,
and it's index is incremented, when that happens. This is the implementation of merging two arrays in Merge sort. The steps are:

(i) For every a[i] and b[j] till i < m and j < n, we check the smaller element and print it. The array whose element is smaller is indexed,
To check the next smallest element. In this we print elements till any one index reaches array length.
(ii) In case of equality of a[i] and b[j], we print a[i] to maintain stability of the sorting algorithm.
(iii) After the condition terminates the remaining numbers in the array have to be larger than arr1, so we print them in the same order. 
"""
def mergeNaiveLists(arr1, arr2):
    arr1.extend(arr2)
    return sorted(arr1)

def mergeNaiveArr(arr1, arr2):
    res = [0]*(len(arr1)+len(arr2))
    res_idx = 0
    # copying the array
    for i in range(len(arr1)):
        res[res_idx] = arr1[i]
        res_idx += 1
    for i in range(len(arr2)):
        res[res_idx] = arr2[i]
        res_idx += 1
    # sorting in O(nlogn) time
    return sorted(res)

def merge2arr(a, b):
    i = 0; j = 0
    # runs exactly len(a) + len(b) times
    while i < len(a) and j < len(b):
        # print the smaller element and incrementing idx
        if a[i] <= b[j]:
            print(a[i])
            i += 1
        else:
            print(b[j])
            j += 1
    # printing the remaining numbers in first array:
    while i < len(a):
        print(a[i]); i += 1
    # printing the remaining numbers in second array:
    while j < len(b):
        print(b[j]); j += 1
    
"""
2. Union And Intersection of two sorted arrays:
"""
"""
3. Count inversions in Array:
"""
"""
4. Kth Smallest Element:
"""
"""
5. Chocolate Distribution Problem:
"""
"""
6. A. Sort an Array with Two Types of elements:
6. B. Sort an Array with Three Types of elements:
"""
"""
7. Minimum difference in Array:
"""
"""
8. Merge Overlapping intervals:
"""
"""
9. Meeting the maximum guests:
"""
"""
10. Merge K sorted Arrays (Hard): 
"""
