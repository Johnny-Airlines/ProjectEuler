'''
Problem 3
Largest prime factor of the number 60085147512
'''

import math

def getFactor(x):
    for i in range(2,math.floor(math.sqrt(x))):
        if x % i == 0:
            if x/i > i:
                return x/i
            else:
                return i
    return "Prime"

num = 600851475143
primes = []

while getFactor(num) != "Prime":
    num = getFactor(num)

print(int(num))
    
