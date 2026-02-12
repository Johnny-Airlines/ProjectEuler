'''
Problem 5
What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
'''

def isEvenlyDivisible(x):
    for i in range(1,21):
        if x % i != 0:
            return False
    return True


num = 20
while not isEvenlyDivisible(num):
    num = num + 1
print(num)
