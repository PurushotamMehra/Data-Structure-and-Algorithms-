from collections import deque

class Queue :
    def __init__(self):
        self.buffer = deque()
        
    def enqueue(self, val):
        self.buffer.appendleft(val)
        
    def dequeue(self):
        return self.buffer.pop()
    
    def isempty(self):
        return len(self.buffer) == 0
    
    def size(self):
        return len(self.buffer)
    
pq = Queue()

pq.enqueue({'Company' : 'DMart', 
            'time' : '15 apr, 11.02 AM', 
            'price' : 131.10})

pq.enqueue({'Company' : 'DMart', 
            'time' : '15 apr, 11.03 AM',    
            'price' : 132}) 

pq.enqueue({'Company' : 'DMart', 
            'time' : '15 apr, 11.04 AM',    
            'price' : 135}) 

pq.enqueue({'Company' : 'DMart', 
            'time' : '15 apr, 11.05 AM',    
            'price' : 139.80}) 
print(pq.buffer)
# print(pq.dequeue())

       