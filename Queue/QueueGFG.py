class Queue:
    def __init__(self):
        self.queue = []
        
    def enqueue(self, item):
        self.queue.append(item)
        
    def dequeue(self):
        if self.isEmpty == True:
            return None
        else:
            self.queue.pop(0)
        
    def isEmpty(self):
        return len(self.queue) == 0
    
    def size(self):
        return len(self.queue)
    
    def peek(self):
        if self.isEmpty:
            return None
        else:
            return self.queue[0]
        
    def Q_print(self):
        if self.isEmpty():
            print("Queue empty")
            return
        else:
            print(self.queue)
            
    
Q = Queue()

Q.enqueue(23)
Q.enqueue(11)
Q.enqueue(34)
Q.enqueue(99)
Q.enqueue(73)
Q.enqueue(69)

Q.Q_print()

Q.dequeue()
Q.dequeue()
 
Q.Q_print()