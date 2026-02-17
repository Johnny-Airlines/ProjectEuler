'''
Problem 27
Considering quadratics of the form:
n**2 + a*n + b where |a| < 1000 and |b| <= 1000
Find the product of the coefficients, a and b, for the quadratic expression that produces the maximum number of primes for consecutive values of n, starting with n = 0.
'''


limit = 200000
primes = {x:True for x in range(2,limit)}
cursor = 0
for i in range(2,int(limit**0.5)+1):
    for j in range(2,int(limit/i)+1):
        primes[i*j] = False
    cursor += 1

#primes = [key for key,val in primes.items() if val]
maxN = 0
bestA = 0
bestB = 0
for a in range(-999,1000):
    for b in range(-1000,1000+1):
        quad = lambda n: n**2+a*n+b
        n = 0
        res = lambda n: primes[quad(n)] if quad(n) < limit and quad(n) > 1 else False
        while res(n):
            n += 1
        if n > maxN:
            maxN = n
            bestA = a
            bestB = b
            print(n,a,b)

quad = lambda n: n**2+bestA*n+bestB
print(maxN,bestA,bestB)
print(bestA*bestB)

