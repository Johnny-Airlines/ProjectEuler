'''
Problem 14
Which starting number, under 1 million, produces the longest Collatz chain?
'''
def collatz(n):
    if n % 2 == 0:
        return n/2
    else:
        return n*3 + 1

def collatzConjecture(n):
    counter = 0
    while n != 1:
        n = collatz(n)
        counter += 1
    return counter


longestChainLength = 0
longestChainStartNumber = 0
for i in range(1,1000000):
    length = collatzConjecture(i)
    if length > longestChainLength:
        longestChainLength = length
        longestChainStartNumber = i

print(longestChainStartNumber)
