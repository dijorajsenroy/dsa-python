"""
A given pattern string is given and we are required to find all the indices at which we find the the pattern string. There are many
algorithms that can be used for pattern searching. Given here is an overview of the algos, pattern len - m, text len - n,
(i) Naive solution:
    Worst Case Time Complexity: O((n-m+1) * m)
    Auxillary Space: O(1)
(ii) Rabin Karp Algorithm:
     Pattern is pre-processed (by computing hash value)
     Worst Case Time Complexity: O((n-m+1) * m)
     Auxillar Space: O(1)
     But better on average cases
(iii) KMP Algorithm: 
      Pattern is pre-processed (by computing its LPS array)
      Worst Case Time Complexity: O(n = len(pattern)) 
      Auxillary Space: O(m = len(text))
(iv) Suffix Tree (built using Tries): O(m) Time Complexity, Text is pre-processed - preferable for fixed length text.

(i) Naive Solution:

The Naive solution idea is simple, we slide the pattern over the entire text and print the location at which its found.
The code for this approach is implemented below. 
"""

def patternMatchingNaive(text, pat):
    n = len(text)
    m = len(pat)
    for i in range(n-m+1):  # O(n-m + 1)
        if text[i:i+m] == pat:  # O(m)
            print(i)

"""
(ii) Rabin Karp Algorithm:

This algorithm also takes worse-case time complexity O((n-m + 1)* m) but performs better than Naive solution in average cases.
The idea of this algorithm is simple, the steps involved are:

(i) Slide the pattern string over the text, like in the Naive solution
(ii) Instead of comparing with each i:n-m substring, compute a hash value of the substring window.
(iii) If the hash value matches with the pattern only then we match individual characters. 
(iv) To prevent the computation of hash value of text window to be O(m), we use a sliding window like approach called Rolling Hash.
In this approach, we subtract the ASCII value of last element of previous window and add the ASCII value of next element, hence
Sliding virtually over the text for searching. if t(i) is the rolling hash value of the ith window, and m is length of pattern,
We have the expression t(i+1) = t(i) - ord(text[i]) + ord(text[i+m]). We can have more complicated hash functions that reduce
the number of false hits than the hash value sum matching technique. 
"""

def RabinKarpAlgorithm(text, pat):
    n = len(text)
    m = len(pat)
    # Computing hash value of pattern
    patHashVal = 0
    for i in pat:
        patHashVal += ord(i)

    # Initialising rolling hash window value
    rollingHashWindow = 0
    for i in text[:m]:
        rollingHashWindow += ord(i)

    # Comparing sliding value with pattern to minimise hits
    for i in range(m, n):
        if rollingHashWindow == patHashVal:
            # Executes lesser times than naive solution
            if text[i-m:i] == pat:
                print(i-m)
        # Sliding the hash value window over the text
        rollingHashWindow += ord(text[i]) - ord(text[i-m])

"""
(iii) Knuth-Morris-Pratt (KMP) Algorithm:

The KMP Algorithm is a Dynamic Programming algorithm, and computes the matched pattern indices in O(len(text)) time. The steps:

(a) Constructing the Longest Proper Prefix Suffix Array (LPS). The word proper perfix means the length of the prefix should
be smaller than the length of the given string. For a string "abc" its proper prefixes are "", "a", "b" and "abc". It's suffixes
are "", "c", "bc" and "abc". We need to compute the longest proper prefixes that is also a suffix and count them in an array. eg,
For string "ababc"
---> substr = "a", proper prefixes = {""}, suffixes = {"","a"}
     thus, lps[0] = len(common = {""}) = 0
---> substr = "ab", proper prefixes = {"", "a"}, suffixes = {"","b","ab"}
     thus, lps[1] = len(common = {""}) = 0
---> substr = "aba", proper prefixes = {"","a","ab"}, suffixes = {"", "a", "ba", "aba"}
     thus, lps[2] = len(common = {"","a"}) = 0<1 = 1
---> substr = "abab", proper prefixes = {"","a", "ab", "aba"}, suffixes = {"", "b","ab", "bab", "abab"}
     thus, lps[3] = len(common = {"", "ab"}) = 0<2 = 2
---> substr = "ababc", proper prefixes = {"","a", "ab", "aba", "abab"}, suffixes = {"", "c","bc", "abc", "babc","ababc"}
     thus, lps[3] = len(common = {""}) = 0
---> lps array = [0,0,1,2,0], for all equal, lps = [0,1,2,3..] and for all distinct, lps = [0,0,0...]

We can construct the LPS array in O(n^3) time, and using the efficient solution in O(n) time complexity. We are initialising the
LPS array as a global variable inside the function hence it can be accessed outside the function as well. In the efficient solution,
we try to re-use the existing values computed for the lps_array for the next value of the lps_array, rather than re-computing it 
freshly. This requires a relationship bewteen lps[i-1] and lps[i] to be defined for all values of i. We know for first letter, 
lps[0] always = 0. we initialise a variable l = lps[i-1], for 0th character, l = 0. For the given string "aaab", we have,
---> i = 0, l = lps[0] = 0
---> i = 1, s[i=1] == s[l=0] == "a", lps[1] = l+1 = 1
---> i = 2, s[i=2] == s[l=1] == "a", lps[2] = l+1 = 2
---> i = 3, s[i=3] =/= s[l=2], lps[3] = 0
"""

def lpsNaive(s):
    lps_array = []
    for i in range(len(s)):
        sub = s[:i+1]  # O(n)
        ppfx = []
        sfx = [""]
        uniq = []
        # computing proper prefixes
        for j in range(len(sub)):  # O(n)
            ppfx.append(sub[:j])
        # computing suffixes
        for j in range(len(sub)):
            sfx.append(sub[j:])
        # computing common elements:
        for j in ppfx:  # O(n)
            if j in sfx:  # O(n)
                uniq.append(j)
        # computing LPS array
        lps_array.append(len(max(uniq)))
    return lps_array

def LPScompute(s):
    lps_array = [0]
    for i in range(1, len(s)): # O(n)
        if s[i] == s[lps_array[i-1]]:
            lps_array.append(lps_array[i-1] + 1)
        else:
            lps_array.append(0)
    return lps_array

"""
(b) Using the above O(n) LPS method, we compute the lps array of the pattern. Using the Naive sliding string matching, now that
we have the LPS array of the pattern we can eliminate unnecessary comparisons of the n-m+1 x m total comparisons. In the given string
text = "aaaaab" and pat = "aaaa". The naive solution would slide this pattern over the text like this:
---> i = 0, s[i:i+n] == pat or "[aaaa]ab"
---> i = 1, "a[aaaa]b"
---> i = 2, "aa[aaab]"
The lps array of "aaaa" = [0,1,2,3], if we consult the lps array to decide the next iteration of matching pattern the LPS array 
tells us how many elements can be skipped for the next match. For example, for text = "aaaaab" and pat = "aaaa", 
---> i = 0, j = 0: txt[i] == pat[j] == "a"
---> i = 1, j = 1: txt[i] == pat[j] == "a"
---> i = 2, j = 2: txt[i] == pat[j] == "a"
---> i = 3, j = 3: txt[i] == pat[j] == "a"
---> i = 4, j = 4: j == M : j = lps[4-1] = 3 --> print 0
---> i = 4, j = 3: txt[i] == pat[j] == "a"
---> i = 5, j = 4: j == M : j = lps[4-1] = 3 --> print 1
---> i = 5, j = 3: txt[i] != pat[j]: j!= 0: j = lps[3-1] = 2 
---> i = 5, j = 2: txt[i] != pat[j]: j!= 0: j = lps[2-1] = 1
---> i = 5, j = 1: txt[i] != pat[j]: j!= 0: j = lps[1-1] = 0
---> i = 5, j = 3: txt[i] != pat[j]: j== 0: i = i+1 = 6
---> i(6) > N(5): terminate 
"""

# From GFG site
def KMPSearch(pat, txt):
    M = len(pat)
    N = len(txt)
    lps = LPScompute(pat)
    j = 0  # index for pattern element
    i = 0  # index for text element
    while i < N:
        # comparing pat and text
        if pat[j] == txt[i]:
            i += 1
            j += 1
        # pattern is found when index is length
        if j == M:
            print("Found pattern at index " + str(i-j))
            # skipping lps[0..lps[j-1]] characters as they match anyways
            j = lps[j-1]

        # mismatch after j matches
        elif i < N and pat[j] != txt[i]:
            # skipping lps[0..lps[j-1]] characters as they match anyways
            if j != 0:
                j = lps[j-1]
            else:
                i += 1