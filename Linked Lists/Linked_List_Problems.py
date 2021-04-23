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

Refer to the animation given in the folder. Rev_LL.gif
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
2. Traverse and Search in linked lists (recursively):
"""
def searchList(current, key):
    # base case, current reaches null if value not found
    if current.data == key:
        return 1
    elif current is None:
        return -1
    else:
        return searchList(current.next, key)

def reverseTraversalDLL(last):
    # last should refer to tail node
    if last is None:
        return 
    print(last.data)
    return reverseTraversalDLL(last.prev)

"""
3. Detect and remove loops in a Linked List:

This problem is going to be solved using Floyd's Cycle Detection Algorithm. We can also use a hash set to keep
track of seen datapoints and return True, when a loop is found (element is seen twice) else it is added to set.
In Floyd's cycle detection - we traverse a linked list using two pointers. We move one pointer one step, the
other by two steps. If these pointers meet at the same node then there is a loop. If pointers do not meet 
then linked list doesn’t have a loop. Floyd's Algorithm is also known as Tortoise and Hare algorithm. Refer to
the Floyds_Cycle.gif file in the folder for the animation. 

The steps in Floyd's Cycle Finding Algorithm:
t - tortoise (slow moving), h - hare (fast moving)
(i) Run a loop and check whether t, h or h.next is null. If it is null then there is no loop, as a linked list
with a loop will never point to null, it always points to one of its nodes. 
(ii) When there is no cycle, h is the first one to reach null as it moves two steps. However when there is a cycle
there is a point where t and h meet at the same node, when that happens we know a cycle exists and return True.
"""
def loopDetectionHashing(head):
    # linear time, linear space
    seen = set()
    curr = head
    while curr is not None:
        if curr.data in seen:
            return True
        else:
            seen.add(curr.data)
            curr = curr.next
    return False

def loopFloydDetection(head):
    # linear time, constant space
    t = head # tortoise
    h = head # hare 
    # checking if they are null every iteration
    while t and h and h.next:
        t = t.next  # tortoise moves one step
        h = h.next.next  # hare moves two steps
        if t is h:
            # meeting point - cycle found
            return True
    return False

"""
Removal of loops - This is based on Floyd's Cycle Finding Algorithm, which we use to determine the first
meeting point of the two pointers. The algorithm states that the second meeting point of the pointers will
be the first node of the cycle if the following steps are followed:
(i) Use Floyd's Algo to find the first meeting point of the slow and fast pointers. 
(ii) Set the slow pointer to the head node, and move them both at a pace of one node each till they coincide.
(iii) The point at the two pointers collide is the first node of the cycle, if we maintain a prev pointer to 
the fast pointer or compare the next of the two pointers till collision, we see that the fast pointer is the
last node of the linked list and points to the first node of the cycle. Thus we need to de-link the past pointer.
"""
def detectAndRemove(head):
    fast = head; slow = head
    found = False # flag variable for detection of loop
    # Use Floyd's to find the first meeting point.
    while slow and fast and fast.next:
        slow = slow.next # move one pace
        fast = fast.next.next # move two paces
        if fast is slow:
            found = True
            break
    # loop detected
    if found:
        slow = head # reset slow pointer to head
        # terminate loop when slow.next and fast.next meet at start of cycle
        while slow.next is not fast.next:
            # traverse till they meet 
            slow = slow.next
            fast = fast.next
        # fast is the tail, de-link it from the cycle's starting node
        fast.next = None
    else:
        print("No Cycle Detected")

"""
4. Merge Sort for Linked Lists:

I. Function to obtain middle node: 
We use a variation of the tortoise and hare algorithm to obtain mid. fast pointer traverses the list two paces 
at a time till it reaches the last or second last node. Mean while for every two paces of the fast pointer,
the slow pointer traverses one pace. Hence at terminating condition, when fast pointer reaches the end of the 
list the slow pointer reaches the middle position which is then returned. This takes O(n) time and O(1) space. 
"""
def getMid(head):
    if head is None:
        return head
    # use tortoise and hare method to find mid
    slow = head; fast = head
    while(fast.next.next != None and fast.next != None):
        slow = slow.next
        fast = fast.next.next
    return slow
    
"""
II. Function to merge sorted halves: 
The steps involved in algorithm to merge two sorted halves into one list is,
(i) Initialize result list as empty: head = NULL. Let left and right be the heads of first and second lists. 
(ii) Create a function to reverse a linked list, reverse left and right lists. 
(iii) While (a != NULL and b != NULL)
    a) Use pointers to traverse the 2 lists. Find the larger of the two pointers.
    b) Insert the larger value of node at the front of result list.
    c) Move ahead in the list of larger node. 
(iv) If right becomes NULL before left, insert all nodes of left into result list at the beginning.
(v)) If left becomes NULL before right, insert all nodes of right into result list at the beginning. 
"""
def mergeSortedHalves(left, right):
    # reverse the lists left and right
    left = reverse(left)
    right = reverse(right)
    head = None

    # inserting the larger nodes of left and right into result
    while left != None and right != None:
        # compare the two pointers
        if left.data >= right.data:
            temp = left.next # store the next node
            left.next = head # add larger node to result list
            left = temp # move ahead in larger list
        else:
            temp = right.next  # store the next node
            right.next = head  # add larger node to result list
            right = temp  # move ahead in larger list

    # if right is not null - insert remaining nodes 
    while right is not None:
        temp = right.next # storing next node temporarily
        right.next = head # inserting next node in result list
        head = right # making inserted node the new head
        right = temp # traverse right to next node

    # if left is not null - insert remaining nodes
    while left is not None:
        temp = left.next  # storing next node temporarily
        left.next = head  # inserting next node in result list
        head = left  # making inserted node the new head
        left = temp  # traverse left to next node
    return head
"""        
III. Merge Sort Function:
The merge sort algorithm for linked lists is described below in the following steps:
(i) If head is null, return because there is only one element in the linked list.
(ii) Make a function to obtain mid for linked lists. Use it to obtain mid and divide the linked list in 2 halves.
(iii) Recursively apply the merge sort function on the two halves. 
(iv) Make a function to sort merged halves and update the head pointer to first node.
"""
def mergeSort(head):
    # check if list is empty or has one node
    if head is None or head.next is None:
        return head
    else:
        # use function to obtain mid
        mid = getMid(head)
        # we break the list at mid
        secondhalf = mid.next
        mid.next = None
        # recursively sort the two halves
        left = mergeSort(head) # left half: head to mid
        right = mergeSort(secondhalf) # right half: mid.next to tail
        # use function to merge sorted halves
        return mergeSortedHalves(left, right)

"""
5. LRU Cache Design Problem:
"""
"""
6. Find Intersection point of two Linked Lists:
"""
"""
7. Removes Duplicates from a sorted Linked List:
"""
"""
8. Palindrome Linked Lists:
"""
