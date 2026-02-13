'''
Problem 12
What is the first triangle number to have over 500 divisors
'''

import math

def nthTriangleNumber(n):
    return int(n*(n+1)/2)

def getDivisors(n):
    divisors = []
    for i in range(1,math.floor(math.sqrt(n))):
        if n % i == 0:
            divisors.append(i)
            divisors.append(n/i)
    return divisors

x = 1

while len(getDivisors(nthTriangleNumber(x))) <= 500:
    x += 1

print(nthTriangleNumber(x))
