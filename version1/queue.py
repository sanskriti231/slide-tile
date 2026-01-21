class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, element):
        self.queue.append(element)

    def isEmpty(self):
        return len(self.queue) == 0
    
    def size(self): return len(self.queue)

    def dequeue(self):
        if not self.isEmpty():
            return self.queue.pop(0)
        return "Queue is empty"
    
    def peek(self):
        if self.isEmpty(): return "Queue is empty"
        return self.queue[0]