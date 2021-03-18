"""
1. Cycle Sort:

Cycle Sort is a worst-case O(n^2) algorithm with the property that it executes the minimum number of memory writes to sort an array. It is in-place 
but not stable in nature. The idea here is to traverse the array and for each element compute the number of elements smaller than that element.
In the sorted array this would be the position of that element and as we swap it exactly once to its rightful place. The initial value at that
memory location becomes our new item to swap. With each swap we can say that elements 0 to i (swapped index) is sorted and we need check only
the remaining sub-array, which means we can start counting position (or count) from i itself. We start from count = i but if count remains i, it
means that the element at i is at its rightful place in which case we exit from the loop when i == count. This algorithm needs to be modified slightly,
to deal with duplicate elements. To make sure we subsititute an item at the right position, each time a count is obtained, before swapping we check if the
position should be swapped, if it should, we take the last occurrence of the number to be swapped with the item. To obtain the number of memory writes, increment
a variable each time you execute a swap. 
"""

def cycleSortDistinct(arr):
    n = len(arr)
    for i in range(n):
        item = arr[i]
        count = 0
        # count elements smaller than item
        for j in range(i + 1, n):
            if arr[j] < item:
                count += 1
        # swap item at its rightful position
        arr[count], item = item, arr[count]
        # loop to determine the position of new item, unless position is correct. 
        while(count != i):
            # starting count from i as 0 to i-1 is sorted.
            count = i
            # obtaining position in unsorted subarray
            # if count is unchanged then we have correct position.
            for j in range(i + 1, n):
                if arr[j] < item:
                    count += 1
            
def cycleSortDuplicates(arr):
    n = len(arr)
    for i in range(n):
        item = arr[i]
        count = 0
        # count elements smaller than item (obtain position)
        for j in range(i + 1, n):
            if arr[j] < item:
                count += 1
        # If the item is already there, this is not a cycle.
        if count == i:
            continue
        else:
            # Otherwise, put the item there or right after any duplicates.
            while item == arr[count]:
                count += 1
            arr[count], item = item, arr[count]
        # loop to determine the position of new item, unless position is correct.
        while(count != i):
            # starting count from i as 0 to i-1 is sorted.
            count = i
            # obtaining position in unsorted subarray
            # if count is unchanged then we have correct position.
            for j in range(i + 1, n):
                if arr[j] < item:
                    count += 1
            # put the item after any duplicates is applicable.
            while arr[count] == item:
                count += 1
            arr[count], item = item, arr[count]
            
"""
2. Heap Sort:
"""

"""
3. Counting Sort:

Counting sort algorithm is a O(n+k) time complexity algorithm where all the numbers lie in the range 0 to k. In the naive implementation,
We simply make a count array for numbers in 0 to k and increment their counts in the array. Since the index is in sorted order, we have 
the numbers (indices) sorted according to frequencies. Then we compute the prefix sum array of this count array, where every ith index
is the sum of frequencies of 0 to i indices. Thus count(i) stores number of elements <= i. From this we construct the sorted array, 
traversing a loop i from N-1 to 0, to make sure the sort is stable. we get the array value arr[i]'s count x = count[arr[i]]. From this 
we know that there are x elements smaller than or equal to arr[i], thus we insert arr[i] at x - 1th position, and decrement it's count.
Similaraly this is repeated for all elements in (N-1,0) and they are all inserted in sorted in a stable order.
"""

def countSort(arr, k):
    # make count array
    count_arr = [0] * k
    for i in arr:
        count_arr[i] += 1
    # compute prefix sum array
    for i in range(1,k):
        count_arr[i] += count_arr[i-1]
    # create sorted array
    res = [0] * len(arr)
    for i in reversed(range(len(arr))):
        res[count_arr[arr[i]] - 1] = arr[i]
        count_arr[arr[i]] -= 1
    # returning result
    arr = res
    del count_arr, res
    return arr

"""
4. Radix Sort:
"""
"""
5. Bucket Sort:
"""

