"""
Implementation of Circular Linked List :-

A Circular Singly Linked List is when the last node is point the first node and there is no node pointing null.
To traverse a cicular linked list we keep track of the starting point and terminate loop when it is encountered
twice. There is no start or end of a circular linked list. 
"""

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class CircularLinkedList:
    def __init__(self):
        self.tail = None

    # Function to add a new element to the linked list
    def push(self, data):
        new = Node(data)
        # when there are no elements in the list
        if self.tail is None:
            new.next = new
            self.tail = new
        else:
            # condition for only one node in the list
            if self.tail.next is self.tail:
                self.tail.next = new
                new.next = self.tail
                self.tail = new
            else:
            # adding new node between tail and tail.next
                before = self.tail
                after = before.next
                before.next = new
                new.next = after
                self.tail = new

    # Function to displat the elements of the linked list
    def display(self):
        # condition for empty list
        if self.tail is None:
            print("List is empty")
        else:
            # loop terminates when tail is encountered twice
            curr = self.tail
            while(True):
                curr = curr.next
                print(curr.data)
                if curr is self.tail:
                    break
            
    # Function to delete a specified element in the linked list
    def pop(self, key):
        # checking if list is empty
        if self.tail is None:
            print("List is empty")
        else:
            found = False # flag variable
            curr = self.tail 
            while(True):
                # traversing till tail comes back
                prev = curr
                curr = curr.next
                if curr.data == key:
                    found = True
                    break
                if curr is self.tail:
                    break
            # if key is found then node is deleted
            if found:
                # only a single node is present (edge case)
                if curr is prev:
                    del curr, prev
                    self.tail = None
                # if key is found at tail element (tail has to be changed)
                elif curr is self.tail:
                    prev.next = curr.next
                    curr.next = None
                    self.tail = prev
                else:
                # key is anywhere else but tail (tail can remain same)
                    prev.next = curr.next
                    curr.next = None
                print("{0} was deleted".format(key))
            else:
                print("{0} was not found".format(key))
                
l = CircularLinkedList()
l.push(0)
l.push(1)
l.push(2)
l.push(3)
l.pop(0)
l.display()
