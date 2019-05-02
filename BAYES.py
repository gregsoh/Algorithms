'''
This code implements algorithms related to Bayes. 
'''
import math
import numpy as np

'''
Naive Bayes (assume binary classification)
Input: Datapoints in the tuple form ([data], classifiction), test_train_split, number of classes
Output: accuracies
Note: inspired by https://chrisalbon.com/machine_learning/naive_bayes/naive_bayes_classifier_from_scratch/
'''
def NaiveBayes(datapoints, test_train_split, numClass):
	def splitData(data, p):
		numData = len(data)
		train, test = data[:int(p * numData)], data[int(p * numData):]
		return train, test

	# Input: list of tuples
	def classificationbyClass(data):
		pop = {} #pop stands for population table
		for d, c in data:
			if c not in pop:
				pop[c] = []
			pop[c].append(d)
		return pop

	# Input: list of data 
	def mean(numbers):
		return sum(numbers) / len(numbers)

	# Input: list of numbers
	def sD(numbers, sample): #checks if this is sample? 
		m = mean(numbers)
		div = len(numbers) if not sample else len(numbers) - 1 #key step on whether we are measuring variance of population or sample
		return math.sqrt(sum([math.pow((num - m), 2) for num in numbers]) / div)

	# Input: list of list
	def summarize(data):
		return [(mean(list(d)), sD(list(d), False)) for d in zip(*data)]

	# Input: list of tuples
	def summarizeByClass(data):
		pop = classificationbyClass(data)
		newpop = {}
		for key, value in pop.items():
			newpop[key] = summarize(value)
		return newpop # key: class value and values: (mean, SD) of each attribute

	def gaussian(x, mean, SD):
		if SD != 0:
			exp = math.exp(-( math.pow((x - mean), 2) / (2 * math.pow(SD, 2))))
			return (1 / (math.pow(2 * math.pi, 0.5) * SD)) * exp
		else:
			return 1 if x == mean else 0

	def prediction(pop, test, prior):
		def predict(pop, d):
			prob = {}
			for key, value in pop.items():
				prob[key] = prior[key]
				for idx, val in enumerate(value):
					m, s = val #(mean, standard deviation)
					prob[key] *= gaussian(d[idx], m, s)
			classification, bestProb = None, 0.
			for c, value in prob.items():
				if classification == None or value > bestProb:
					bestProb = value
					classification = c
			return classification
		r = []
		for d, c in test:
			r.append(predict(pop, d))
		return r
	def accuracy(test, result):
		truepositive, truenegative, falsepositive, falsenegative = 0, 0, 0, 0
		for idx in range(len(test)):
			d, c = test[idx]
			if c == result[idx]:
				if c == 1:
					truepositive += 1
				else:
					truenegative += 1
			if c != result[idx]:
				if result[idx] == 1: 
					falsepositive += 1
				else:
					falsenegative += 1
		return truepositive, truenegative, falsepositive, falsenegative

	train, test = splitData(datapoints, test_train_split)
	pop = summarizeByClass(train)
	prior = [0 for _ in range(numClass)]
	for t in train: 
		f, c = t
		prior[c] += 1 / len(train)
	result = prediction(pop, test, prior)
	tp, tn, fp, fn = accuracy(test, result)
	print(tp, tn, fp, fn)
	return (tp, tn, fp, fn)



#######################################################
### TESTS
#######################################################
def NaiveBayesTest():
	def test_1():
		a = (np.array([2.]), 1)
		b = (np.array([1.]), 0)
		c = (np.array([-1.]), 0)
		d = (np.array([3]), 1)
		e = (np.array([2.75]), 1)
		data = [a, b, c, d, e]
		assert NaiveBayes(data, 0.8, 2) == (1, 0, 0, 0)
	def test_2():
		a = (np.array([2., 1.]), 1)
		b = (np.array([1., 0.5]), 0)
		c = (np.array([-1., -2.]), 0)
		d = (np.array([3., 4.]), 1)
		e = (np.array([2.75, 6]), 1)
		data = [a, b, c, d, e]
		assert NaiveBayes(data, 0.8, 2) == (1, 0, 0, 0)
	test_1()
	test_2()
NaiveBayesTest()

