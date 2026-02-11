'''
Problem 2
Sum all even Fibonnaci numbers below 4 million
'''

sum = 0

def fib(x,y):
    global sum
    if x+y < 4000000:
        if (x+y)%2 == 0:
            sum += x+y
        fib(y,x+y)

fib(1,1)
print(sum)


