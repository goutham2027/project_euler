## problem 25 ##

fib = {0:0,1:1}

def fibonacci(n):
    if fib.has_key(n):
        return fib[n]
    else:
        tmp = fibonacci(n-1) + fibonacci(n-2)
        fib[n] = tmp
        return tmp
    

i = 1
while True:
    if len(str(fibonacci(i))) == 1000:
       print i
       break
    i= i+1

##sol: 4782 ##
