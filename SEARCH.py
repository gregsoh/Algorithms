'''
This code implements seach algorithms. 
'''

# Algorithm 1: Binary Search
# Input(s): array of sorted integers, left range, right range, input we are looking for
# Output(s): index
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

# Algorithm 2: Breadth First Search (applied to word ladder problem)
# Input(s): begin word, end word and wordlist (all words have same length)
# Output(s): length of transformation (at most 1 char can be changed for each transformation)
def breadthFirstSearch(begin, end, wordList):
	if begin == end: 
		return 0
	wordLength, wordListSize = len(begin), len(wordList)
	wordDict = {}
	for word in wordList:
		for j in range(wordLength):
			if word[ : j] + "-" +  word[j + 1 :] in wordDict:
				wordDict[word[ : j] + "-" +  word[j + 1 :]].append(word)
			else:
				wordDict[word[ : j] + "-" +  word[j + 1 :]] = [word]

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

#######################################################
### TESTS
#######################################################
def binarySearchTest():
	t1, t2 = [-1, 2, 3, 4, 5], [1, 1, 1, 1, 2] #tests
	r1, r2 = len(t1) - 1, len(t2) - 1 #range 1 & 2
	assert binarySearch(t1, 0, r1, 2) == 1; binarySearch(t1, 0, r1, 4) == 3
	assert binarySearch(t2, 0, r1, 3) == -1; binarySearch(t2, 0, r1, 2) == 4

def breadthFirstSearchTest():
	assert breadthFirstSearch("hit", "cog", ["hot","dot","dog","lot","log","cog"]) == 5

def mainTest():
	binarySearchTest()
	breadthFirstSearchTest()

mainTest()