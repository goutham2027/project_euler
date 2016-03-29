## 48 self powers ##

## 1**1 2**2 ... 10**10 = 10405071317 ##

## find the last ten digits of the series of 1**1 2**2 ... 1000*1000 ##


ssp = 0
import math
for i in range(1,1001):
    ssp  = ssp + i**i

print ssp


##Ans: 9110846700 ##
