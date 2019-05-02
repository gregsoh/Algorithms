'''
This code implements seach algorithms. 
'''
'''
Algorithm 1: Binary Search
Input(s): array of sorted integers, left range, right range, element we are searching
Output(s): index
'''
def binarySearch(arr, l, r, itm):
	if r - l <= 1:
		return -1
	size = r - l + 1
	midpt = size // 2

	if arr[l + midpt] == itm:
		return l + midpt
	if arr[l + midpt] <= itm:
		return binarySearch(arr, l + midpt, r, itm)
	else:
		return binarySearch(arr, l, l + midpt, itm)

'''
Algorithm 2: Interpolation Search
Input(s): array of sorted integers, left range, right range, element we are searching
Output(s): index
Comments: If elements are uniformly distributed, O(log(log n)); Worst Case: O(n)
'''
def interpolationSearch(arr, l, r, itm):
	if r - l <= 1:
		return -1
	size = r - l + 1
	if arr[r] - arr[l] == 0:
		return 0 if arr[l] == itm else -1
	ratio = (itm - arr[l]) / (arr[r] - arr[l])
	midpt = int(ratio * (r - l + 1) - 1)
	if ratio > 1: # Check if it is even sensible 
		return -1 
	if midpt == -1: #Indicates first entry
		return 0 
	if arr[l + midpt] == itm:
		return l + midpt
	if arr[l + midpt] <= itm:
		return interpolationSearch(arr, l + midpt, r, itm)
	else:
		return interpolationSearch(arr, l, l + midpt, itm)

'''
Algorithm 3: Jump Search
Input(s): array of sorted integers, jumpstep, element we are searching
Output(s): index
Comments: O(n / m + m + 1); By differentiating, we note that optimal jumpstep m = sqrt(n)
'''
def jumpSearch(arr, jumpstep, itm):
	pointer, size = 0, len(arr) - 1
	while arr[pointer] < itm and pointer < size:
		pointer += jumpstep 
	l, r = pointer - jumpstep + 1, pointer
	if pointer >= size:
		l, r = size - jumpstep, size - 1
	if pointer == 0: 
		return 0
	# linear search
	for idx in range(l, r + 1):
		if arr[idx] == itm:
			return idx
	return -1

'''
Algorithm 4: Breadth First Search (applied to word ladder problem)
Input(s): begin word, end word and wordlist (all words have same length)
Output(s): length of transformation (at most 1 char can be changed for each transformation)
'''
def breadthFirstSearch(begin, end, wordList):
	if begin == end: 
		return 0
	wordLength, wordListSize = len(begin), len(wordList)
	wordDict = {}
	#Preprocessing
	for word in wordList:
		for j in range(wordLength):
			if word[ : j] + "-" +  word[j + 1 :] in wordDict:
				wordDict[word[ : j] + "-" +  word[j + 1 :]].append(word)
			else:
				wordDict[word[ : j] + "-" +  word[j + 1 :]] = [word]
	#Actual BFS
	q = [(begin, 1)]
	v = set(); v.add(begin)
	while q:
		word, level = q.pop(0)
		for b in range(wordLength):
			intermediate = word[ : b] + "-" + word[b + 1 : ]
			if intermediate in wordDict:
				for itm in wordDict[intermediate]:
					if itm == end:
						return level + 1
					if itm not in v:
						v.add(itm)
						q.append((itm, level + 1))
	return 0

'''
Algorithm 5: Depth First Search (applied to stepping numbers: adjacent digits have an absolute difference of 1)
Input(s): n, m (lower and upper range inclusive respectively)
Output(s): set of all stepping numbers
'''
def steppingNumbers(n, m):
	def DFS(pop, n, m, num):
		if num <=m and num >= n: 
			pop.add(num)
		if num >= m or num ==0:
			return
		lastDigit = num % 10
		lower, upper = max(lastDigit - 1, 0), max((lastDigit + 1) % 10, 9)
		if lower != lastDigit:
			DFS(pop, n, m, 10 * num + lastDigit - 1)
		if upper != lastDigit:
			DFS(pop, n, m, num * 10 + lastDigit + 1)

	population = set()
	for startingDigit in range(0, 10):
		DFS(population, n, m, startingDigit)
	return population

#######################################################
### TESTS
#######################################################
def binarySearchTest():
	t1, t2 = [-1, 2, 3, 4, 5], [1, 1, 1, 1, 2] #tests
	r1, r2 = len(t1) - 1, len(t2) - 1 #range 1 & 2
	assert binarySearch(t1, 0, r1, 2) == 1; binarySearch(t1, 0, r1, 4) == 3
	assert binarySearch(t2, 0, r2, 3) == -1; binarySearch(t2, 0, r2, 2) == 4

def interpolationSearchTest():
	t1, t2, t3 = [-1, 2, 3, 4, 5], [1, 1, 1, 1, 2], [2, 2, 2, 2] #tests
	r1, r2, r3 = len(t1) - 1, len(t2) - 1, len(t3) - 1 #range 1 & 2
	assert interpolationSearch(t1, 0, r1, 2) == 1; interpolationSearch(t1, 0, r1, 4) == 3
	assert interpolationSearch(t2, 0, r2, 3) == -1; interpolationSearch(t2, 0, r2, 2) == 4
	assert interpolationSearch(t2, 0, r2, 1) == 0; assert interpolationSearch(t3, 0, r3, 2) == 0
	assert interpolationSearch(t3, 0, r3, 4) == -1

def jumpSearchTest():
	t1, t2 = [-1, 2, 3, 4, 5], [1, 1, 1, 1, 2] #tests
	assert jumpSearch(t1, 2, 2) == 1; assert jumpSearch(t1, 1, 4) == 3 
	assert jumpSearch(t1, 2, 4) == 3; assert jumpSearch(t2, 3, 1) == 0 

def breadthFirstSearchTest():
	assert breadthFirstSearch("hit", "cog", ["hot","dot","dog","lot","log","cog"]) == 5

def depthFirstSearchTest():
	assert steppingNumbers(10, 15) == set([10, 12])
	assert steppingNumbers(0, 21) == set([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 21])

def mainTest():
	binarySearchTest()
	interpolationSearchTest()
	breadthFirstSearchTest()
	jumpSearchTest()
	depthFirstSearchTest()

mainTest()