'''
Problem 34
145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 + 145 = 145.

Find the sum of all numbers which are equal to the sum of the factorial of the digits.
Note: As 1! = 1 and 2! = 2 are not sum they are not included.
'''

def fact(n):
    res = 1
    for x in range(1,n+1):
        res *= x
    return res

def sumDigits(n):
    sum = 0
    for i in str(n):
        i = int(i)
        sum += fact(i)
    return sum

sum = -3
for i in range(1000000):
    if i == sumDigits(i):
        sum += i
print(sum)
