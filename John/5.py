'''
Problem 5
What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
'''

def gcd(a,b):
    while a != b:
        if a > b:
            a -= b
        elif a < b:
            b -= a
    return a

def lcm(a,b):
   return int(abs(a*b)/gcd(a,b))

def lcmMany(*args):
    num = 1
    for a in args:
        num = lcm(num,a)
    return num

print(lcmMany(*tuple(range(1,21))))
