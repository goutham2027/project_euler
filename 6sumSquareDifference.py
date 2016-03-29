## sum of squares of first ten numbers is 385 ##
## square of sum of first ten natural numbers is 55**2 3025 ##
## Difference is 3025 - 385 = 2640 ##
## Find the difference between the sum of the squares of the first 100 natural ##
## numbers and the square of the sum ##


def sumofsquares(n):
    return (n*(n+1)*(2*n+1))/6

def sumofnumbers(n):
    return (n*(n+1))/2
    

print sumofnumbers(100)**2 - sumofsquares(100)


## Ans 25164150 ## 
