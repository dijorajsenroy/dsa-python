"""
1.
Printing all divisors of a number n in sorted order in O(root(n)) time:
This uses the facts that - divisors always exist in pairs and one of them is 
always less than root(n). We simply traverse a loop from 0 to root(n) and root(n)
to n to get all divisors in sorted order.
"""
import math
def divisors(n):
    i=1
    divs = []
    while(i*i <=n):
        if (n%i == 0):
            divs.append(i)
        i+=1
    while(i>=1):
        if(n%i ==0):
            divs.append(n//i)
        i-=1
    return divs


"""
2.
Optimised Solution for checking if number is prime, in O(root(n)) time:
We add bases cases for 0,1 and check for divisibility of 2 and 3. Prime numbers have the property,
of occurring with one number in between with the exception of 2 and 3, so we check for this exception.
After which we run a loop from 5, the next prime number and check for i and i+2 to be prime. To furthur 
optimise this a step of 6 has been added, because this pair occurs after an interval of 6 numbers from a
prime number. Using these properties, in the i-loop we traverse all the known prime numbers pairs 5,7, 11,13, 
17,19 and so forth, that are smaller than the root of the number, and check for divisibility with the number.

"""
import math
def isPrime(n):
    if n == 1 or n == 0:
        return False
    elif n == 2 or n == 3:
        return True
    elif n%2 == 0 or n%3 == 0:
        return False
    else:
        for i in range(5, round(math.sqrt(n)) + 1, 6):
            if n%i == 0 or (n+2)%i == 0:
                return False
        return True

"""
3. 
HCF and LCM using the Optimised Euclidean Algorithm. For two numbers A,B the time complexity of this solution is
O(min(A,B)). The Euclidean algorithm states, gcd(A,B) = gcd(A-B, B), assuming A>B. We use mod instead of this:
LCM = A*B/HCF.
"""
def gcd(a,b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)


"""
4.
Counting digits in a number O(1) solution:
"""
count_digits = lambda n: math.floor(math.log10(n) + 1)

"""
5. 
Reversing a number - recursive solution. As base case when n is 0, 0 is returned to previous call.
Otherswise the remainder of n%10 (last digit) is multiplied by 10^length of num, and to that the next 
recusrive call is added, passing arguments n/10 (or the number without the last digit), effectively reducing
the length of the number and the last digit being added to result, repeatedly till the n is 0 (no digits left)
Theta(n) time complexity
"""
def reverse(n):
    l = count_digits(n)
    if n == 0:
        return 0
    else:
        return ((n % 10)*(10 ** l)) + reverse(n/10)

"""
6.
Number of Trailing Zeroes in Factorial of n Problem: We count the number of 5s that are a factor of the number as 
that determines the number of trailing zeros, given that 5x2 = 10 and, there are usually more 2s than 5s as factors 
of a number. The formula implemented: [n/5] + [n/25] + [n/125] .... [n/5^i] for i<=n
"""
def countZeros(n):
    res = 0
    i=5
    while(i<=n):
        res += n//i
        i *= 5
    return res
print(countZeros(10))

