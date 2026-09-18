'''
Problem 36
The decimal number, 585 = 1001001001_2 (binary), is palindromic in both bases.
Find the sum of all numbers, less than one million, which are palindromic in base 10 and base 2.
Please note that the palindromic number, in either base, may not include leading zeros.
'''

def isPalindromic(a):
    n = list(str(a))
    nReversed = list(str(a))
    nReversed.reverse()
    if nReversed == n:
        return True
    else:
        return False

sum = 0
for i in range(1000000+1):
    if isPalindromic(i) and isPalindromic(str(bin(i))[2:]):
        sum += i
print(sum)
