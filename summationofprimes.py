## problem 10 ## 
import math

def isprime(n):
    squareroot = math.sqrt(n)
    for i in range(2,int(squareroot)+1):
        if n % i == 0:
            return False
    return True
    

def nthprime(n):
    primecount = 0
    i = 2
    while True:
        
        if isprime(i):
            primecount += 1
        if primecount == n:
            return i
        i = i+1

def getnextprime(curprime):
    st = curprime + 1
    while not isprime(st):
        st = st + 1
    return st

curprime = 2
sumofprimes = 0
while curprime < 2000000:
    sumofprimes += curprime
    curprime = getnextprime(curprime)

print sumofprimes

#solution: 142913828922

