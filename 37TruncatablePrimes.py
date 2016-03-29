##The number 3797 has an interesting property. Being prime itself, it is possible to continuously remove ##
##digits from left to right, and remain prime at each stage: 3797, 797, 97, and 7.##
## Similarly we can work from right to left: 3797, 379, 37, and 3. ##

## Find the sum of the only eleven primes that are both truncatable from ##
##left to right and right to left. ##

## NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes. ##


from prime import Prime
p = Prime()
def truncatableprime(n):
    ## from left to right ##
    for i in range(len(str(n))):
        if not p.isprime(int(str(n)[i:])):
            return False
    ## from right to left             
    tmp = n
    while tmp>0:
        if not p.isprime(tmp):
            return False
        tmp = tmp/10

    return True


count = 1

n = 10
sumofTP = 0
while count <= 11:
    n = p.getnextprime(n)
    if truncatableprime(n):
        print n
        sumofTP += n
        count += 1

print "sum is ", sumofTP


##Ans: 748317 ##
