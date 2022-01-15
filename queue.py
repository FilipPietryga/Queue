class Queue:
    def __init__(self, initial):
        self.queue = initial
    
    def enqueue(self, elem):
        self.queue.append(elem)
        return self.queue
    
    def dequeue(self):
        return self.queue.pop(0)

    def checkQueue(self):
        print(self.queue)

    def checkHead(self):
        print(self.queue[0])

    def checkTail(self):
        print(self.queue[-1])