'''
Problem 5
What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
'''

#Euclid's Algorithm
def slowerGcd(a,b):
    while a != b:
        if a > b:
            a -= b
        elif a < b:
            b -= a
    return a

#Euclidean Algorithm
def gcd(a,b):
    if a == 0 or a==b:
        return b
    if a > b:
        return gcd(a % b, b)
    if a < b:
        return gcd(b % a, a)

def lcm(a,b):
    return int(abs(a*b)/gcd(a,b))

def lcmMany(*args):
    num = 1
    for a in args:
        num = lcm(num,a)
    return num

print(lcmMany(*tuple(range(1,21))))
