## problem-50 ##
## Consecutive prime sum ##

'''
The prime 41, can be written as the sum of six consecutive primes:

41 = 2 + 3 + 5 + 7 + 11 + 13
This is the longest sum of consecutive primes that adds to a prime below one-hundred.

The longest sum of consecutive primes below one-thousand that adds to a prime, contains 21 terms, and is equal to 953.

Which prime, below one-million, can be written as the sum of the most consecutive primes?
'''
def nthprime(n):
    primecount = 1
    prime = 0
    while primecount <= n:
        prime = getnextprime(prime)
        primecount+= 1
    return prime

def isprime(num):
    ''' Checks whether given number(n) is prime or not '''
    import math
    squareroot = math.sqrt(num)
    for i in range(2,int(squareroot)+1):
        if num % i == 0:
            return False
    return True

primes = []

def getnextprime(num=1):
    if num < 2:
        return 2
    nextnum = num + 1
    while not isprime(nextnum):
        nextnum += 1
    return nextnum

def getpreviousprime(num):
    if num <= 2:
        return 2
    previousnum = num - 1
    while not isprime(previousnum):
        previousnum -= 1
    return previousnum
    
def getAllPrimes(num):
    ''' Get all primes less than the given number '''
    ### implement with a hint argument which gives the list of already existing primes ###
    primes = []
    prime = 2
    while prime <= num:
        primes.append(prime)
        prime = getnextprime(prime)
    return primes
    
def findConsecutivePrimes(num):
    ''' take a prime and return consecutive primes whose sum equal to given prime '''
    # get all primes less than given prime(num) # @done@
    primes = getAllPrimes(num)
#    while sum(primes) >= num or len(primes) == 0
    # while sum of primes is less than or equal to given prime(num) pop the first element #
    # when it is less return false. when it is true return true and the consecutive primes. #

    
    

