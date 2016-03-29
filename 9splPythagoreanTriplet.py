## A Pythagorean triplet is a set of three natural numbers, a < b < c ##
## for which, a**2 + b**2 = c**2 ##
## There exists exactly one Pythagorean triplet for which a + b + c = 1000. ##
## Find the product abc. ##

def pythagorean(a,b,c):
    return a**2 + b**2 == c**2


for i in range(1,1001):
    for j in range(i,1001):
        for k in range(j,1001):
            if i+j+k == 1000 and pythagorean(i,j,k):\
               print i,j,k

## 200 375 425 ##
##Ans: 31875000 ##
