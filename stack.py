from collections import deque
#LIFO (last in First Out)
class stack:
    def __init__(self):
        self.stack=deque()
    def pop(self):
        return self.stack.pop()
    def push(self,val):
        self.stack.append(val)
    def peek(self):
        return self.stack[-1]
    def is_empty(self):
        return len(self.stack)==0
    def size(self):
        return len(self.stack)
#FIFO (First in First Out)
class Queue:
    def __init__(self):
        self.queue=deque()
    def dequeue(self):
        return self.queue.pop()
    def enqueue(self,val):
        self.queue.appendleft(val)
    def is_empty(self):
        return len(self.queue)==0
    def size(self):
        return len(self.queue)
stack=stack()
stack.push(5)
stack.push(9)
stack.push(3)
stack.push(4)
print(stack.pop())