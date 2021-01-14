"""
1. Binary Equivalent of a number N:
"""
def binary(n):
    # base case if division leads to 0
    if n == 0:
        return

    # calling on n/2 and printing remainder of n/2
    binary(n // 2)
    print(n % 2, end=" ")
    
"""
2. Print N to 1 and 1 to N

Using the simple fact that when print statement is before recursive call, 
we are printing the number before it is changed by the next call. So the order of 
printing would be N, N-1, N-2, N-3 and so forth. But when it is after the recursive 
statement, the control makes the calls first and then the call preceding the base-case 
would execute its print statement being 1 (since base-case is 0), then control goes to 
the call before that and 2 is printed upto the first call where N is printed. In effect
if print statement is after the recursive call then printing order is reversed.

nTo1 is tail recursive and takes less time than oneToN on modern compilers
"""

def oneToN(n):
    if n == 0:
        return

    oneToN(n-1)
    print(n)


def nTo1(n):
    if n == 0:
        return

    print(n)
    nTo1(n-1)
    
"""
3. Tail recursive solution for factorial of N:
A tail recursion does not return anything to it's previous call. Hence we return the value of
factorial to the control when base case is reached. We make an extra argument to save the value
of n in the next call and an argument k which uses the n values each iteration to save the factorial.
n takes values n, n-1, n-2.. and k takes values n*k, n-1*(n*k), n-2*(n-1*(n*k)) and so forth.
K has been given a default initial value of 1, which is a python feature.
"""

def factorial(n,k=1):

    if n ==1 or n == 0:
        return k
    else:
        return factorial(n-1, n*k)

"""
4. Fibonacci Numbers:
A fibonacci number is defined as A(n) = A(n-1) + A(n-2). for all numbers >=0. Therefore there needs to be 
base-cases for the two smallest numbers 0 and 1. 
"""
def fib(n):
    if n==0 or n==1:
        return n # 0 or 1 respectively
    else:
        return fib(n-1) + fib(n-2)

"""
5. Sum of N natural numbers. base-case should be for n=0, sum(0)=0. The solution is simple 
but can be converted into a tail recursion. The non-tail recursive solution and the tail recursive 
solution are given as follows. The time complexity of both solutions is Theta(n) but the auxillary space
utilised by tail recursion is optimised compared to non tail recursion.
"""

def natsum_NTR(n):
    return 0 if n == 0 else (n + natsum_NTR(n-1))

def natsum_TR(n,k=0):
    return k if n == 0 else natsum_TR(n-1, n+k)

    
"""
6. Sum of digits of a number using recursion: num//10 removes the last digit, num%10 gives the last digit,
the base case should be when integer division by 10 makes the number 0. The non tail recursion is simply add
the num//10 iteration to num%10. The tail recursion method would be to, add the modulus result to a dummy parameter.
And make the base return the result to the control, on the last execution of the recursive statement. For non-tail
recursion base-case  may return any number to its previous call, but tail recursion needs to return the result.
Time complexity is Theta(d) and Auxillary Space Theta(d) for recursion calls. The iterative solution takes const space.
"""
def digisum_NTR(num):
    return 0 if num == 0 else (num%10 + digisum_NTR(num//10))


def digisum_TR(num, k=0):
    return k if num == 0 else digisum_TR(num//10, k + num%10)

