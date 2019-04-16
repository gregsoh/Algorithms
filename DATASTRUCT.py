'''
This code implements common data structs.  
'''

# DataStruct 1: Queue
class myQueue:
	def __init__(self):
		self.queue = list()

	def enqueue(self, data):
		self.queue.append(data)

	def dequeue(self):
		self.queue.pop(0)

	def isEmpty(self): 
		return len(self.queue) == 0 

	def order(self): 
		return self.queue

# DataStruct 2: Stack
class myStack:
	def __init__(self):
		self.stack = list()

	def push(self, data):
		self.stack.append(data)

	def pop(self):
		self.stack.pop()

	def peek(self):
		self.stack[len(stack) - 1]

	def isEmpty(self): 
		return len(self.stack) == 0 

	def order(self): 
		return self.stack

#######################################################
### TESTS
#######################################################
def queueTest():
	q = myQueue()
	assert q.isEmpty() == True
	for itm in range(3):
		q.enqueue(itm + 1)
		q.enqueue(itm - 2)

	assert q.order() == [1, -2, 2, -1, 3, 0]
	for itm in range(2):
		q.dequeue()
	assert q.order() == [2, -1, 3, 0]

def stackTest():
	s = myStack()
	assert s.isEmpty() == True
	for itm in range(3):
		s.push(itm)
		s.push(2 * itm)
	assert s.order() == [0, 0, 1, 2, 2, 4]
	for itm in range(2):
		s.pop()
	assert s.order() == [0, 0, 1, 2]


def mainTest():
	queueTest()
	stackTest()

mainTest()