'''
Problem 1
Sum all the numbers that are multiples of 3 or 5 below 1000
'''

sum = 0
for i in range(0,1000):
    if i % 3 == 0 or i % 5 == 0:
        sum = sum + i
print(sum)
