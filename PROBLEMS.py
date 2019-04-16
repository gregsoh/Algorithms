import random, numpy as np
import matplotlib.pyplot as plt


def calculate(n):
	price = [0 for i in range(n + 1)]
	strategy = [0 for i in range(n + 1)]
	numstock = 0 
	for i in range(1, n):
		v = random.randint(0, 1)
		if v == 0: #price increase
			price[i] = price[i - 1] + 1
			strategy[i] = -price[i]
			numstock += 1
		else:
			price[i] = price[i - 1] - 1
			strategy[i] = price[i]
			numstock -= 1
	v = random.randint(0, 1)
	t = 0
	if v == 0: #price increase
		t = price[n - 1] + 1
	else:
		t = price[n - 1] - 1
	
	price[n] = t
	strategy[n] = numstock * t
	return sum(strategy)


def total():
	v1, v2, v3, v4, v5, v6 = [], [], [], [], [], []
	for _ in range(100000):
		v1.append(calculate(4))
		v2.append(calculate(5))
		v3.append(calculate(6))
		v4.append(calculate(7))
		v5.append(calculate(8))
		v6.append(calculate(100))
	print(np.mean(v1), np.mean(v2), np.mean(v3), np.mean(v4), np.mean(v5), np.mean(v6))
	print(np.min(v1), np.min(v2), np.min(v3), np.min(v4), np.min(v5), np.min(v6))
	plt.hist(v6, bins = 100)
	plt.show()
total()
