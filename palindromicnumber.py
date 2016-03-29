'''
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 x 99.

Find the largest palindrome made from the product of two 3-digit numbers.
'''
import math
import time

s = time.time()
def ispalindrome(n):
    if str(n) == str(n)[::-1]:
        return True
    else:
        return False


def isprime(n):
    sqroot=int(math.sqrt(n))
    j=2
    while j<=sqroot:
        if n%j==0:
            return False
        j=j+1
    return True


#numbers = range(10000,998002)
curpalindrome = None
for num1 in range(100,1000):
    for num2 in range(100,1000):
        t = num1 * num2
        if ispalindrome(t):
            if curpalindrome is None:
                curpalindrome = t
            elif curpalindrome < t:
                curpalindrome = t


print curpalindrome
print time.time() - s


## ans: 906609 ##
