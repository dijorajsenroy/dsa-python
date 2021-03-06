"""
1. Palindrome Check Using Recursion:

There are two methods - Reversing a string and comparing with the original. And recursively checking for
corner elements in reducing substring till substring ceases to exist(n == 1 or n == 0), Although in Python this
can be done very simply, using: s == s[::-1], pythonic string manipulation and slicing.
As base case we are checking if the two variables signifying start and end of string have met in the center.
If they have not we are taking boolean and of the corner character's equality and the next set of call chars.
Time complexity is Theta(n), the same as pythonic slicing method, rather the slicing method has less auxillary
space compared to N recursion call stack memory.
"""
def palindrome(s, start, end):
    if start >= end:
        return True
    else:
        return (s[start] == s[end]) and palindrome(s, start+1, end-1)

"""
2. Rope Cutting Problem:

A rope of n length has to be cut in pieces of lengths in the set {a,b,c}. Write a function that returns the 
maximum number of cuts that can be made or -1 if the rope cannot be cut into the given lengths. From the 
recursion tree we have that base cases are for negative lengths, and valid case is 0 length, which means
the rope has been cut successfully. We already know if rope cannot be cut function returns -1, which corresponds
to the base-case where all leaves are negative. For each cut we are computing the max of three cuts, which is -1 
if all cuts are invalid or 0 if one of the cut is valid since max(0,-1)=0. We thus return -1 if the max is -1 and
increment the value if its 0, so we get the number of cuts. The previous level, the max is computed and 1 is the max,
and again it is incremented till the result is obtained at the head of the call. We have started at res=0 at the level
where the valid number of cuts is found and incremented on our way up.
"""

def rope(n,a,b,c):
    if n < 0:
        return -1
    elif n == 0:
        return 0
    else:
        res = max(rope(n-a,a,b,c),rope(n-b,a,b,c),rope(n-c,a,b,c))
        return -1 if res == -1 else res + 1

"""
3. Generating Subsets Using Recursion:

For a string "ABC" the subsets are "", "A", "B", "C", "AB"...."ABC". We make a recursion tree starting from an empty literal,
and at each level we make a recursion call to add one of these letters. When an index variable increments and reaches the length
of the string (at three levels of recursion), we obtain the leaf nodes as the answer.
"""
res = [] # global variable
def genSub(s, curr="", index=0):
    if index == len(s):
        res.append(curr)
        return
    else:
        genSub(s, curr = curr, index = index+1)
        genSub(s, curr = curr + s[index], index = index+1)

"""
4. Printing Permutations Using Recursion:

We use recursion to increment an index variable i to denote the position of the character being swapped. i=0 swaps the 0th character with 
characters j=0,1,2. Hence we also require a loop to decide which character will be used for swapping. In the next recursive call, when i 
is incremented by 1, i=1, we swap the 1st character with characters j=1,2 and the two strings obtained are the answers. Thus we need to print
them when i reaches length len(s)-1. The loop for j runs from i to len(s)-1. The time complexity of this solution is O(n^2), which is the 
same as the iterative solution and also utilises theta(n) auxillary space for the recursive call stack. Thus its not an optimisable solution.
"""
def swap(s,i,j):
    s = list(s)
    s[i],s[j] = (s[j],s[i])
    s = "".join(s)
    return s 

def permute(s, i=0):
    if i == len(s)-1:
        print(s)
        return
    else:
        for j in range(i, len(s)):
            permute(s=swap(s, i, j), i = i+1)
            
"""
5. Binary to Gray Code Problem using Recursion:

Gray code is a variation of binary code in which the difference between two consecutive bits is always 1. This propert makes it useful for K-maps,
and many other applications. For example, the n-bit gray codes are given below for some values of n. n = 2:
00 01 11 10
n = 3: 000 001 011 010 110 111 101 100 and so forth.
We have a given binary number and we are required to convert it to gray code. We consider the last two bits of the number and compare them, 
if they are same we have to convert or else we retain the numbers. for a number n, we follow the steps:
(i) base-case is at n==0, where we return 0 to previous call.
(ii) If last two digits are same, ie either 11 or 00 we divide by 10 and pass to the next call, whose result is multiplied by 10. thus 11 becomes
10 and 100 becomes 10. Ensuring that bits are opposite.
(iii) If last two digits are opposite we add 1 to its recursive call to make sure it stays inverted.
"""

def binary_to_gray( n ): 
    if not(n): 
        return 0
    # Taking last digit     
    a = n % 10
     # Taking second last digit 
    b = int(n / 10) % 10
    # If last digit are opposite bits 
    if (a and not(b)) or (not(a) and b): 
        return (1 + 10 * binary_to_gray(int(n / 10))) 
    # If last two bits are same 
    return (10 * binary_to_gray(int(n / 10)))
