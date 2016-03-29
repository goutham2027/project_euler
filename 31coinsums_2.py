import time
s = time.time()
count = 0
for onep in range(0,201):
    for twop in range(0,101):
        if onep+twop*2 >200:
            break
        for fivep in range(0,41):
            if onep+twop*2+fivep*5 > 200:
                break
            for tenp in range(0,21):
                if onep+twop*2+fivep*5+tenp*10 > 200:
                    break
                for twentyp in range(0,11):
                    if onep+twop*2+fivep*5+tenp*10+twentyp*20 > 200:
                        break
                    for fiftyp in range(0,5):
                        if onep+twop*2+fivep*5+tenp*10+twentyp*20+fiftyp*50 > 200:
                            break
                        for onepound in range(0,3):
                            tmp = onep*1 + twop*2 + fivep*5 + tenp*10 + twentyp*20 + fiftyp*50 + onepound*100
                            if tmp == 200:
                                #print onep,' ',twop,fivep,' ',tenp,' ',twentyp,' ',fiftyp,' ',onepound
                                count += 1
    print onep, count
                                
print time.time() - s                 


##Ans: 73681+1 ##
## Add 1 as we can make a combination of 2 pounds with one 2 pound coin ##
