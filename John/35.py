'''
Problem 35
The number, 197, is called a circular prime because all rotations of the digits: 197, 971, and 719, are themselves prime.
There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.
How many circular primes are there below one million?
'''

def rotate(n):
    res = list(str(n))
    res.append(res.pop(0))
    return "".join(res)


limit = 1000000
primes = {x:True for x in range(2,limit)}
cursor = 0
for i in range(2,int(limit**0.5)+1):
    for j in range(2,int(limit/i)+1):
        primes[i*j] = False
    cursor += 1

circularPrimes = []
for prime in [key for key,val in primes.items() if val]:
    isCircular = True
    rotation = rotate(prime)
    while int(rotation) != prime:
        if not primes[int(rotation)]:
            isCircular = False
        rotation = rotate(rotation)
    if isCircular:
        circularPrimes.append(prime)
print(len(circularPrimes))

