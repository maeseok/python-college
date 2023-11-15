class ListQueue:
	def __init__(self):
		self.__queue = []

	def enqueue(self, x):
		self.__queue.insert(0,x)

	def dequeue(self):
		return self.__queue.pop()

	def front(self):
		if self.isEmpty():
			return None
		else:
			return self.__queue[-1]

	def isEmpty(self) -> bool:
		return (len(self.__queue) == 0);
 
	def dequeueAll(self):
		self.__queue.clear()

	def printQueue(self):
		print("Queue from front:", end = ' ')
		for i in range(len(self.__queue)-1, -1, -1):
			print(self.__queue[i], end = ' ')
		print()

# 코드 7-6