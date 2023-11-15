import queue

class Stack:
    def __init__(self):
        self.queue1 = queue.Queue()
        self.queue2 = queue.Queue()

    def push(self, data):
        while not self.queue1.empty():
            self.queue2.put(self.queue1.get())
        self.queue1.put(data)
        
        while not self.queue2.empty():
            self.queue1.put(self.queue2.get())

    def pop(self):
        if self.queue1.empty():
            return None
        return self.queue1.get()

class Queue2:
    def __init__(self):
        self.in_stack = []
        self.out_stack = []
    
    def enqueue(self, element):
        self.in_stack.append(element)
    
    def dequeue(self):
        if len(self.out_stack)==0:
            while len(self.in_stack)>0:
                self.out_stack.append(self.in_stack.pop())
        return self.out_stack.pop()
    
    def is_empty(self):
        return len(self.in_stack)==0 and len(self.out_stack)==0

data= Queue2()
data.enqueue(1)
data.enqueue(2)
print(data.dequeue())
print(data.dequeue())
print(data.is_empty())