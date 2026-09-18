'''
Problem 10
Sum the primes below 2 million
'''

import math

limit = 2000000
primes = {x:True for x in range(2,limit)}
cursor = 0
for i in range(2,math.ceil(math.sqrt(limit))):
    for j in range(2,int(limit/i)+1):
        primes[i*j] = False
    cursor += 1

primes = [key for key,val in primes.items() if val]
sum = 0
for prime in primes:
    sum += prime
print(sum)

