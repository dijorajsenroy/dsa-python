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

Check if a string s2 can be obtained from s1 by rotating it any number of times. The type of rotation can be left or right rotation.
The Naive solution is O(n*n) for searching and slicing in the loop. We can compute the concatenation of s1+s1 and thus we have
all the rotations in it. Searching s2 in s1+s2 would take O(n) time complexity.
"""
def checkRotNaive(s1, s2):
    leftrot = s1; rightrot = s1
    for _ in range(len(s1)):
        leftrot = leftrot[1:] + leftrot[0]
        rightrot = rightrot[-1] + rightrot[:-1]
        if leftrot == s2 or rightrot == s2:
            return True
    return False

checkRot = lambda s1, s2: s2 in s1*2

"""
6. Anagram Search or Matching all permutations of a pattern in text:

Check if any permutation of a pattern is present in the string. The Naive solution is to slide the pattern over the txt and check 
if the pair is an anagram. We can check for anagram in O(len(pat)) time, thus the time complexity of this solution is the same as
the naive pattern matching algorithm, ie, O((n-m+1)*m). The efficient solution here again is to use the character - indexed count 
array approach, but since dictionaries are not useful here we will implement character array using ord(char) as index. For this
solution we are essentially modifying the Rabin Karp Algorithm by matching the counts of the pattern and string. Steps:

(i) For every ith character in pat, we increment the value stored in it's corresponding index in the count array of txt and pat.
The count_txt array stores the value of current window of text and count_pat stores the frequency of pattern elements. 
(ii) In a loop from len(pat) to len(txt) - 1, we do the following:
    (a) If the count arrays are equal we found an occurrence of the pattern. Print index.
    (b) Else we virtually slide the count_txt window by adding the next frequency and subtracting the first. Hence we are sliding
    the frequency window of the letters in that substring which will be compared with the frequencies of the pattern.
    (c) We increment the count of the current character in count_txt and decrement the count of prev first character.
(iii) Check if the count arrays are equal for the last window in the array as well.
"""
def anagramSearchNaive(txt, pat):
    for i in range(len(txt) - len(pat) + 1): # O(n-m+1)
        if anagram(txt[i:i+len(pat)], pat):
            return True
    return False

def anagramSearch(txt, pat):

    # making two count arrays (constant space)
    count_txt = [0]*256# substring window frequencies
    count_pat = [0]*256 # pattern frequencies

    # Initialising window and pattern frequencies for 1st window
    for i in range(len(pat)):
        count_txt[ord(txt[i])] += 1
        count_pat[ord(pat[i])] += 1
    
    # Sliding the window 
    for i in range(len(pat), len(txt)):
        # if the count arrays are same we have a match
        if count_txt == count_pat:
            print("Found at, ", i - len(pat))

        # increasing frequency of current character 
        count_txt[ord(txt[i])] += 1
        # decreasing frequency of first character of previous window
        count_txt[ord(txt[i - len(pat)])] -= 1
        
    # Checking for last window
    if count_txt == count_pat:
        print("Found at, ", len(txt)-len(pat))
    

"""
7. Lexicographic Rank of a string:
"""
"""
8. Longest Substring with Distinct Characters:
"""
