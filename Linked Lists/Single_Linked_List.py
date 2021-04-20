"""
Implementation of a Single Linked List Node :- 
contains attributes data and reference to next Node, initially null
"""
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

"""
Function to print all the nodes: Traverse a current pointer till it is not null. The loop is terminated 
when the value of current is null, or after the last node has been printed. To traverse the linked list,
set the current to the next node by using the next refernece field.
"""
def display(head):
    curr = head
    while(curr is not None):
        print(curr.data)
        curr = curr.next

"""
INSERTION IN LINKED LISTS:

I.Function to insert a value at the start: First we check if the linked list is empty, if it is empty, head
node (the first node) should be Null as it has not been assigned yet. In that case the new node should be
the head node. However if head is not null, we need to make the new node point to the head node, and set 
the new node as the head node by storing the new node's reference in head. 
"""
def insertAtStart(head, data):
    new = Node(data)
    if head is None:
        head = new
    else:
        new.next = head
        head = new
    return head

"""
II. Function to insert a value at the end: To insert a value after the last node, we traverse to the end of the
list such that the current variable stores the reference of the last node, meaning we would terminate the loop
when current.next is null. As current refers to the last node, we make it point to the new node and make the
new node point to null. 
"""
def insertAtEnd(head, data):
    curr = head
    new = Node(data)
    # executes for all nodes except last node 
    while(curr.next is not None):
        curr = curr.next
    # curr stores the reference of the last Node
    curr.next = new
    new.next = None
    return head


"""
III. Function to insert at any given position: There are three cases to be handled here,
(i) pos is 0: meaning we insert at start of the linked list
(ii) pos is between 1 and listSize: meaning we insert at the given position
(iii) pos is listSize: meaning we insert at end.

Case (i) can be handled separately in constant time, which is the most efficient way of doing it. For Case (ii)
We are required to create a variable that would count index of the nodes till position of insertion is reached.
With every iteration as we traverse to the next node this count is incremented till it reaches the required pos.
Thus when count == pos we terminate the loop. It may happen that pos doesn't exist in the list (pos > listSize),
In that case we should also terminate the loop when Null is reached, count would stop incrementing and not reach
pos in such a case. While traversing the loop we keep track of the previous node (pos-1th) node as well, as
the insertion has to take place between the pos - 1th and pos th nodes. We make the insertion only when count
reaches pos (count == pos), or else the position doesn't exist. After handling these edge cases, we insert
at pos by setting the (pos - 1th) prev.next to the new node and new.next to the (pos th)current node.
"""
def insertAtPos(head, pos, data):
    curr = head
    count = 0
    new = Node(data)
    if pos == 0:
        # handles insertion at start
        return insertAtStart(head, data)
    else:
        # executes till prev is pos - 1th node
        while curr is not None and count < pos:
            prev = curr
            curr = curr.next
            count += 1
        # if count != pos then pos doesnt exist
        if count == pos:
            prev.next = new
            new.next = curr
        else:
            print("Position doesn't exist")
        return head

"""
DELETION IN LINKED LISTS:

I. Function to delete at start: We need to deallocate the head node by breaking its link to the rest of the linked list and making it
point to null. The node after the head node should become the new head. If head was the only node in the list, then after deletion head
should be null, If the linked list was empty there should be an error message. In python, del can be used to derefernce head directly.
This operation takes constant time complexity as there is no traversal required.
"""
def deleteAtStart(head):
    if head is not None:
        nextNode = head.next # None if there is no next node
        head.next = None # break link to the remaining list
        head = nextNode # None if head was only node
    else:
        print("List is empty")
    return head

"""
II. Function to delete at end: Check for underflow if head is null, meaning there are no nodes in the linked list. To delete the last node
of the linked list we have to traverse the linked list keeping track of the last node and the node before it. The node before the last node
can be linked to null to easily deallocate the last node and disconnet it from the list. This takes Theta(size of list) time complexity.
"""
def deleteAtEnd(head):
    if head is not None:
        curr = head
        # traverses till curr is the last node
        while curr.next is not None :
            prev = curr
            curr = curr.next
        # dereference the curr (last) node
        prev.next = None
    else:
        print("List is empty")
    return head

"""
III. Function to delete a user defined value: First we check for underflow so an error message is printed for deletion in empty lists.
Run a while loop to traverse all the nodes in the linked list till the node with key is found. There are the following cases that arise:
(i) Key is the first element in that case deletion at start is invoked (Edge case)
(ii) Key does not exist, in that case the traversal loop should execute till current node is null. Print a message.
(iii) Key exists in the middle of the linked list. We traverse the list and where current node holds the key we terminate loop. Hence
the node for deletion is the current node. To delete it we also keep track of the node previous to the current node. In case of current
not being None (key existing) we link the node after the current (curr.next) to the node before the current (prev). Hence prev.next 
should store the reference of curr.next. Then we remove the link between curr and curr.next. 
(iv) Key exists, but in last node (Edge case), In this case when key is found at curr, the loop terminates and curr holds the value of
the last node and not null. prev holds the value of the node before curr. However for the last node, curr.next is None and thus cannot
be referenced. Using the prev node method remedies this as prev.next is assigned null on deletion of curr.
"""
def deleteKey(head, key):
    if head is not None:
        if head.data == key:
            return deleteAtStart(head)
        else:
            curr = head
            # curr should be null if key not found
            while curr is not None:
                # termination if key is found
                if curr.data == key:
                    break
                else:
                    # keeping track of previous node
                    prev = curr
                    curr = curr.next
            if curr is None:
                print("Key was not found")
            else:
                prev.next = curr.next
                curr.next = None    
    else:
        print("List is empty")
    return head 


"""
Implement and Test All the functions
"""
# make linked list 0 1 2 3 using insertion
head = insertAtPos(insertAtEnd(insertAtStart(Node(1), 0), 2), 3, 3)
# display
display(head)
# delete first, start and key = 1
display(deleteKey(deleteAtStart(deleteAtEnd(head)), 1))


