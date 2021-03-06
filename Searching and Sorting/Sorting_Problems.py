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

A pair of elements in an array such that the greater element occurs before the smaller element is called an inversion.
onditions: arr[i] > arr[j] for i < j. For a sorted array there are 0 inversions, for a reverse sorted array there are 
n*(n-1)/2 inversions. The simple algorithm to do this is to check all pairs and count in O(n*n) time. Using Merge Sort,
We can do this in O(nlogn) time complexity. While we are recursively sorting the two halves, we are also counting the
inversions. The steps in this algorithm are described below:
For every inversion (x, y) where x > y, the possibilities are -
case 1: both x and y lie in left half (handled by recursively counting in left half)
case 2: both x and y lie in right half (handled by recursively counting in right half)
case 3: x lies in left half and y lies in right half (case 1 and case 2 eventually reach case 3 with recursive calls. 
The merge function has to be modified to handle case 3, and that will recursively handle cases 1 and 2). The merge fucntion:
Merge the left and right half like the normal merge function, but for the condition right[j] > left[i],
the elements satisfy the condition of being inversions so we count them as such. to count inversions we increment it by mid - i,
where i is the position of the inverted element. 
"""
def countInversionNaive(arr):
    count = 0 
    for i in range(len(arr) - 1):
        for j in range(i + 1, len(arr)):
            if arr[i] > arr[j]:
                count += 1
                print(arr[i], arr[j])
    return count

# Function to Use Inversion Count
def countInversions(arr):
    temp_arr = [0]* len(arr)
    return _mergeSort(arr, temp_arr, 0, len(arr) - 1)

# Function to use MergeSort to Count Inversions
def _mergeSort(arr, temp_arr, left, right):
    inv_count = 0
    if left < right:
        mid = (left + right)//2
        # inversion counts in the left subarray
        inv_count += _mergeSort(arr, temp_arr, left, mid)
        # inversion counts in right subarray
        inv_count += _mergeSort(arr, temp_arr, mid + 1, right)
        # merge two sorted subarrays
        inv_count += merge(arr, temp_arr, left, mid, right)
    return inv_count

# Function to merge 2 sorted subarrays
def merge(arr, temp_arr, left, mid, right):
    i = left     # Starting index of left subarray
    j = mid + 1  # Starting index of right subarray
    k = left     # Starting index of to be sorted subarray
    inv_count = 0
    while i <= mid and j <= right:
        # There will be no inversion if arr[i] <= arr[j]
        if arr[i] <= arr[j]:
            temp_arr[k] = arr[i]; i += 1
        else:
            # Inversion will occur
            temp_arr[k] = arr[j]; j += 1
            inv_count += (mid - i + 1)
        k += 1
    # Copy the remaining elements into temp array
    while i <= mid:
        temp_arr[k] = arr[i]; k += 1; i += 1
    while j <= right:
        temp_arr[k] = arr[j]; k += 1; j += 1
    # Copy the sorted subarray into original array
    for i in range(left, right + 1):
        arr[i] = temp_arr[i]

    return inv_count


"""
4. Kth Smallest Element:

We are given a number k and an unsorted array. The task is to find out the kth smallest element in the array. The naive method
to do this is to sort the array in O(nlogn) time and index the k - 1th element. Using Quick Sort (Lomuto) as a subroutine is
a better method with an average case time complexity of O(n), and worst case O(n*n). The task of the lomuto partition func is 
to put the last element of the array to its correct position in the sorted array, meaning all elements before it are smaller
and after it are larger. The Quick Sort function calls this partition function recursively on the left and right half to put
each element in its correct place in the array. Since lomuto partitition puts an element after all the elements smaller than it
and returns index, and the index returned by it is k, then it is the kth smallest element. 
p, arr = lomutoPartition(arr)
arr = [0...i|p|j....n] where 0 to i < p < j to n
case 1: if k - 1 > p: look for k - 1 in right subarray (or greater elements)
case 2: if k - 1 < p: look for k - 1 in left subarray (or smaller elements)
case 3: if k - 1 == p: kth smallest element is found.
"""

def kthsmallest(arr, k):
    low = 0; high = len(arr) - 1
    while low <= high:
        p = lomutoPartition(arr, low, high)
        if k - 1 == p:
            return p
        elif k - 1 < p:
            high = p - 1
        else:
            low = p + 1
            
# function to compute lomuto partitioned array
def lomutoPartition(arr, low, high):
    """
    The goal of lomuto partition is to put a pivot (last element) to its rightful position in the array. For this purpose
    We will maintain two subarrays 0 to i for elements <= pivot, and i+1 to j for elements >= pivot. To do this we start from
    j = 0 and i = -1 and whenever we encounter an element smaller than pivot in (j+1,n) we add it to the (0,i) subarray by 
    swapping arr[j] with arr[i + 1] and increment i ++ to increase window size. Lastly, we swap pivot at i + 1 and return. 
    """
    pivot = arr[high] # pivot is always last element
    i = low - 1
    for j in range(low, high):
        if arr[j] < pivot:
            # swap and increase smaller than pivot window
            arr[i + 1], arr[j] = arr[j], arr[i + 1]
            i += 1
    # swap with pivot, new index of pivot is i + 1
    arr[i + 1], pivot = pivot, arr[i + 1]
    return i + 1


"""
5. Chocolate Distribution Problem:

In an array, index i represents a packet of chocs and arr[i] represents the number of chocs in it. There are m children, we 
want to distribute the choloclates between m children such that every child gets exactly one packet, and the difference
between the minimum chocs and maximum chocs received by a child should be minimum. for example in an array [x1,x2..xN]
we have to pick m elements m_arr = [m1,m2...mM] such that max(m_arr) - min(m_arr) is minimum. The steps in solving this:
(i) Sort the array in O(nlogn) time complexity
(ii) Assume the first of m numbers chosen to be the minimum, as we are going in sorted order the mth number should be max.
So for each arr[i] we need to find arr[i + m - 1] - arr[i] and take the minimum of these values to obtain out answer. 
"""

def chocDist(arr, m):
    arr.sort()
    min_val = arr[m - 1] - arr[0]
    for i in range(1, len(arr)):
        min_val = min(min_val, arr[i + m - 1] - arr[i])
    return min_val

"""
6. A. Sort an Array with Two Types of elements:

Can also be asked as Segregate negative and positive elements, Segregate even and odd elements, Sort a binary array. The 
solution has to be a stable sorting algorithm. This problem can be solved using Lomuto in Theta(n) time and O(1) space.
"""

def sort2types(arr):
    p = max(arr)
    i = -1
    for j in range(len(arr)):
        if arr[j] < p:
            arr[i + 1], arr[j] = arr[j], arr[i + 1]
            i += 1
    return arr

"""
6. B. Sort an Array with Three Types of elements:

Can also be asked as Sort an array of 0s, 1s, 2s, Three-way partitioning when multiple occurrences of a pivot may exist,
Partitioning around a range, etc. To solve this problem we will use a standard Hoare's partition variation called the
Dutch National Flag Algorithm. All the pivot elements should come together or form a range of pivots, we have to maintain
4 sections in the array, 0 to low consisting of elements smaller than lower range of pivot and l1 to mid should be all pivots
high to N - 1 should be all greater than higher range of pivot. The 4 parts are: a[1...low], a[low...mid - 1], a[mid... high]
a[high + 1...N]. If the ith element is 0, we swap it with low and decrement low. if it is 1, we keep it as it is but decrement 
the (mid, high) range. If it is 2 then we swap it with an element in the high range. 
Algorithm: 
(i) Keep three indices low = 1, mid = 1 and high = N and there are four ranges, 1 to low (the range containing 0), 
low to mid (the range containing 1), mid to high (the range containing unknown elements) and high to N (the range containing 2).
(ii) Traverse the array from start to end and mid is less than high. (Loop counter is i)
(iii) If the element is 0 then swap the element with the element at index low and update low = low + 1 and mid = mid + 1
(iv) If the element is 1 then update mid = mid + 1
(v) If the element is 2 then swap the element with the element at index high and update high = high – 1.
"""

def sort3types(arr):
    low = 0; high = len(arr) - 1; mid = 0
    while mid <= high:
        if arr[mid] == 0:
            arr[low], arr[mid] = arr[mid], arr[low]
            low = low + 1
            mid = mid + 1
        elif arr[mid] == 1:
            mid = mid + 1
        else:
            arr[mid], arr[high] = arr[high], arr[mid]
            high = high - 1
    return arr
