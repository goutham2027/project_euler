'''
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
'''
import math
import time

s = time.time()


def stage1(n):
    if n%20 == 0 and n%14 == 0 and n%16 == 0 and n%18 == 0:
        return True
    return False

def stage2(n):
    if n%11 == 0 and n%13 == 0 and n%17 == 0 and n%19 ==0:
        return True
    return False

def stage3(n):
    if n%10 == 0 and n%8 == 0 and n%9 == 0 and n%7 == 0 :
        return True
    return False

def isprime(n):
    sqroot=int(math.sqrt(n))
    j=2
    while j<=sqroot:
        if n%j==0:
            return False
        j=j+1
    return True

n = 2
while True:
 #   print n
    if stage2(n) and stage1(n):
        break


    n=n+1

print n

print time.time() - s


## Ans: 232792560 ##

