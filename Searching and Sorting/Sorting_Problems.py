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
2. A. Intersection of two sorted arrays:

Given two sorted arrays print the intersection of the two, if there are common elements then we need to print it only once.
Intersection refers to the set of common elements of the two arrays. The Naive O(m*n) is two check individual elements, if
they are not duplicates (arr[i - 1] != arr[i]) then it is checked with the other array and printed if common. Another method
To do this in linear time but O(n) space is to use Hash set intersection, which would work for unsorted arrays as well. The
Efficient method for this program is to, run two pointers in either arrays and check for each index in a1 and a2. 4 Cases:

(i) i > 0 and a1[i - 1] == a1[i] : Increment i till a1[i] is the last occurrence od a duplicate value in a1. 
To handle the duplicate elements we start with a condition to handle them before we check for equality. We increment i till
a[i - 1] != a[i], which means it is the last occurrence of the element and then check for it in a2. We don't need to have a
condition for duplicates in a2, as when we find a match we increment both i and j, so i now points to a different element
greater than a2[j] and j would increment till a match is found again.

(ii) a1[i] < a2[j] : We increment j to obtain a value greater than a2[j] in next iteration

(iii) a1[i] > a2[j] : We increment i to obtain a value greater than a1[i] in next iteration

(iv) a1[i] == a2[j] : Print the common element

The algorithm takes Theta(len(a1) + len(a2)) time and no auxillary space. 
"""
def intersectionNaive(a1, a2):
    for i in range(len(a1)):
        if i > 0 and a1[i - 1] == a1[i]:
            # repeating element
            continue
        else:
            # check if a1[i] is common
            if a1[i] in a2:
                print(a1[i])
                
# Using Hash Sets ( Works for unsorted arrays as well)
def intersectionSet(a1, a2):
    a1 = set(a1)
    a2 = set(a2)
    # time complexity - O(min(len(a1), len(a2)))
    a1 = a1.intersection(a2)
    # constant lookup for hash set
    for i in a1:
        print(i)

# Efficient solution  - Theta (m + n)
def intersection(a1, a2):
    i = 0; j = 0
    m = len(a1); n = len(a2)
    while i < m and j < n:
        if i > 0 and a1[i - 1] == a1[i]:
            # dulplicates are not checked for
            i += 1
            continue
        if a1[i] == a2[j]:
            # common element found
            print(a1[i])
            i += 1
            j += 1
        elif a1[i] < a2[j]:
            i += 1
        else:
            j += 1

"""
2. B. Union of two sorted arrays:

Given two sorted arrays print the all the elements in both arrays, but the duplicate elements should be printed only once.
If the arrays are unsorted we can use the Hash set data structure to solve this in linear time. For the efficient solution,
There are the following cases for every a1[i] and a2[j] 0 <= i < m, 0 <= j < n:
(i) In case of repeating element(x > 0 and a[x - 1] == a[x]) in a1 and a2, we skip them to its last occurrence.
(ii) if a1[j] < a2[j] we print a1[i] and increment i
(iii) if a1[j] > a2[j] we print a2[j] and increment j
(iv) in case a1[i] == a2[j] we print either and increment both i and j.
This loop ensures that all the smaller non-duplicate elements in either arrays have been printed. To print the remaining
larger elements we use individual while loops and the same loop variables(that stores the last printed index), while 
checking for duplicate elements we print the remaining elements. This takes O(m + n) time and O(1) space
"""
def union(a1, a2):
    i = 0; j = 0
    m = len(a1); n = len(a2)
    while i < m and j < n:
        # check for last occurrence of a1[i]
        if i > 0 and a1[i - 1] == a1[i]:
            i += 1; continue
        # check for last occurrence of a2[j]
        if j > 0 and a2[j - 1] == a2[j]:
            j += 1; continue
        # print and increment the smaller value
        if a1[i] < a2[j]:
            print(a1[i]); i += 1
        elif a2[j] < a1[i]:
            print(a2[j]); j += 1
        else:
            print(a1[i])
            i += 1; j += 1
    # print the remaining elements and check for duplicates
    while i < m:
        if i > 0 and a1[i - 1] != a1[i]:
            print(a1[i])
        i += 1
    while j < n:
        if j > 0 and a2[j - 1] != a2[j]:
            print(a2[j])
        j += 1

# time complexity - O(m + n), works for unsorted arrays as well.
def unionSet(a1, a2):
    a1 = set(a1)
    a2 = set(a2)
    a1 = a1.union(a2)
    for i in a1:
        print(i)
        
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
"""
"""
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
