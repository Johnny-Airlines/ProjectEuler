'''
Problem 25
What is the index of the first Fibonnaci number to have 1000 digits?
'''

a = 1
b = 1
c = 1
while len(str(a)) != 1000:
    a,b = b,a+b
    c += 1
print(a,b)
print(c)

