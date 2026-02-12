'''
Problem 4
Find the largest palindrome made from the product of two 3-digit numbers.
'''

def isPalindrome(x):
    if x == int(str(x)[::-1]):
        return True
    return False

largestPalindrome = 0

for i in range(0,1000):
    for j in range(0,1000):
        product = i*j
        if isPalindrome(product) and product > largestPalindrome:
            largestPalindrome = product

print(largestPalindrome)
