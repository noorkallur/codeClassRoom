class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

# here Cicrcular queue is implemented using a list    
# look at the circular-queue.png if you dont undestand it
# https://www.geeksforgeeks.org/introduction-to-circular-queue/ 
class CustomCircularQueue:
    def __init__(self, maxSize):
        self.front = -1
        self.rear = -1
        self.queue = [None] * maxSize
    
    def isQfull(self):
        """check if the next of REAR is FRONT that means its full
        """
        print(f"front: {self.front} rear: {self.rear}")
        return (self.rear + 1)%len(self.queue) == self.front

    def isEmpty(self):
        """if FRONT or REAR is -1 then its empty
        """
        return self.front == -1
        
    def enqueue(self, val):
        if self.isQfull():
            print(f"Q full")            
            return
        if self.isEmpty():
            self.front = 0
        
        self.rear = (self.rear + 1)%len(self.queue) # relative position(used to jump to index 0 when rear reaches end index)   
        self.queue[self.rear] = val

    def dequeue(self):
        if self.isEmpty():
            print(f"Q is empty")
            return
        self.queue[self.front] = None
        if self.front == self.rear:
            self.front = self.rear = -1 # make sure to reset the front and back
            return
        self.front = (self.front+1)%len(self.queue)
        

    

    
q = CustomCircularQueue(5)

q.enqueue(1)    
q.enqueue(2)    
q.enqueue(3)
q.enqueue(4)
q.enqueue(5)
q.enqueue(6)
q.dequeue()
q.dequeue()
q.dequeue()
q.dequeue()
q.dequeue()
q.enqueue(4)
q.enqueue(5)
q.enqueue(6)
q.enqueue(1)    
q.enqueue(2) 
print(q.queue)
    