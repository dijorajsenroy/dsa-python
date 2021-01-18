"""
1. Sieve of Eratosthenes Algorithm for printing prime numbers up to n in O(nloglogn) time

    i-loop:
            Running a loop to select a prime number in (2 to root(n)), whose
            multiple will be marked as not prime or false. This will execute only 
            for numbers marked True, hence all False numbers wont be considered.

    j-loop:
            the condition checks if value at i is True (or is prime).
            If it is prime then we use i for a loop to mark multiples of 
            i False, as they are known consonants. loop starts from 2*i so i 
            is not marked false, and step is i as we are checking for multiples,
            j = 2i, 2i+i, 2i+i+i and so forth. loop can also start from i*i and 
            futhur optimise the solution. In this process, j takes values, 
            j = i*i, i*(i+1), i*(i+2) and so forth.
"""
import math
def soe(n):
    # creating a boolean array to store prime nums and marking 0,1 as False
    primes = [True for i in range(0, n + 1)]
    primes[0] = False
    primes[1] = False
    # i-loop
    for i in range(2, round(math.sqrt(n)) + 1): 
        if primes[i]: 
           # j-loop
            for j in range(i*i, n+1, i):
                primes[j] = False
    return [i for i in range(0, n+1) if primes[i]]

"""
2. Euclidean Algorithm to compute HCF:

The Euclidean algorithm is a recursive technique to calculate the GCD of two numbers A,B given A>B. It states that,
GCD(A,B) = GCD(A-B, B). Since it is difficult to determine which number passed as argument is larger, we optimise
this algorithm and instead of subtraction we compute modulus which removes the -ve parameter issue.
"""

def gcd(A,B):
    if B == 0:
        return A
    else:
        return gcd(B, A%B)
  
"""
3. Number of divisors and Sum of divisors:

To compute these two quanitities we find the prime factorisation of the number n. Such that n = p1^e1 . p2^e2 .... pk^ek. 
Where pk is the kth prime factor and ek is its exponent value. For finding prime factors we may use Sieve of Eratosthenes,
or Fermats Factorization Method. The number of divisors thus D(n) = (e1 + 1)*(e2 + 1)*...(ek + 1). The sum of factors is:
S(n) = (p1^(e1+1) - 1)/(p1 - 1) * (p2^(e2+1) - 1)/(p2 - 1) * (pk^(ek+1) - 1)/(pk - 1). Converting to code we have :
"""

# function to compute p powers of q factors - O(pq)
def findpow(n, factors):
    res = []
    for i in factors:
        count = 0
        a=n
        while(a >= i):
            if a % i == 0:
                count += 1
            a = a/i
        res.append((i,count))
    return res

# Computing sum and number of divisors
def compute(n):
    prime_factors = findpow(n, [i for i in soe(n) if n%i == 0])
    Dn = 1
    Sn = 1
    for i in prime_factors:
        pk,ek = i
        Dn *= (ek+1)
        Sn *= (pk**(ek+1) - 1)//(pk - 1)
    
    return Dn,Sn



