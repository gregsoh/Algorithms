'''
This code implements beyesian linear regression (just a simple toy example). 
'''
import numpy as np
np.random.seed(1)

# Fn 1: Generating data (this is not predicted by model)
#       Assume y = b_0 + b_1x + e (where e is normal distributed with mean 0, variance 0.1)
# Input(s): b_0 (intercept), b_1 (slope) and some random error term
# Output(s): true y values
def generateData(b_0, b_1, x):
	mu, sigma = 0, 0.1
	return b_0 + b_1 * x + np.random.normal(mu, sigma, len(x))

# Mainfn: Main fn
# Input(s): N.A.
# Output(s): Graphs
def mainFn():
	# Generating data
	b_0, b_1 = -0.2, 1.5
	x = np.random.uniform(-2, 2, 300)
	y = generateData(b_0, b_1, x)

