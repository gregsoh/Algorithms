import random, numpy as np
import matplotlib.pyplot as plt

'''
Assume you start with 0 stocks and stock price is $0. The stock price either increases by $1 or decreases by $1 each day. 
You implement 1-lag algorithm. If stock price decrease, you sell and if stock price increase, you buy. 
What is the distribution and what is the expected returns. 
'''
def mainFn(n):
	price = [0 for i in range(n + 1)]
	strategy = [0 for i in range(n + 1)]
	numstock = 0 
	for i in range(1, n + 1):
		v = random.randint(0, 1)
		if v == 0: #price increase
			price[i] = price[i - 1] + 1
			strategy[i] = -price[i]
			numstock += 1
		else: #price decrease
			price[i] = price[i - 1] - 1
			strategy[i] = price[i]
			numstock -= 1
	value = price[n] * numstock
	return value + sum(strategy) 

def simulate():
	r = []
	epoch = 10000
	for _ in range(epoch): 
		r.append(mainFn(100))
	print(np.mean(r), np.min(r))
	plt.hist(r, bins = 100)
	plt.show()
	
simulate()
