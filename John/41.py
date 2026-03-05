'''
Problem 41
An n-digit number is pandigital if it makes use of all the digits 1 to n exactly once; for example, the 5-digit number, 15234, is 1 through 5 pandigital.
What is the largest n digit pandigital prime that exists?
'''

limit = 7654321
primes = {x:True for x in range(2,limit)}
cursor = 0
for i in range(2,int(limit**0.5)+1):
    for j in range(2,int(limit/i)+1):
        primes[i*j] = False
    cursor += 1
print("Primes done computing")
maxVal = 0
for prime in [key for key,val in primes.items() if val]:
    if len(list(str(prime))) == len(set(str(prime))) == max([int(i) for i in list(str(prime))]) and not "0" in list(str(prime)) and prime > maxVal:
        maxVal = prime
print(maxVal)
