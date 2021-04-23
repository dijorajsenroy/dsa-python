# Queue using Lists Implementation

class Queue:
    
    def __init__(self, maxlen):
        self.queue = []
        self.maxlen = maxlen

    def isEmpty(self):
        return self.queue == []

    def push(self, data):
        if len(self.queue) < self.maxlen:
            self.queue.append(data)
        else:
            print("Overflow Error")

    def pop(self):
        if len(self.queue) == 0:
            print("Underflow Error")
            return
        else:
            data = self.queue[0]
            del self.queue[0]
            return data

    def peek(self):
        return self.queue[0]

    def sizeQueue(self):
        return len(self.queue)

# Circular Queue

# Double Ended Queue