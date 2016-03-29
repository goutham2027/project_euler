



def seq(n):
    global cnt
    if n <= 1:
        cnt = cnt +1 
        return cnt
    else:
        cnt = cnt +1
        return seq(n/2 if n%2 == 0 else 3*n+1)

maxchaincount = 0

for n in range(1,1000001):
    cnt = 0
    cnt = seq(n)
    if cnt >= maxchaincount:
        maxchaincount = cnt
        print n



##Ans: 837799 with chain length 525 ##
