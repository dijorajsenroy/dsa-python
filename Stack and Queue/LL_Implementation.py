# Implementation of a Node
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Implementation of a Stack using Linked List

class Stack:
    # default constructor
    def __init__(self):
        # top node is initially null
        self.top = None
        self.size = 0
        self.head = None
    
    # Function to insert a Node at top of stack
    def push(self, data):
        new = Node(data) # create a new node
        if self.top is None:
            # set new node as top if stack is empty
            self.top = new
            self.head = new # set head as first node
        else:
            # insert new node after top node
            self.top.next = new
            # make inserted node new top node
            self.top = new
        print(self.top.data, "has been inserted")
        self.size += 1
    
    # Function to display top node
    def peek(self):
        if self.top is None:
            print("Stack Underflow")
        else:
            print(self.top.data)
    
    # Function to delete the top Node
    def pop(self):
        # Check for underflow
        if self.top is None:
            print("Stack Underflow")
        else:
            print(self.top.data, "has been deleted")
            if self.head is self.top:
                # there is only one node in the stack
                self.head = None
                self.top = None
            else:
                # traverse to the node before top node and de-link the two
                prev = self.head
                while prev.next is not self.top:
                    prev = prev.next
                # set previous node as the new top node
                self.top = prev
                prev.next = None
            self.size -= 1

    # Function to obtain the size of the stack
    def sizeStack(self):
        return self.size
    # Function to check if stack is empty
    def isEmpty(self):
        return self.size == 0

# Implementation of a Queue using Linked Lists

class Queue:
    # default constructor
    def __init__(self):
        self.front = None # front is the first node up for deletion
        self.rear = None # rear is the most recently entered node
        self.size = 0

    # Function to insert an element at rear end (enqueue operation)
    def enqueue(self, data):
        new  = Node(data) # node for insertion
        # case 1: new is the first node queued
        if self.size == 0:
            # initialising both pointers with new node
            self.rear = new
            self.front = new
        else:
            # case 2: insert new node before rear node
            new.next = self.rear
            # set rear as newly inserted node
            self.rear = new
        print(self.rear.data, "has been inserted")
        self.size += 1

    # Function to display the front node
    def peekFront(self):
        print(self.front.data if self.front is not None else "Queue Underlfow Error")

    # Function to display the rear node
    def peekRear(self):
        print(self.rear.data if self.rear is not None else "Queue Underlfow Error")

    # Function to remove a node at the Front end (Dequeue operation)
    def dequeue(self):
        # Check for underflow
        if self.size == 0:
            print("Queue Underlfow Error")
        else:
            print(self.front.data, "has been deleted")
            # case 1: Only one node in the queue (front is rear)
            if self.front is self.rear and self.size == 1:
                self.front = None
                self.rear = None
            else:
                # case 2: Traverse to the node before front and de-link it
                curr = self.rear
                while curr.next is not self.front:
                    curr = curr.next
                # set curr as the new front
                self.front = curr
                curr.next = None
            self.size -= 1