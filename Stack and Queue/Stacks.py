# Implementation of Stack using Lists

class Stack:

    def __init__(self, maxlen):
        self.maxlen = maxlen
        self.stack = []

    def isEmpty(self):
        return self.stack == []

    def push(self, data):
        if len(self.stack) < self.maxlen:
            self.stack.append(data)
        else:
            print("Overflow Error")

    def pop(self):
        if len(self.stack) == 0:
            print("Underflow Error")
            return -1
        else:
            data = self.stack[-1]
            del self.stack[-1]
            return data

    def peek(self):
        return self.stack[-1]

    def size(self):
        return len(self.stack)
