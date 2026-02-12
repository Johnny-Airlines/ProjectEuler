'''
Problem 7
What is the 10 001st prime?
'''

import math

limit = 200000
nums = {x:True for x in range(2,limit)}

for i in range(2,math.ceil(math.sqrt(limit))):
    if nums[i]:
        for j in [i**2+x*i for x in range(0,limit)]:
            nums[j] = False

primes = [key for key,val in nums.items() if val]
print(primes[10000])
