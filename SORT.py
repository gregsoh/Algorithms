'''
This code file implements sorting algorithms. 
Note: For understandability, "v" in the code refers to temporary variable
'''

'''
Algorithm 1: Insertion Sort
Input(s): array of numbers
Output(s): sorted array
Notes: O(N^2) time; O(1) Aux Space; in-place
'''
def insertionSort(arr):
	for idx in range(1, len(arr)):
		key = arr[idx]
		pointer = idx - 1
		while pointer >= 0 and arr[pointer] > key:
			arr[pointer + 1] = arr[pointer]
			pointer -= 1
		arr[pointer + 1] = key
	return arr

'''
Algorithm 2: Selection Sort
Input(s): array of numbers
Output(s): sorted array
Notes: O(N^2) time; O(1) Aux Space; in-place
'''
def selectionSort(arr):
	size = len(arr)
	pointer = 0
	while pointer < size - 1:
		minimum = pointer
		for idx in range(pointer, size):
			if arr[idx] < arr[pointer]:
				minimum = idx
		v = arr[pointer] # additional space
		arr[pointer] = arr[minimum]
		arr[minimum] = v
		pointer += 1
	return arr

'''
Algorithm 3: Bubble Sort
Input(s): array of numbers
Output(s): sorted array
Notes: Worst is O(N^2) time; O(1) Aux Space; in-place
'''
def bubbleSort(arr): 
	def swap(array, idx):
		v = arr[idx - 1]
		arr[idx - 1] = arr[idx]
		arr[idx] = v
	
	size = len(arr)
	pointer = size
	for _ in range(size - 1):
		for j in range(1, pointer):
			if arr[j - 1] > arr[j]:
				swap(arr, j)
		pointer -= 1 #mini optimization
	return arr

'''
Algorithm 4: Count Sort
Input(s): array of numbers and upper limit of range (0 to N inclusive)
Output(s): sorted array
Notes: O(n + k); O(k) Aux Space; not in-place; stable
'''
def countSort(arr, N): 
	size = len(arr)
	counter = [0 for i in range(N + 1)]
	newarr = [0 for i in range(size)]
	for itm in arr:
		counter[itm] += 1
	for idx in range(1, N + 1):
		counter[idx] += counter[idx - 1] 
	for idx in range(size - 1, -1, -1): #this ensures in-place
		itm = arr[idx]
		newarr[counter[itm] - 1] = itm
		counter[itm] -= 1 
	return newarr

'''
Algorithm 5: Quick Sort
Input(s): array of numbers, low and high index
Output(s): sorted array
Notes: O(n logn); O(logn) Aux Space; in-place; not stable
'''
def quickSort(arr, low, high):
	def swap(arr, l, h):
		v = arr[l]
		arr[l] = arr[h]
		arr[h] = v

	def partition(arr, l, h): 
		pivot = h
		s, e = l, h - 1 #s = start; e = end
		while s <= e:
			while arr[s] <= arr[pivot] and s <= e: 
				s += 1
			while arr[e] > arr[pivot] and s <= e: 
				e -= 1
			if s < e: 
				swap(arr, s, e)
		#swap final position
		v = arr[s]
		arr[s] = arr[pivot]
		arr[pivot] = v
		return s

	if low < high:
		idx = partition(arr, low, high)
		quickSort(arr, low, idx - 1)
		quickSort(arr, idx + 1, high)
	return arr

'''
Algorithm 6: Merge Sort
Input(s): array of numbers
Output(s): sorted array
Notes: O(n logn); O(n) Aux Space; not in-place; stable
'''
def mergeSort(arr):
	if len(arr) >= 2: 
		MID = len(arr) // 2
		LEFT = arr[0: MID]
		RIGHT = arr[MID: len(arr)]
		a = mergeSort(LEFT)
		b = mergeSort(RIGHT)

		c1, c2, v = 0, 0, []
		while c1 < len(a) and c2 < len(b):
			if a[c1] < b[c2]:
				v.append(a[c1])
				c1 += 1
			else:
				v.append(b[c2])
				c2 += 1
		# handle residual
		if c1 == len(a):
			v += b[c2 : len(b)]
		if c2 == len(b):
			v += a[c1 : len(a)]
		return v
	return arr

'''
Algorithm 7: Heap Sort
Input(s): array of numbers
Output(s): sorted array
Notes: O(n logn); O(1) Aux Space; in-place; not stable
'''
def heapSort(arr):
	def swap(arr, a, b):
		v = arr[a]
		arr[a] = arr[b]
		arr[b] = v

	def minHeap(arr, size, idx):
		l, r = 2 * idx + 1, 2 * idx + 2
		smallest = idx
		if l < size and arr[l] < arr[smallest]: 
			smallest = l
		if r < size and arr[r] < arr[smallest]:
			smallest = r
		if smallest != idx:
			swap(arr, smallest, idx)
			minHeap(arr, size, smallest) #trickle down

	def buildHeap(arr, size):
		for idx in range(size // 2 - 1, -1, -1):
			minHeap(arr, size, idx)

	size = len(arr)
	buildHeap(arr, size)
	for idx in range(size):
		v = arr[size - 1]
		arr[size - 1] = arr[0]
		arr[0] = v
		size -= 1
		minHeap(arr, size, 0)
	return arr

'''
Algorithm 8: Radix Sort
Input(s): array of non-negative numbers, radix, num characters of max element k
Output(s): sorted array
Notes: O(nk) n words, k characters; O(n + r) Aux Space, where r is radix; not in-place; stable
'''
def radixSort(arr, radix, k):
	num = len(arr)
	for k_i in range(k):
		pop = dict(zip(radix, [[] for i in range(len(radix))]))
		for n in arr:
			pop[(n // (10 ** k_i)) % 10].append(n)
		newarr = []
		for _, val in pop.items():
			for v in val:
				newarr.append(v)
		arr = newarr
	return arr

'''
Algorithm 9: Stooge Sort
Input(s): array of numbers, left and right
Output(s): sorted array
Notes: O(n^2.7); Organizes the first 2/3, last 2/3 and first 2/3 again
'''
def stoogeSort(arr, l, r):
	def swap(arr, a, b):
		v = arr[a]
		arr[a] = arr[b]
		arr[b] = v

	if arr[l] > arr[r]:
		swap(arr, l, r)
	if r - l <= 1:
		return

	while r - l + 1 >= 2:
		p = (r - l + 1) // 3
		stoogeSort(arr, l, r - p)
		stoogeSort(arr, l + p, r)
		stoogeSort(arr, l, r - p)
		return arr


#######################################################
### TESTS
#######################################################
def insertionSortTest():
	t1, t2, t3, t4 = [2], [3, 2], [3, 9, -2], [3, 2, 1, 1, 0] #tests
	r1, r2, r3, r4 = [2], [2, 3], [-2, 3, 9], [0, 1, 1, 2, 3] #expected results

	assert insertionSort(t1) == r1; assert insertionSort(t2) == r2
	assert insertionSort(t3) == r3; assert insertionSort(t4) == r4

def selectionSortTest():
	t1, t2, t3, t4 = [2], [3, 2], [3, 9, -2], [3, 2, 1, 1, 0] #tests
	r1, r2, r3, r4 = [2], [2, 3], [-2, 3, 9], [0, 1, 1, 2, 3] #expected results

	assert selectionSort(t1) == r1; assert selectionSort(t2) == r2
	assert selectionSort(t3) == r3; assert selectionSort(t4) == r4

def bubbleSortTest():
	t1, t2, t3, t4 = [-1], [1, 0], [2, 3, -2], [3, 2, 1, 1, 0] #tests
	r1, r2, r3, r4 = [-1], [0, 1], [-2, 2, 3], [0, 1, 1, 2, 3] #expected results

	assert bubbleSort(t1) == r1; assert bubbleSort(t2) == r2
	assert bubbleSort(t3) == r3; assert bubbleSort(t4) == r4

def countSortTest():
	t1, t2, t3, t4 = [1], [1, 0], [2, 3, 7], [3, 2, 1, 1, 0] #tests
	r1, r2, r3, r4 = [1], [0, 1], [2, 3, 7], [0, 1, 1, 2, 3] #expected results

	assert countSort(t1, 1) == r1; assert countSort(t2, 1) == r2
	assert countSort(t3, 7) == r3; assert countSort(t4, 3) == r4

def quickSortTest():
	t1, t2, t3, t4, t5 = [1], [1, -1], [1, 0, 3], [2, 1, 3, 7], [3, 2, 1, 1, 0] #tests
	r1, r2, r3, r4, r5 = [1], [-1, 1], [0, 1, 3], [1, 2, 3, 7], [0, 1, 1, 2, 3] #expected results

	assert quickSort(t1, 0, 0) == r1; assert quickSort(t2, 0, 1) == r2
	assert quickSort(t3, 0, 2) == r3; assert quickSort(t4, 0, 3) == r4
	assert quickSort(t5, 0, 4) == r5

def mergeSortTest():
	t1, t2, t3, t4, t5 = [1], [1, -1], [1, 1, 1], [2, 1, 5, 7], [3, 2, 1, 1, 0] #tests
	r1, r2, r3, r4, r5 = [1], [-1, 1], [1, 1, 1], [1, 2, 5, 7], [0, 1, 1, 2, 3] #expected results

	assert mergeSort(t1) == r1; assert mergeSort(t2) == r2
	assert mergeSort(t3) == r3; assert mergeSort(t4) == r4
	assert mergeSort(t5) == r5

def heapSortTest():
	t1, t2, t3, t4, t5 = [-1, 1], [1, 1, 1], [1, 2, 7, 5], [2, 1, 1, 3, 0], [0, 1, 2, 3, 4] #tests
	r1, r2, r3, r4, r5 = [1, -1], [1, 1, 1], [7, 5, 2, 1], [3, 2, 1, 1, 0], [4, 3, 2, 1, 0] #expected results

	assert heapSort(t1) == r1; assert heapSort(t2) == r2
	assert heapSort(t3) == r3; assert heapSort(t4) == r4
	assert heapSort(t5) == r5

def radixSortTest():
	assert radixSort([23, 34, 11], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 2) == [11, 23, 34]
	assert radixSort([23, 34, 11, 100], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 3) == [11, 23, 34, 100]
	assert radixSort([23, 34, 10, 103], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 3) == [10, 23, 34, 103]
	assert radixSort([23, 23, 10, 34], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 2) == [10, 23, 23, 34]
	assert radixSort([2, 23, 117, 3423], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 4) == [2, 23, 117, 3423]

def stoogeSortTest():
	assert stoogeSort([23, 34, 11], 0, 2) == [11, 23, 34]
	assert stoogeSort([23, 34, 11, 100], 0, 3) == [11, 23, 34, 100]
	assert stoogeSort([23, 34, 10, 103], 0, 3) == [10, 23, 34, 103]
	assert stoogeSort([23, 23, 10, 34], 0, 3) == [10, 23, 23, 34]
	assert stoogeSort([2, 23, 117, 3423], 0, 3) == [2, 23, 117, 3423]

def mainTest():
	insertionSortTest()
	selectionSortTest()
	bubbleSortTest()
	countSortTest()
	quickSortTest()
	mergeSortTest()
	heapSortTest()
	radixSortTest()
	stoogeSortTest()

mainTest()