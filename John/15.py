'''
Problem 15
In a 20 x 20 grid, and only being able to move to the right and down, how many ways are there from the top left to the bottom right
'''

num = 0
count = 0
for i in range(0,2**41-1):
    num += 1
    path = str(format(num, '040b'))
    if path.count('0') == path.count('1'):
        #print(path)
        count += 1
    if i % round((2**41-1)/100) == 0:
        print(round(i/((2**41-1)/100)))
print(count)
