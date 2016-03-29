
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
        
        
#sol: 104743
