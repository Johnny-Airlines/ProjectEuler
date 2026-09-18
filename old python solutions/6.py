'''
Problem 6
Find the difference between the sum of the squares of the first 100 natural numbers and the square of the sum
'''

sumOfSquares = 0
for i in range(0,101):
    sumOfSquares += i**2

sum = 0
for i in range(0,101):
    sum += i

squareOfSum = sum ** 2

print(squareOfSum-sumOfSquares)
