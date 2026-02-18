'''
Problem 30
Find the sum of all the numbers that can be written as the sum of fifth powers of their digits.
As 1 = 1**5 is not a sum it is not included.
'''

count = 0
for num in range(2,1000000):
    i = [int(x) for x in str(num)]
    sum = 0
    for n in i:
        sum += n**5
    if sum == num:
        print(num,sum,i)
        count += num
print(count)
