'''
This code implements general algorithms I find interesting. 
There are more that I have seen but I did not have the opportunity to code it up myself. I will add it to this code base whenever I have the time. 
'''
import math
import numpy as np
from DATASTRUCT import linkedlist, node

# Algorithm 1: Determinisitc policy to see if number is prime
# Input(s): natural number
# Output(s): true/false if number is prime
def isPrime(num):
	if num == 1:
		return False
	c = 2
	while c * c <= num:
		if num % c == 0:
			return False
		c += 1
	return True

# Algorithm 2: Sieve of Eratosthenes -- find all primes <= a number 
# Input(s): natural number
# Output(s): list of primes
def primeList(num):
	if num == 1:
		return []
	if num == 2 or num == 3:
		return [2]
	prime = [1 for i in range(num + 1)]
	pop, c = [], 2
	while c * c <= num:
		if prime[c] == 1:
			pop.append(c)
			for j in range(c * c, num + 1, c):
				prime[j] = 0
		c += 1
	for k in range(c, num + 1):
		if prime[k] == 1:
			pop.append(k)
	return pop

# Algorithm 3: Fast Power -- calculating a ** b efficiently
# Input(s): a, b; both natural numbers
# Output(s): a ** b
def fastPower(a, b):
	r = 1
	while b > 0:
		if b % 2 == 0: 
			a = a ** 2
			b /= 2
		else:
			r *= a
			b -= 1
			a = a ** 2
			b /= 2
	return r

# Algorithm 4: Square root -- \sqrt{k} using Newton's method
# Input(s): num, x0, numIter
# Output(s): approximate value of \sqrt{k}
def squareRoot(num, x0, numIter):
	for itr in range(numIter):
		x0  += - (x0 ** 2 - num) / (2 * x0) 
	return x0

# Algorithm 5: String matching algorithm (Knuth-Morris-Pratt algorithm)
# Input(s): string, pattern
# Output(s): index of match
def stringSearch(string, pattern):
	s, p = list(string), list(pattern)

	# preprocessing
	length = len(p)
	v = [0 for _ in range(length)]
	i, j = 0, 1
	for j in range(1, length):
		if p[i] == p[j]:
			v[j] = i + 1
			i += 1
		else:
			if i != 0:
				i = v[i - 1]

	# main algorithm
	track = 0
	for idx, char in enumerate(s):
		if char == p[track]: 
			track += 1
		else:
			if track >= 1:
				track = v[track - 1]
		if track == length:
			return idx - length + 1
	return -1

# Algorithm 6: Rabin-Karp String Matching Algorithm
# Input(s): string, pattern, prime #
# Output(s): is there a match?
def rabinKarp(string, pattern, prime):
	s, p = list(string), list(pattern)
	ttl = 0
	for idx, itm in enumerate(p):
		ttl += ord(itm) * prime ** (idx)

	check = 0
	for idx in range(len(s) - len(p)):
		if idx == 0:
			win = s[0 : len(p)]
			for idx2, itm in enumerate(win):
				check += ord(itm) * prime ** (idx2)
		else:
			check -= ord(s[idx - 1])
			check /= prime 
			check += ord(s[idx + len(p) - 1]) * prime ** (len(p) - 1)

		if check == ttl:
			confirm = True
			for itr in range(len(p)):
				if p[itr] != s[idx + itr]:
					confirm = False
			if confirm == True:
				return True
	return False

# Algorithm 7: Kadane's Algorithm (solution to common problem: Largest Sum Contiguous Subarray)
# Input(s): list of positive or negative numbers
# Output(s): max value of contiguous subarray
def kadane(num):
	track, ttl = 0, 0
	for idx in range(len(num)):
		ttl += num[idx]
		ttl = max(ttl, 0)
		if ttl > track:
			track = ttl
	return track

# Algorithm 8: Von Mises Iteration (produces greatest eigenvalue of matrix)
# Input(s): Matrix (must be diagonalizable), size of matrix, epoch
# Output(s): largest eigenvalue, and associated eigen vector
# Inspiration: https://www.scribd.com/document/264003151/Power-Method-Proof (proof is attached)
def vonMisesIter(matrix, size, epoch):
	X = np.random.rand(size, 1)
	eival = 0
	for _ in range(epoch):
		Y = np.matmul(matrix, X)
		eival = max(abs(Y))
		X = np.divide(Y, eival)
	return eival, X

# Algorithm 9: Floyd Cycle
# Input(s): linkedlist
# Output(s): index of linkedlist where loop begins (otherwise returns -1)
# Runs in O(n) with no auxilary space
def floydCycle(l):
	slow, fast = l.head, l.head
	if fast == None: # check if there is even a node
		return -1
	while fast.next and fast.next.next:
		fast = fast.next.next
		slow = slow.next
		if fast.value == slow.value:
			slow = l.head
			while slow and fast: 
				fast = fast.next
				slow = slow.next
				if slow.value == fast.value:
					return slow.value
	return -1

#######################################################
### TESTS
#######################################################
def isPrimeTest():
	assert isPrime(1) == False; assert isPrime(2) == True
	assert isPrime(3) == True; assert isPrime(4) == False
	assert isPrime(7) == True; assert isPrime(10) == False

def primeListTest():
	assert primeList(1) == []
	assert primeList(2) == [2]
	assert primeList(3) == [2]
	assert primeList(5) == [2, 3, 5]
	assert primeList(8) == [2, 3, 5, 7]

def fastPowerTest():
	assert fastPower(3, 5) == 243
	assert fastPower(6, 15) == 470184984576

def squareRootTest():
	def withinLimits(result, tol, num):
		if result <= math.sqrt(num) + tol and result >= math.sqrt(num) - tol:
			return True
		return False
	tol = 10 ** -3
	numIter = 10
	assert withinLimits(squareRoot(5, 2, numIter), tol, 5) == True
	assert withinLimits(squareRoot(17, 3, numIter), tol, 17) == True
	assert withinLimits(squareRoot(19, 5, numIter), tol, 19) == True

def stringSearchTest():
	assert stringSearch("abcdefg", "abc") == 0
	assert stringSearch("abcdefg", "cde") == 2
	assert stringSearch("abcdefg", "efg") == 4
	assert stringSearch("abcdefg", "sfh") == -1
	assert stringSearch("abcdefgabj", "abj") == 7
	assert stringSearch("abcdefgabc", "abc") == 0

def rabinKarpTest():
	assert rabinKarp("abc", "b", 5) == True
	assert rabinKarp("afjz", "fa", 11) == False
	assert rabinKarp("afjz", "fj", 11) == True
	assert rabinKarp("abcdesdfs1fg", "fas", 11) == False
	assert rabinKarp("abcdesdfs1fgadkjhafjkhkj2h34jk23k4hj23h4jkhads", "adflksdnfkjadhfjksajdkfb", 101) == False
	assert rabinKarp("4jk23k4hj23h4jkhadsasdfasdf", "j23h4jkhads", 23) == True

def kadaneTest():
	assert kadane([-2, -3, 4, -1, -2, 1, 5, -3]) == 7
	assert kadane([-1, -2, 3, 4, 5, -1, -5, -3]) == 12
	assert kadane([-1, 5, -1, 4, 5, -1, -5, -3]) == 13

def vonMisesIterTest():
	def withinLimits(result, tol, actual, vector):
		if vector == False:
			if result <= actual + tol and result >= actual - tol:
				return True
			return False
		else:
			for itm in range(len(actual)):
				if result[itm] > actual[itm] + tol and result[itm] < actual[itm] - tol:
					return False
			return True
	tol = 10 ** -3
	matrix1 = np.array([[-2, -4, 2 ], [-2, 1, 2], [4, 2, 5]])
	a, b = vonMisesIter(matrix1, 3, 100)
	assert withinLimits(a, tol, 6, False) == True
	assert withinLimits(b, tol, [1, 6, 16], True) == True

	matrix2 = np.array([[2, 2], [5, -1]])
	a, b = vonMisesIter(matrix2, 2, 1000)
	assert withinLimits(a, tol, 4, False) == True
	assert withinLimits(b, tol, [1, 1], True) == True

def floydCycleTest():
	#Test 1
	LL = linkedlist()
	for itm in range(10, 0, -1):
		LL.insert(itm)
	assert floydCycle(LL) == -1
	# Test 2
	LL = linkedlist()
	for itm in range(10, 0, -1):
		LL.insert(itm)
	LL.connect(5, 9)
	#LL.check()
	assert floydCycle(LL) == 5

	# Test 3
	LL = linkedlist()
	for itm in range(25, 0, -1):
		LL.insert(itm)
	LL.connect(19, 25)
	#LL.check()
	assert floydCycle(LL) == 19

def mainTest():
	isPrimeTest()
	primeListTest()
	fastPowerTest()
	squareRootTest()
	stringSearchTest()
	rabinKarpTest()
	kadaneTest()
	vonMisesIterTest()
	floydCycleTest()

mainTest()