'''
Problem 10
Sum the primes below 2 million

Notes:
Extremely slow in python(Has not been run in python yet, only translated to c first then run online in an onlince compiler)
'''

import math

limit = 2000000
nums = {x:True for x in range(2,limit)}

for i in range(2,math.ceil(math.sqrt(limit))):
    if nums[i]:
        for j in [i**2+x*i for x in range(0,limit)]:
            nums[j] = False

primes = [key for key,val in nums if val]
sum = 0
for prime in primes:
    sum += prime
print(sum)

