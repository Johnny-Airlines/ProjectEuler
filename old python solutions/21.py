'''
Problem 21
Sum all the amicable numbers under 10000.
Let d(n) be defined as the sum of proper divisors of n ( numbers less than n which divide evenly into n).
If d(a) = b and d(b) = a, where a != b, then a and b are amicable numbers.
'''

def d(n):
    divisors = []
    for i in range(1,int(n**0.5)+2):
        if n % i == 0:
            divisors.append(i)
            divisors.append(int(n/i))
    sum = 0 
    for i in divisors:
        sum += i
    sum -= n
    return sum

sum = 0
for i in range(10000+1):
    if d(d(i)) == i and d(i) != i:
        sum += i
print(sum)
