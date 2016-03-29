## problem 35 ##
## Circular Primes ##
'''
The number, 197, is called a circular prime because all rotations of the digits: 197, 971, and 719, are themselves prime.

There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.

How many circular primes are there below one million?
'''



def isprime(n):
    import math
    squareroot = math.sqrt(n)
    for i in range(2,int(squareroot)+1):
        if n % i == 0:
            return False
    return True


def get_rotations(num):
    string_num = str(num)
    rotations = []
    for i in range(len(string_num)):
        rotations.append(int(string_num[i:] + string_num[0:i]))
    return rotations

def circular_prime(num):
    num_list = get_rotations(num)
    for num in num_list:
        if isprime(num):
            continue
        else:
            return False
    return True

#print circular_prime(2)
#print circular_prime(197)
#print circular_prime(3)
#print circular_prime(4)
#print circular_prime(5)
#print circular_prime(7)

circular_prime_count = 0
for i in range(2,1000000):
    if circular_prime(i):
        circular_prime_count += 1
print circular_prime_count

# Answer: 55
