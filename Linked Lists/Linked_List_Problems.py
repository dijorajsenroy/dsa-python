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

def reverseTraversal(last):
    # last should refer to tail node
    if last is None:
        return 
    print(last.data)
    return reverseTraversal(last.prev)

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
4. Find Intersection point of two Linked Lists:
"""
"""
5. Removes Duplicates from a sorted Linked List:
"""
"""
6. Merge Sort for Linked Lists:
"""
"""
7. Palindrome Linked Lists:
"""
"""
8. LRU Cache Design Problem:
"""
