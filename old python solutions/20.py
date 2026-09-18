'''
Problem 20
Sum the digits in 100!
'''

def factorial(n):
    num = 1
    for i in range(1,n+1):
        num *= i
    return num

num = str(factorial(100))
sum = 0
for i in num:
    sum += int(i)
print(sum)
