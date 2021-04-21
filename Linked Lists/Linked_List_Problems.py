"""
1. Reversal of Linked Lists:

To reverse a Linked List we create three pointers, prevN, currN, nextN. prevN and nextN is intiially null, and currN is set to head node.
A loop is used till curr reaches null (at which point) prevN is the previous node and last node. With every iteration of the loop the steps:
(i) The next node is stored temporarily in nextN so that it may used later, as curr node will be de-linked from it.
(ii) Set the current node's link to the previous node. Intially the current node (head) will be set to null (prev). This reverses the 
direction of the link as curr now points the other way. 
(iii) Set prev to the current node as the next node that will be reversed in next iteration should point to this.
(iv) Set current node to the next node. By doing this, we have reversed the link of the current node to make it point the node before it,
set up the prev node in a way that its reference is now the curr node, and curr and next both point to the node that should be reversed,
this is repeated till prev becomes the last node.
(v) When prev is the last node set it as the new head of the list. 

For Example:

(initially, nxt = cur.next)
None     [1]---->[2]---->[3]----> None
prv      cur     nxt
(cur.next = prv)
None<----[1]    [2]---->[3]----> None
(prev = cur; cur = nxt)
None<----[1]    [2]---->[3]----> None
         prv    cur,nxt

(second iteration, nxt = cur.next)
None<----[1]    [2]---->[3]----> None
         prv    cur     nxt
(cur.next = prv)
None<----[1]<----[2]    [3]----> None
(prev = cur; cur = nxt)
None<----[1]<----[2]    [3]----> None
                 prv    cur,nxt

(third iteration, nxt = cur.next)
None<----[1]<----[2]    [3]----> None
                 prv    cur      nxt
(cur.next = prv)
None<----[1]<----[2]<----[3]     None
                 prv     cur     nxt
(prev = cur; cur = nxt)
None<----[1]<----[2]<----[3](head)     None
                         prv           cur, nxt ---> terminating condition                  
"""

def reverse(head):
    prevN = None
    currN = head
    nextN = None
    while(currN is not None):
        # Iterates till current node is last node
        nextN = currN.next  # saving next node
        currN.next = prevN  # change link direction
        # traversing previous and current pointers
        prevN = currN
        currN = nextN
    head = prevN
    return head

"""
2. Detect loop in a linked list:
"""
"""
3. Find Intersection point of two linked lists:
"""
