"""
1. Cycle Sort:
"""
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

