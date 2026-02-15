'''
Problem 9 
Find the Pythagorean triplet for which a + b + c = 1000
'''

import math

for i in range(1,1001):
    for j in range(1,1001):
        hyp = math.sqrt(i**2+j**2)
        if hyp.is_integer() and i+j+hyp == 1000 and j < i:
            print(int(i*j*hyp))
