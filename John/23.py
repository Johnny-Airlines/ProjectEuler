'''
Problem 23
Find the sum of all positive integers which can not be written as the sum of two abundant numbers.
All intgers greater than 28123 can be written as the sum of two abundant numbers.
An anbundant number is such that the sum of its proper divisors is greater than itself.
'''

def isAbundant(n):
    sum = 1
    for i in range(2,int(n**0.5)+2):
        if n % i == 0:
            sum += i + int(n/i)
            if sum > n:
                return True
    return False

abundantNumbers = []
for i in range(28123):
    if isAbundant(i):
        abundantNumbers.append(i)

print(abundantNumbers)
numbers = {i:True for i in range(28123)}
for i in abundantNumbers:
    for j in abundantNumbers:
        if i+j in numbers:
            numbers[i+j] = False
print(numbers)
trueNums = [key if value else 0 for key,value in numbers.items()]
trueNums = list(set(trueNums))
sum = 0
for num in trueNums:
    sum += num
print(sum)
