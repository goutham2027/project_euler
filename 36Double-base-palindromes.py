'''
The decimal number, 585 = 10010010012 (binary),
is palindromic in both bases.

Find the sum of all numbers, less than one million,
which are palindromic in base 10 and base 2.

(Please note that the palindromic number, in either base,
may not include leading zeros.)
'''

def ispalindrome(val):
    if str(val) == str(val)[::-1]:
        return True
    return False


n = 1000000
num = 1
sumofpals = 0 
while num <= n:
    if ispalindrome(num) and ispalindrome(bin(num)[2:]):
        sumofpals += num
        print num
    num += 1

print "sum of palindromes ", sumofpals

##Ans: 872187 ## 
