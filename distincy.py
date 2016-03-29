## problem 29 ##

## distinct powers ##



items = set()
for a in range(2,101):
    for b in range(2,101):
        items.add(pow(a,b))
        
print len(list(items))

## sol: 9183 ##
