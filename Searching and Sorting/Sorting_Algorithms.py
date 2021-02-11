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
	# Traverse through 1 to len(arr) 
	for i in range(1, len(arr)): 
		key = arr[i] 
  		# Move elements of arr[0..i-1], that are 
        	# greater than key, to one position ahead 
        	# of their current position 
        	j = i-1
        	while j >=0 and key < arr[j] : 
                	arr[j+1] = arr[j] 
                	j -= 1
        	arr[j+1] = key
	
	return arr

"""
3. Merge Sort:

It is a divide and conquer algorithm, ie, it divides the array into two parts and recursively sorts these two parts and merges
the sorted parts. It is a stable sorting algorithm that works in Theta(nlogn) time complexity and Theta(n) auxillary space. 
For linked list sorting it works in O(1) aux space, and has a variant called Block Merge sort that does not need extra space, 
and is an in-place algorithm. For arrays in general (not list), Quick Sort outperforms Merge sort.

The algorithm is explained in steps below:
(i) There are many ways of dividing the array into two parts but for this implementation we divide it by midpoint of the array.
The parts are stored in two different arrays hence utilising Theta(n) auxillary space. Then we input these two arrays in a recursive
call. 
(ii) The base case of these calls is when there is one element left in the array, ie, len(arr) == 1. At this point both the subarrays 
are sorted. Then we combine the two sorted subarrays using the efficient method of merging two subarrays, ie, to traverse the two subarrays
simultaneously in Theta(m+n) time and compare two indices to find the smaller one and increment it. Then the remaining ones are printed.

For example in an array: [3,2,1,0], the recursion is going to be as follows:
recursive calls:		 [3,2,1,0]
						 /      / 
					[3,2]      [1,0]
					/   /      /   / 
				  [3]  [2]   [1]   [0] ---> (base-case) return these values and backtrack

backtracking:     [3]  [2]   [1]   [0] ---> returning values to prev calls (base-case)
				   /   /      /    /
				f([3],[2])   f([1],[0])
				  [2,3]       [0,1]
				    /          /
				  f([2,3],[0,1])
				  [0, 1, 2, 3] ---> return sorted result

where f is the efficient Theta(m+n) merge function of two arrays
"""

# Function to merge 2 arrays in Theta(m+n) time
def mergeArrs(arr, left_half, right_half):

	# index variables for result and halves
	k = 0; i = 0; j = 0

	while i < len(right_half) and j < len(left_half):

		# save the smaller one and increment index
		if left_half[i] <= right_half[j]:
			arr[k] = left_half[i]
			i += 1
		else:
			arr[k] = right_half[j]
			j += 1
		k += 1

	# save the remaining numbers in left half to result
	while i < len(left_half) and k < len(arr):
		arr[k] = left_half[i]
		k += 1; i += 1

	# save the remaining numbers in right half to result
	while j < len(right_half) and k < len(arr):
		arr[k] = right_half[j]
		k += 1; j += 1

	return arr

def mergeSort(arr):
	
	# base case for single element
	if len(arr) == 1:
		return
	
	# divide the array into two:
	left_half = arr[:len(arr) // 2]
	right_half = arr[len(arr) // 2:]

	# recursively sort halves
	mergeSort(left_half)
	mergeSort(right_half)

	# merge sorted halves and return result
	# debug: print(left_half, right_half, mergeArrs(arr, left_half, right_half))
	return mergeArrs(arr, left_half, right_half)

"""
4. Quick Sort:

There are three types of Partitions in Quick Sort: Naive, Lomuto and Hoare. 

(i) Naive: All elements smaller than a key should come before it, and bigger after it. To do this we append smaller elements to a temp
array and larger elements to a second temp array and concatenate the two. This takes linear time and linear space complexity.

(ii) Lomuto: This method takes linear time complexity and constant space complexity. In this partition we assume pivot (key) to be the
last element. We have to ensure that elements from 0 to i are smaller than pivot and i+1 to j are >= pivot. To do this we traverse the arr,
if a smaller element is found in (j+1,n) we swap it with i+1 and increment the window of smaller elements. For elements greater than pivot
we dont do anything. The last window size is i+1 and we insert the pivot here, hence computing the partitioned array.

(iii) Hoare: This is the most efficient partition algorithm, The pivot index is the first element. It runs in O(n) time and takes constant
space complexity. It uses do-while loop in C/C++ but since the loop doesn't exist in python it has not been implemented.

"""
def naivePartition(arr, low, high, p):
	pivot = arr[p]
	temp = [0] * (high - low + 1); k = 0
	# saving elements <= pivot
	for i in range(low, high + 1):
		if arr[i] <= pivot:
			temp[k] = arr[i]; k += 1
	# saving elements > pivot
	for i in range(low, high + 1):
		if arr[i] > pivot:
			temp[k] = arr[i]; k += 1
	# copying array and saving loc of pivot
	new_idx = 0
	for i in range(low, high + 1):
		arr[i] = temp[i - low]
		if arr[i] == pivot:
			new_idx = i

	return arr, new_idx

def lomutoPartition(arr, low, high):
	# default pivot is last element in array
	pivot = arr[high]
	# initialising window as first element of range
	windowLimit = low - 1
	for j in range(low, high):
		if arr[j] < pivot:
			# add to smaller window and increase window size
			windowLimit += 1
			# swapping the smaller element with element outside window
			arr[windowLimit], arr[j] = (arr[j], arr[windowLimit])
	# inserting pivot at end of the window limit
	arr[windowLimit + 1], arr[high] = (arr[high], arr[windowLimit + 1])

	return arr, windowLimit + 1

"""
The worst case time complexity in Quick Sort is O(n^2) but it can almost always be avoided by using any one of the three
partition fucntions and different intial pivot indices. Hence the average time complexity is O(nlogn). It is an in-place,
divide and conquer algorithm which makes lesser memory writes and thus is more cache friendly than Merge Sort. Quick Sort
is also tail recursive, as the last thing it does is the recursive call, even though python does not eliminate tail-call.
Naive Partition is stable but slower, in comparison Hoares and Lomuto is faster but unstable. In this algorithm:
(i) We insert the pivot into it's correct position in the array, and recursively sort the two partitions created.
(ii) (low, pivot) and (pivot+1, high) are sorted till there are no unsorted elements left in the subarray in base-case,
low >= high is only true when there is 1 element or no unsorted elements in array. We return at this point.
For example:                [9, 4, 3, 1, 10, |5|]
							pivot = 5, pivot_idx = 3
							[1, 4, 3, |5|, 10, 9]
							/                /
						QS(0,2)            QS(4,5)
					 [1,4,|3|]		       [10, |9|]
			pivot = 3, idx = 1				pivot = 9, idx = 4
				[1,|3|, 4]					[|9|, 10]
				/		/					/		/
			QS(0,0)   QS(4,4)			QS(4,4)   QS(5, 5)
			return	  return			return	   return

"""

def quickSort(arr, low, high):
	# base case is when no elements in range (low, high)
	if low >= high:
		return
	# obtain partitioned array and position
	arr, pivot_idx = lomutoPartition(arr, low, high)
	# recursively sort the the partitions
	quickSort(arr, low, pivot_idx - 1)
	quickSort(arr, pivot_idx + 1, high)

# arr = [9,4,3,1,10,5]
# quickSort(arr, 0, len(arr) - 1)
# print(arr)
