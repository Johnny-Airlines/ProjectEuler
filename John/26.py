'''
Problem 26
Find the value of d < 1000
for which 1/d
contains the longest recurring cycle in its decimal fraction part.
'''
from decimal import *

PREC = 200000
getcontext().prec = PREC
nums = {}
maxD = 0
maxRepetend = 0
for d in range(1,1000):
    reciprocal = str(Decimal(1)/Decimal(d))[2:]
    if len(reciprocal) < PREC:
        pass
    else:
        for repetend in range(1,2000):
            if reciprocal[repetend:repetend*2] == reciprocal[repetend*2:repetend*3]:
                nums[d] = repetend
                if repetend > maxRepetend:
                    maxD = d
                    maxRepetend = repetend
                break

print(maxD)



