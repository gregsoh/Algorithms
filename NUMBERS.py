'''
This code implements algorithms related to prime numbers (or natural numbers). 
'''
import math

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

def mainTest():
	isPrimeTest()
	primeListTest()
	fastPowerTest()
	squareRootTest()

mainTest()