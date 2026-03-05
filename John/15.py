'''
Problem 15
In a 20 x 20 grid, and only being able to move to the right and down, how many ways are there from the top left to the bottom right
'''

def fact(n):
    res = 1
    while n >= 1:
        res *= n
        n -= 1
    return res

def choose(n,k):
    return fact(n)/(fact(k)*fact(n-k))

print(int(choose(20*2,20)))
