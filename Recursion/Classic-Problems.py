"""
1. Josephus Problem:

We have n people in a circle and every iteration the kth person is killed. Give the survivors position. We calculate the kth person,
from the x+1th person is the xth person was killed last round, and we use only survivors for calculating. For n=7, k=3, we have,
0 1 x2x 3 4 5 6 ===> 0 1 3 4 x5x 6 ===> 0 x1x 3 4 6 ===> 0 3 4 x6x ===> 0 3 x4x ===> x0x 3 ===> 3 survivor
killed ==> 2,5,1,6,4,0
For n=4, k=2 we have,
0 x1x 2 3  ===> 0 2 x3x ===> 0 x2x ===> 0 survivor

To obtain a recursive solution we have to obtain a relationship between josephus(n, k) and josephus(n-1, k).
for n=5, k=3
josephus(5,3) --> 3
josephus(4,3) --> 0
josephus(3,3) --> 1
josephus(2,3) --> 1
josephus(1,3) --> 0

Thus we can take the base-case of the recursion to be 0 at n==1, which is also independent of the value of k. 
One method can be to construct these values for n=1 to 10 and k= 1 to 10 from the Bruteforce solution O(n^2).
From the above series we can derive a recursive pattern as :

josephus(n,k) = (josephus(n,k) + k) % n

We add + k as after every iteration, the postions are being shifted by k. The mod n operation ensures that the value
does not cross n, otherwise there may be an overflow error. The time complexity of this solution is Theta(n).
"""

def josephus(n, k):
    if n == 1:
        return 0
    else:
        return (josephus(n-1,k) + k) % n

    
"""
2. Sum of Subsets Problem:

For an array compute the number of subsets whose sum is equal to a given sum. To generate subsets of the array, let us 
consider 2 cases for every element: It is either included in the subset or excluded. At the head of the recursive tree,
There is the null set, and to every right child we add an element and every left child we keep unchanged. The leaves of
this tree would give the subsets of the array. We can take 2 approaches - either using an array or calculating sum using
just parameters. The array solution simply makes a recursive tree and adding elements to curr variable every right child.
sum is computed using pythonic function sum() and checked for base case when control is at last level.

For the parameterised solution, we have taken a different approach.

"""

# Solution using array - taking up more auxillary space
count = []
def subsets(arr, sumval, curr = [], index= 0):
    if index == len(arr):
        if sumval == sum(curr):
            count.append(True)
    else:
        # Right subtree
        subsets(arr = arr,
                sumval = sumval, 
                curr = curr, 
                index = index + 1)

        # Left subtree
        new_elem = arr[len(arr) - index - 1]
        subsets(arr = arr,
                sumval = sumval, 
                curr = curr + [new_elem], 
                index = index + 1)
        
#subsets([10, 20,15], 35)
#print(len(count))

# Solution using parameters to compute sum - lesser auxillary space.

def countSubsets(arr, index, sumval):
    if index == 0:
        return 1 if sumval == 0 else 0
    else:
        return (countSubsets(arr, index = index - 1, sumval = sumval)
                + countSubsets(arr, index = index - 1, sumval = sumval + arr[index-1]))

#array = [ int(i) for i in str(input()) if i != " "]
#sumval = int(input())
#countSubsets(arr = array,
            #index = len(array),
            #sumval = )


"""
3. Tower of Hanoi Problem:

There are three towers A, B, C. The tower A has n number of discs of increasing radius. 
The task is to print the number of moves taken to transport the n discs in the same order from tower A to tower C. 
The rule is that at a time only one disc can be transported and in any tower, a larger disc will not sit over 
a smaller disc. We break this problem into subproblems such that a recursive statement can cover some of the moves
of discs and we use that recursive statement again. To accomplish this we compare the moves for n discs and n-1 discs.
Then we aim to break the moves into repeated patterns that can be arranged in recursive form. 

For n=2 discs however we do the following:
------------------------
(i) move 1 from A to B
------------------------
(ii) move 2 from A to C
------------------------
(iii) move 1 from B to C
------------------------

Steps for n = 3 discs are:
------------------------
(i) move 1 from A to C
(ii) move 2 from A to B
(iii) move 1 from C to B        # source = A, auxillary = C, destination = B
------------------------
(iv) move 3 from A to C         # nth disc case
------------------------
(v) move 1 from B to A          # source = B, auxillary = A, destination = C
(vi) move 2 from B to C
(vii) move 1 from A to C
------------------------

Comparing n = 2 and n = 3, we see that the recursive solution has three sub-problems:
(i) move n-1 discs from A to B using C as an auxillary tower
(ii) move nth disc from A to C
(iii) move n-1 discs from B to C using A as an auxiallary tower

TOH(n) = TOH(n-1, move from A to B using C) + (move nth from A to C) + TOH(n-1, move from B to C using A)

For the purpose of recursion we will consider three towers: Source, Destination and Auxillary. For sub-problem (i), A is source,
B is Destination, C is Auxillary. the base-case of this recursion is for input 1, so that we may have a print statement for disc
number 1 at n == 1.
"""

def TOH(n, source = "A", auxillary = "B", destination = "C"):

    if n == 1:
        # case for moving disc number 1
        print("Move 1 from {0} to {1}".format(source, destination))
        return

    else:
        # case for moving n-1 top discs from source to auxillary tower
        TOH(n-1, source = source, auxillary = destination, destination = auxillary)
        
        # case for moving nth disc to destination tower
        print("Move {0} from {1} to {2}".format(n, source, destination))

        # case for moving n-1 top discs from auxillary to destination tower
        TOH(n-1, source = auxillary, auxillary = source, destination = destination)
