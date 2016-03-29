'''
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?

'''
import math
import time

s = time.time()
def isprime(n):
    sqroot=int(math.sqrt(n))
    j=2
    while j<=sqroot:
        if n%j==0:
            return False
        j=j+1
    return True
    

#n = 13195 # 29
n = 600851475143
#n= 4000000
n2 = n
curprime = 2

def getnextprime(curprime):
    st = curprime + 1
    while not isprime(st):
        st = st + 1
    return st


while n > 0:

    if isprime(n):
        curhighprime = n
        break

    elif n%curprime == 0:
        print curprime
        curhighprime = curprime
        n = n/curprime
        continue
  
    else:
        curprime = getnextprime(curprime)
      #  print curprime," current prime"
        if curprime<=n2:
            continue
        else:
            break

print curhighprime
print time.time() - s
