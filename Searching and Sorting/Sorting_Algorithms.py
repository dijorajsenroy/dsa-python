"""
1. Selection Sort:

The idea is simple for every ith element in (0, N) we are finding the smallest element in range (i+1, N) and swap it with the
ith element. Thus the smallest elements start occupying lower indices. The time complexity of this algorithm is Theta(n^2) and it
is in-place, meaning it doesn't require any extra space. It has lesser memory writes than most algorithms (except Cycle Sort).

The algorithm is mentioned here:
(i) For i passes compute the smallest element in i+1 to Nth subarray. Store it in a variable for minimum element's index,
If there is no element found then let the variable store the value of i
(ii) Swap the ith element with either itself or the value of j that was stored in the minimum index. 
"""

def selectionSort(arr):
	for i in range(len(arr)):
		min_idx = i
		# finding smalles element in (i+1,n)
		for j in range(i + 1, len(arr)):
			if arr[j] < arr[min_idx]:
				min_idx = j
			# swapping smallest with ith element
			arr[i], arr[min_idx] = (arr[min_idx], arr[i])
	return arr
			
"""
2. Bubble Sort:

Bubble sort is an O(n^2) stable sorting algorithm. The word stable here means that the order of two elements with same sorting key value 
is preserved. The algorithm is inplace meaning that there is no extra space allocated. The idea is to compare two adjacent j and j+1th 
elements and swap them if j > j+1. Thus essentially in every iteration we are pushing the largest element to its final position in the
end of the array. For N elements there has to be N-1 passes to push N-1 largest elements. We can optimise this algorithm in two ways.
We know that for every ith iteration we have already computed i passes, which means the i largest elements have been pushed to the end
of the array. Hence we run jth loop only for unswapped elements in j = 0 to N-i-1 elements. We can add a flag variable to stop when the
array is already swapped. 

The steps in this Algorithm are:
(i) Run i = N-1 passes to push N-1 largest elements to the end of the array. For every ith pass compute N-i-1 iterations because the
last i elements are already sorted. We take N-1 instead of N to prevent overflow in indexing the array.
(ii) Compare adjacent elements j and j+1 and swap them is j>j+1, thus pushing the larger element to the end.
(iii) At the start of each iteration we initialise a flag variable as false. When a swap occurs we change this value to true. After swap,
if the flag is still false, it means that there was no swap that had occurred meaning that the array is sorted. Thus we can reduce the 
number of useless swaps after the array is already sorted to optimise this solution.
"""

def bubbleSort(arr):
	for i in range(len(arr)-1):
		swapped = False
		for j in range(len(arr)-i-1):
			if arr[j] > arr[j+1]:
				arr[j], arr[j+1] = (arr[j+1], arr[j])
				swapped = True
		if swapped == False:
			break
	return arr

"""
3. Insertion Sort:

Like Bubble Sort and Selection Sort, Insertion Sort is also an O(n^2) worst case time complexity, comparison based algorithm. It is stable,
and in-place in nature, meaning that the order is preserved and takes O(1) auxillary space. For small sized arrays Insertion Sort is the
best algorithm, python standard function sorted() uses TimSort(merge sort variant) which for small array sizes switches to insertion sort.
It takes O(n) time when the array is already sorted, which is its best-case time complexity. The idea is to maintain a sorted subarray in
the array whose length is incremented everytime an element is inserted into it into it's correct position in the subarray. For every i,
0 to i elements are sorted and i+1th element is inserted into it's appropriate position in the 0 to i subarray. The steps are as follows:

(i) for i=0 or 1st element subarray is already sorted. We pick the next element, and start from i = 1.
(ii) for an ith element we compare it with all the elements in the 0 to i-1 sorted elements, and determine its appropriate place to 
be inserted, ie, where i > jth element or i < j+1th element in 0 to i-1.
(iii) Shift all the elements in the sorted subarray after the insertion index of the ith element. To compute this we swap all elements while
two the j-1th element is more than the jth element. This ensures the j=ith value is inserted in the rightful place and all values are shifted.

"""

def insertionSort(arr):
	for i in range(1, len(arr)):
		# element to be inserted in arr[0]...arr[i-1] subarray
		key = arr[i]
		j = i - 1
		while j >= 0 and key < arr[j]:
			# swap arr[j+1](initially key) and arr[j]
			# till we find a value greater than key and stop 
			arr[j+1], arr[j] = arr[j], arr[j+1]
			j -= 1
	return arr

"""
3. Merge Sort:
"""
def merge_sort(nums):

	if len(nums) == 1:
		return

	middle_index = len(nums) // 2

	left_half = nums[:middle_index]
	right_half = nums[middle_index:]

	merge_sort(left_half)
	merge_sort(right_half)

	i = 0
	j = 0
	k = 0

	while i < len(left_half) and j < len(right_half):
		if left_half[i] < right_half[j]:
			nums[k] = left_half[i]
			i = i + 1
		else:
			nums[k] = right_half[j]
			j = j + 1

		k = k + 1

	while i < len(left_half):
		nums[k] = left_half[i]
		k = k + 1
		i = i + 1
    
"""
4. Quick Sort:
"""
def quick_sort(nums, low, high):

	if low >= high:
		return

	pivot_index = partition(nums, low, high)
	quick_sort(nums, low, pivot_index-1)
	quick_sort(nums, pivot_index+1, high)


def partition(nums, low, high):

	#pivot_index = (low+high)//2
	#swap(nums, pivot_index, high)

	i = low

	for j in range(low, high, 1):
		if nums[j] <= nums[high]:
			#swap(nums, i, j)
			i = i + 1

	#swap(nums, i, high)

	return i

"""
5. Counting Sort:
"""
"""
6. Radix Sort:
"""
"""
7. Heap Sort:
"""
"""
8. Cycle Sort:
"""


