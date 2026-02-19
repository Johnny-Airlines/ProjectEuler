'''
Problem 37
The number 3797 has an interesting property. Being prime itself, it is possible to continuously remove digits from left to right, and remain prime at each stage: 3797, 797, 97, and 7. Similarly we can work from right to left: 3797, 379, 37, and 3.
Find the sum of the only eleven primes that are both truncatable from left to right and right to left.
NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.
'''


limit = 1000000
primes = {x:True for x in range(2,limit)}
cursor = 0
for i in range(2,int(limit**0.5)+1):
    for j in range(2,int(limit/i)+1):
        primes[i*j] = False
    cursor += 1
primes[1] = False
sum = 0
for prime in [key for key,val in primes.items() if val and key>9]:
    isTruncatablePrime = True
    truncOffset = 1
    while truncOffset < len(str(prime)):
        if not primes[int(str(prime)[truncOffset:])]:
            isTruncatablePrime = False
        truncOffset += 1
    truncOffset = -1
    while truncOffset > -1*len(str(prime)):
        if not primes[int(str(prime)[:truncOffset])]:
            isTruncatablePrime = False
        truncOffset -= 1
    if isTruncatablePrime:
        print(prime)
        sum += prime
print(sum)

