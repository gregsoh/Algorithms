'''
This code implements machine learning algorithms from scratch (with understanding of the math behind algorithm). 
'''
import random, math
import numpy as np
import matplotlib.pyplot as plt

'''
Algorithm 1: Linear Regression (basic)
Input(s): list of x, list of y, number of data points
Output(s): slope and intercept
Note: We are doing ordinary least squares with the error = (difference) ^ 2
       Methodology employed is to take partial derivatives and use Ax = b to solve the equation 
       Understanding of matrix determinants, inverses is necessary
       Let the equation be y = mx + b
       Inspiration: https://stackoverflow.com/questions/27092203/how-do-i-determine-the-coefficients-for-a-linear-regression-line-in-matlab
'''
def basicLinearRegression(x, y, num):
	sum_x, sum_x2 = sum(x), sum([itm ** 2 for itm in x])
	sum_y, sum_y2 = sum(y), sum([itm ** 2 for itm in y])
	sum_product = sum([x[i] * y[i] for i in range(num)])

	m = (sum_x * sum_y - num * sum_product) / ((sum_x) ** 2 - num * sum_x2)
	b = (sum_product * sum_x - sum_y * sum_x2) / ((sum_x) ** 2 - num * sum_x2)
	return m, b

'''
Algorithm 2: Multi Regression (basic)
Input(s): list of x1, list of x2, list of y, number of data points
Output(s): two weights and intercept
Note: We are doing ordinary least squares with the error = (difference) ^ 2
       Methodology employed is to stochastic gradient descent/ batch gradient descent
       Understanding of partial derivatives and back propagation is necessary
       Let the equation be y = w1x1 w2x2 + b
       Inspiration: https://towardsdatascience.com/step-by-step-tutorial-on-linear-regression-with-stochastic-gradient-descent-1d35b088a843
'''
def basicMultiRegression(x1, x2, y, num):
	def batchProcessing(numInBatch, x1, x2, y, num):
		numBatches = num // numInBatch
		c = 0
		x1T, x2T, yT = [], [], [] #transformed
		for idx in range(numBatches):
			if c + numInBatch < num:
				x1T.append(x1[c: c + numInBatch])
				x2T.append(x2[c: c + numInBatch])
				yT.append(  y[c: c + numInBatch])
			else:
				x1T.append(x1[c: num])
				x2T.append(x2[c: num])
				yT.append(  y[c: num])
			c += numInBatch
		return x1T, x2T, yT
	def calculateLoss(b, w1, w2, x1, x2, y):
		err = 0
		for idx in range(len(x1)):
			err += (w1 * x1[idx] + w2 * x2[idx] + b - y[idx]) ** 2
		return err
	# constants
	eta = 0.001
	epoch = 100000
	
	# main code
	numInBatch = 1 # num elements in batch
	numBatches = num // numInBatch # number of batches
	x1T, x2T, yT = batchProcessing(numInBatch, x1, x2, y, num)
	w1, w2, b = random.uniform(-0.1, 0.1), random.uniform(-0.1, 0.1), random.uniform(-0.1, 0.1)
	for _ in range(epoch):
		for bNum in range(numBatches):
			x1b, x2b, yb = x1T[bNum], x2T[bNum], yT[bNum]
			numElem = len(x1b)
			predicted = []
			for idx, itm in enumerate(x1b):
				predicted.append(w1 * itm + w2 * x2b[idx] + b)
			
			# derivatives
			dw1, dw2, db = [], [], [] 
			for i in range(numElem):
				derr = 2 * (predicted[i] - yb[i]) 
				db.append(derr)
				dw1.append(derr * x1b[i])
				dw2.append(derr * x2b[i])
			b -= eta * sum(db) / numElem
			w1 -= eta * sum(dw1) / numElem
			w2 -= eta * sum(dw2) / numElem
	return b, w1, w2

'''
Algorithm 3: Neural Network (basic)
Input(s): list of x, list of y, # data, # features, # outputs, activation version, epoch
Output(s): w1, w2, bias1 and bias2 
Note: This method uses numpy matrices to solve (reduces computational time)
		"act" stands for activation function. 0 is sigmoid and 1 is tanh. 
'''
def basicNeuralNetwork(x, y, numData, numFeature, numOutput, act, epoch):
	def activation(x, version):
		def sig(x):
			return 1 / (1 + np.exp(-x))
		def tanh(x):
			return 2 * sig(2 * x) - 1

		if version == 0: #sigmoid
			return sig(x)
		else: #tanh
			return tanh(x) 

	def activation_der(x, version):
		def sig_der(x):
			sig = 1 / (1 + np.exp(-x))
			return sig * (1 - sig)
		def tanh_der(x):
			sig = 1 / (1 + np.exp(-2 * x))
			h = 2 * sig - 1
			return 1 - h ** 2

		if version == 0: #sigmoid
			return sig_der(x)
		else: #tanh
			return tanh_der(x)

	eta = 0.001
	numHidden = int(np.floor((numFeature * numOutput) ** 0.5) + 1)
	weight1 = np.random.rand(numHidden, numFeature)
	weight2 = np.random.rand(numOutput, numHidden)
	bias1 = np.random.rand(numHidden, 1)
	bias2 = np.random.rand(numOutput, 1)
	for _ in range(epoch):
		for idx, d in enumerate(x):
			d = d.reshape((len(d), 1))
			h = np.matmul(weight1, d) + bias1
			hAct = activation(h, act)

			o = np.matmul(weight2, hAct) + bias2
			oAct = activation(o, act)
			err = np.linalg.norm(oAct - y[idx]) / 2 #divide by 2 to make derivative simpler

			#Derivatives
			derr_do = oAct - y[idx]
			do_dx = activation_der(o, act)
			r = np.multiply(derr_do, do_dx) #result
			bias2 -= eta * r
			r_M = r * np.transpose(hAct)
			weight2 -= eta * r_M
			r2 = np.multiply(np.matmul(np.transpose(weight2),r), activation_der(h, act))
			bias1 -= eta * r2
			r2_M = r2 * np.transpose(d)
			weight1 -= eta * r2_M
	return weight1, weight2, bias1, bias2

#######################################################
### TESTS
#######################################################
from scipy import stats # only used in test
def basicLinearRegressionTest():
	def withinTolerance(a, b, tolerance):
		if a > b - tolerance and a < b + tolerance:
			return True
		return True

	tol = 10 ** -3
	x, y = [1, 2, 3, 4, 5], [2, 3, 5, 6, 7]
	num = len(x)
	m, b = basicLinearRegression(x, y, num)
	slope, intercept, r, p, e = stats.linregress(x, y)
	assert withinTolerance(m, slope, tol) == True
	assert withinTolerance(b, intercept, tol) == True

def basicMultiRegressionTest():
	x1 = [4, 2, 1, 3, 1, 6]
	x2 = [1, 8, 0, 2, 4, 7]
	y  = [2, -14, 1, -1, -7, -8]
	num = len(x1)
	b, w1, w2 = basicMultiRegression(x1, x2, y, num)
	print("Final values", b, w1, w2)

def basicNeuralNetworkTest():
	numData = 5
	numFeature = 3
	y = []
	x = np.random.rand(numData, numFeature)
	for _ in range(numData):
		y.append(random.sample([-1, 1], 1)[0])
	numOutput = 2
	basicNeuralNetwork(x, y, numData, numFeature, numOutput, 2, 1)

def mainTest():
	basicLinearRegressionTest()
	basicMultiRegressionTest()
	basicNeuralNetworkTest()

mainTest()