'''
Problem 46
It was proposed by Christian Goldbach that every odd composite number can be written as the sum of a prime and twice a square.</p>
9 = 7 + 2 * 1^2
15 = 7 + 2 * 2^2
21 = 3 + 2 * 3^2
25 = 7 + 2 * 3^2
27 = 19 + 2 * 2^2
33 = 31 + 2 * 1^2
It turns out that the conjecture was false.
What is the smallest odd composite that cannot be written as the sum of a prime and twice a square?
'''

limit = 10000
primes = {x:True for x in range(2,limit)}
cursor = 0
for i in range(2,int(limit**0.5)+1):
    for j in range(2,int(limit/i)+1):
        primes[i*j] = False
    cursor += 1
composites = [n for n,isPrime in primes.items() if not isPrime]
primes = [n for n,isPrime in primes.items() if isPrime]
print("Primes done computing")


for composite in [n for n in composites if n % 2 != 0]:
    failsConjecture = True
    for prime in [n for n in primes if n < composite]:
        for square in [n**2 for n in range(int(((composite-prime)/2)**0.5)+1)]:
            if prime + 2 * square == composite:
                failsConjecture = False
                break
    if failsConjecture:
        print(composite)
        break
