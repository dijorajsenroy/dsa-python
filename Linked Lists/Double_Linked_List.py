"""
Implementation of a Double Linked List Node:
"""
class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

"""
Traversal in both directions:
"""
def display(head):
    curr = head
    print("Forward traversal")
    while(curr is not None):
        print(curr.data)
        last = curr
        curr = curr.next
    print("Reverse traversal")
    while(last is not None):
        print(last.data)
        last = last.prev


"""
INSERTION OF DOUBLE LINKED LISTS NODES:-

I. Insert at starting postion: It's the same as single linked list, we check if the list is empty, in which case
the inserted node becomes the only node and is directly made head. If the list is not empty, the node has to be
linked to the head node, meaning that new.next needs to point to head, and head.prev needs to point to new. new
becomes the new head as it has been inserted at the start of the list. Theta(1) Time complexity, same as SLL.
"""
def insertAtStart(head, data):
    new = Node(data)
    # check if list not empty
    if head is not None:
        new.next = head
        head.prev = new
        new.prev = None
        head = new
    else:
        head = new
    return head


"""
II. Insertion at end position: Same as single linked lists, except the prev of the new node has to be assigned
to the last node as well as the next of the last node has to be assigned to the new node. One advantage is that
we dont have to keep track of previous node as it can be accessed using the prev field of every node. This takes
Theta(size of list) time complexity which is the same as singly linked lists.
"""
def insertAtEnd(head, data):
    new = Node(data)
    curr = head
    while curr.next is not None:
        curr = curr.next
    # insert at end
    curr.next = new
    new.prev = curr
    new.next = None
    return head

# This can be done in O(1) time if the tail pointer is maintained as well.
def insertAtEndt(head, tail, data):
    new = Node(data)
    tail.next = new
    new.prev = tail
    new.next = None
    tail = new
    return head, tail


"""
III. Insertion before a given node's reference: This operation can be carried out easily by using prev field
of reference. We check if the given node is the head node separately as in that case the node before it is null.
If it is head, then the new node is made the head node. If it is not then the new node is inserted between
given.prev and given. This is done by linking before.next to new and new.prev to before, similarly, we need to
link new.next to given and given.prev to new. In Double linked list this takes constant time however, in SLL
We would need to traverse the list till the given node had been reached. 
"""

def insertBefore(head, given, data):
    # check if given is head
    new = Node(data)
    if given is head:
        new.next = head
        head.prev = new
        new.prev = None
        head = new
    else:
        # insert between nodes before and given
        before = given.prev
        before.next = new
        new.prev = before
        new.next = given
        given.prev = new
    return head

"""
DELETION OF DOUBLE LINKED LIST NODES:-

I. Deletion at start: The algorithm is the same as SLLs, first we have to check if the list is not empty, which
is true only if head is null. We need to de-link head from the rest of the node by setting head.next to null and
head.next.prev to null as well. this breaks the link between head and head.next. head.next is the new head. This
takes the same time complexity Theta(1) as single linked list deletion at start.
"""
def deleteAtStart(head):
    if head is not None:
        curr = head.next
        # head may be the last node
        if curr is not None:
            curr.prev = None
        head.next = None
        head = curr
    else:
        print("List is empty")
    return head

"""
II. Deletion at end: First we check if the list is empty if head is null. We also have to handle the edge case
where head is the only node in the list. Same as linked lists, this would take Theta(size of list) as there has
to be some traversal involved to get to the last node. We traverse the list till we reach the last node. If the 
node is not head then curr.prev should hold the previous node's value. We break the link between curr.prev and
curr nodes by making curr.prev.next point to null and curr.prev point to null.
"""
def deleteAtEnd(head):
    if head is not None:
        curr = head
        # traverse till curr is last node
        while(curr.next is not None):
            curr = curr.next
        # handle the case where head is last node
        if curr is head:
            head = None
        else:
            before = curr.prev
            curr.prev = None
            before.next = None
    else:
        print("List is empty")
    return head

# This can be done in O(1) time when we keep track of tail pointer before-hand
def deleteAtEndt(head, tail):
    # check if list empty
    if head is not None:
        # check if there is only one node
        if head is tail:
            head = None
            tail = None
        else:
            # delete tail using tail.prev
            before = tail.prev
            tail.prev = None
            before.next = None
            tail = before
    else:
        print("List is empty")
    return head, tail
"""
III. Deletion of a node (reference given): This problem can be done in constant time complexity in case of
double linked lists by accessing the previous fields of the given node. In single linked lists however, this 
would take Theta(position of node) time as we would have to traverse to the given node. First we check if the
list is empty(head is null), in which case there is an error message. If the given node for deletion is head,
then we deallocate it right away. Given these edge cases are handled, we store given.prev in a variable before
so that before and given can me mutually de-linked. This is done by setting given.prev to null, and before.next
to given.next so that given is bypassed and before is linked to the node after given.
"""
def deleteGiven(head, given):
    if head is not None:
        if head is given:
            head = None
        else:
            # before is the node before given
            before = given.prev
            # after is the node after given (can be null)
            after = given.next
            given.prev = None
            # before is linked to null if given was last node
            before.next = after
            # if after exists, it should be linked to before
            if after is not None:
                after.prev = before
    else:
        print("List is empty")
    return head
"""
Implement and Test the functions:
"""

head = Node(1)
head = insertAtStart(head, 0)
head = insertAtEnd(head, 2)
display(head)
given = head.next
head = insertBefore(head, given, -1)
display(head)
given = head.next
display(deleteGiven(head, given))

