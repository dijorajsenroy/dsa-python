"""
1. Palindrome Check Using Recursion:
There are two methods - Reversing a string and comparing with the original. And recursively checking for
corner elements in reducing substring till substring ceases to exist(n == 1 or n == 0), Although in Python this
can be done very simply, using: s == s[::-1] string manipulation and slicing.

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
"""
