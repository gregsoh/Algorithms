'''
This code implements sorting algorithms. 
v in the code often refers to temporary variable
'''

# Algorithm 1: Selection Sort
# Input(s): array of numbers
# Output(s): sorted array
# Notes: O(N^2) time; O(1) Aux Space; in-place
def selectionSort(arr):
	size = len(arr)
	c = 0
	while c < size - 1:
		minimum = c
		for idx in range(c, size):
			if arr[idx] < arr[c]:
				minimum = idx
		v = arr[c] # additional space
		arr[c] = arr[minimum]
		arr[minimum] = v
		c += 1
	return arr

# Algorithm 2: Bubble Sort
# Input(s): array of numbers
# Output(s): sorted array
# Notes: Worst is O(N^2) time; O(1) Aux Space; in-place
def bubbleSort(arr): 
	def swap(array, idx):
		v = arr[idx - 1]
		arr[idx - 1] = arr[idx]
		arr[idx] = v
	size = len(arr)
	c = size
	for i in range(size - 1):
		for j in range(1, c):
			if arr[j - 1] > arr[j]:
				swap(arr, j)
		c -= 1
	return arr

# Algorithm 3: Count Sort
# Input(s): array of numbers and upper limit of range (0 to max N)
# Output(s): sorted array
# Notes: O(n + k); O(k) Aux Space; not in-place; stable
def countSort(arr, N): 
	size = len(arr)
	counter = [0 for i in range(N + 1)]
	newarr = [0 for i in range(size)]
	for itm in arr:
		counter[itm] += 1
	for idx in range(1, N + 1):
		counter[idx] += counter[idx - 1] 
	for idx in range(size - 1, -1, -1):
		itm = arr[idx]
		newarr[counter[itm] - 1] = itm
		counter[itm] -= 1 
	return newarr

# Algorithm 4: Quick Sort
# Input(s): array of numbers, low and high index
# Output(s): sorted array
# Notes: O(n logn); O(logn) Aux Space; in-place; not stable
def quickSort(arr, low, high):
	def swap(arr, l, h):
		v = arr[l]
		arr[l] = arr[h]
		arr[h] = v

	def partition(arr, l, h): 
		pivot = h
		s, e = l, h - 1
		while s <= e:
			while arr[s] <= arr[pivot] and s <= e: 
				s += 1
			while arr[e] > arr[pivot] and s <= e: 
				e -= 1
			if s < e: 
				swap(arr, s, e)
		v = arr[s]
		arr[s] = arr[pivot]
		arr[pivot] = v
		return s

	if low < high:
		idx = partition(arr, low, high)
		quickSort(arr, low, idx - 1)
		quickSort(arr, idx + 1, high)
	return arr

# Algorithm 5: Merge Sort
# Input(s): array of numbers
# Output(s): sorted array
# Notes: O(n logn); O(n) Aux Space; not in-place; stable
def mergeSort(arr):
	if len(arr) >= 2: 
		midpt = len(arr) // 2
		LEFT = arr[0: midpt]
		RIGHT = arr[midpt: len(arr)]
		a = mergeSort(LEFT)
		b = mergeSort(RIGHT)

		c1, c2, v = 0, 0, []
		while c1 < len(a) and c2 < len(b):
			if a[c1] < b[c2]:
				v.append(a[c1])
				c1 += 1
			elif a[c1] >= b[c2]:
				v.append(b[c2])
				c2 += 1
		if c1 == len(a):
			v += b[c2 : len(b)]
		if c2 == len(b):
			v += a[c1 : len(a)]
		return v
	return arr

# Algorithm 6: Heap Sort
# Input(s): array of numbers
# Output(s): sorted array
# Notes: O(n logn); O(1) Aux Space; in-place; not stable
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

# Algorithm 7: Radix Sort
# Input(s): array of non-negative numbers, radix, num characters of max element k
# Output(s): sorted array
# Notes: O(nk) n words, k characters; O(n + r) Aux Space, where r is radix; not in-place; stable
def radixSort(arr, radix, k):
	num = len(arr)
	for k_i in range(k):
		pop = dict(zip(radix, [[] for i in range(len(radix))]))
		for n in arr:
			pop[(n // (10 **  k_i)) % 10].append(n)
		newarr = []
		for key, val in pop.items():
			for v in val:
				newarr.append(v)
		arr = newarr
	return arr

#######################################################
### TESTS
#######################################################
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

def mainTest():
	selectionSortTest()
	bubbleSortTest()
	countSortTest()
	quickSortTest()
	mergeSortTest()
	heapSortTest()
	radixSortTest()

mainTest()