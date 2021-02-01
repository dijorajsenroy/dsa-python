"""
1. Check of Palindrome - Efficient Solution:

The normal solution is using O(n) extra space. To optimise this, we are iteratively comparing the first and last
characters and reducing the length of the string, if they are equal. For a palindrome number 0 or 1 letters, 
will be left in the string, for a non palindrome number we are using a break condition.
"""
def palindrome(s):
    count  = 0
    for i in range(len(s)):
        if s[i] == s[len(s)-i-1]:
            count += 1
    return count == len(s) or count == len(s) - 1

"""
2. Anagram problem:

We are given two strings, the goal is to check whether these two are anagrams (made of the same characters). The naive solution
can be to generate all permutations of a given string and compare with the given string. A less complicated solution can be to 
sort both strings and to check for equality. The sorted strings should be equal and sorting can be done in O(nlogn) time.
We can optimise both solutions for it to compare the two strings in just one iteration in O(n) time. For this purpose 
we have to use a count array, We use the characters as indices of this array and increment it and decrement it for s1 and s2 resp.
If the number is an anagram, for each index of count s1[i] the element is incremented and decremented and thus the net is 0. However
since character index is not supported in python like C++, we will use a dictionary to keep the count.

"""
def anagramNaive(s1, s2): 
    return sorted(s1) == sorted(s2) if len(s1) == len(s2) else False

def anagram(s1, s2):
    # checking equal length
    if len(s1) == len(s2):
        u1 = set(s1); u2 = set(s2)
        # checking same set of characters
        if u1 == u2:
            del u2
            # checking same frequency of characters
            d = dict(zip(u1, [0]*len(u1)))
            for i in range(len(s1)):
                d[s1[i]] += 1
                d[s2[i]] -= 1
            # checking if all counts are 0 in d
            return all([d[i] == 0 for i in d])
        else:
            return False
    else:
        return False
"""
3. Left-most repeating character in a string:

In a given string we have to compute the character that is repeating in nature and its first occurrence is left-most. The naive O(n*n)
solution is to compute if the ith element exists in the i+1 to n substring. A better method is to use the count array approach. 
We make a dictionary of the elements, without set because set is unordered and we need to perserve the order.
"""
def leftMostRepeatingCharNaive(s):
    for i in range(len(s)):
        if s[i] in s[i+1:]:
            return i
    return -1

def leftMostRepeatingChar(s):
    d = dict.fromkeys(s)
    d = dict(zip(d.keys(), [0]*len(d)))
    if len(d) == len(s):
        # Worst case - all distinct elements
        return -1
    else:
        for i in d:
            if s.count(i) > 1: # O(n)
                return s.index(i)

"""
3. Left-Most non repeating element:

"""
def leftMostNonRepeatingChar(s):
    d = dict.fromkeys(s)
    d = dict(zip(d.keys(), [0]*len(d)))
    for i in d:
        if s.count(i) == 1:  # O(n)
            return s.index(i)
    return -1

"""
4. Reversing the words in a string:

In other languages like in C and Cpp we would have to create a Stack data structure and push the elements one by one, and
append the words to the output. To optimise this in Cpp we can use the algorithm to reverse each word, and then reverse the
entire string. But in Python its possible to do it in no extra space and O(n) time because of split and join functions.
"""
def reverseWords(s):
    # O(n) time complexity and O(1) auxillary space
    s = s.split(" ")[::-1]
    return " ".join(s)

"""
5. Check if Strings are rotations:
"""
"""
6. Anagram Search:
"""
"""
7. Lexicographic Rank of a string:
"""
"""
8. Longest Substring with Distinct Characters:
"""
