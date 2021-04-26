import array as a
import sys
# Implementation of Stack using Arrays
class Stack:

    def __init__(self, maxlen):
        self.maxlen = maxlen
        self.arr = a.array('i', [0] * maxlen)
        self.top = -1
        self.size = 0

    def isEmpty(self):
        return self.size == 0

    # Insertion happens on top
    def push(self, data):
        if self.size == self.maxlen:
            print("Stack Overflow")
        else:
            self.top += 1
            self.arr[self.top] = data
            self.size += 1

    # Deletion happens from top
    def pop(self):
        if self.size == 0:
            print("Stack Underflow")
        else:
            print(self.arr[self.top], " has been deleted")
            self.arr[self.top] = 0
            self.top -= 1
            self.size -= 1

    def peek(self):
        if self.size == 0:
            print("Stack Empty")
        else:
            print(self.arr[self.top])

    def stackSize(self):
        print(self.size)


# Implementation of Queue using Arrays
class Queue:

    def __init__(self, maxlen):
        self.maxlen = maxlen
        self.arr = a.array('i', [0] * maxlen)
        self.front = 0
        self.rear = maxlen - 1
        self.size = 0
        
    def isEmpty(self):
        return self.size == 0

    # Enqueue Operation: Insertion takes place at Rear End
    def enqueue(self, data):
        if self.size != self.maxlen:
            self.rear = (self.rear + 1) % self.maxlen
            self.arr[self.rear] = data
            self.size += 1
        else:
            print("Queue Overflow")

    # Dequeue Operation: Deletion takes place at Front End
    def dequeue(self):
        if self.size != 0:
            self.arr[self.front] = 0
            self.front = (self.front + 1) % self.maxlen
            self.size -= 1
        else:
            print("Queue Underflow")

    def displayFront(self):
        print(self.arr[self.front])

    def displayRear(self):
        print(self.arr[self.rear])

    def queueSize(self):
        print(self.size)

# Circular Queue
# Double Ended Queue

