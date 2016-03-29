## factorial digit sum ##

#n facotorial means n  (n − 1)  ... 3  2  1
#For example, 10fact = 10 x 9 x x 3 x 2 x 1 = 3628800,
#and the sum of the digits in the number 10fact is 3 + 6 + 2 + 8  8 + 0 + 0 = 27
#Find the sum of the digits in the number 100 fact


fact = {0:1,1:1}
def factorial(n):
    if fact.has_key(n):
        return fact[n]
    else:
        tmp = n * factorial (n-1)
        fact [n] = tmp
        return tmp

n = 100
digits = factorial(n)
sumofdigits = 0
while digits > 0:
    sumofdigits += (digits%10)
    digits = digits/10
    
print sumofdigits


## sol: 648 ##
