class Queue:
    def __init__(self):
        self.queue = []

    def push(self, element):
        self.queue.append(element)

    def isEmpty(self):
        return len(self.queue) == 0
    
    def size(self): return len(self.queue)

    def pop(self):
        if not self.isEmpty():
            return self.queue.pop(0)
        return "Queue is empty"
    
    def front(self):
        if self.isEmpty(): return "Queue is empty"
        return self.queue[0]