'''
Problem 32
An n-digit number is pandigital if it makes use of all the digits 1 to n exactly once; for example, the 5-digit number, 15234, is 1 throught 5 pandigital.

The product 7524 is unusual, as the identity, 39*186 = 7254, cotaining multiplicand, multiplier, and product is 1 through 9 pandigital.
Find the sum of all products whose multiplicand/multiplier/product identity can be written as a 1 through 9 pandigital.
HINT: Some products can be obtained in more than one way so be sure to only include it once in your sum.
'''
def permutations(k,A):
    global perms
    if k == 1:
        perms.append("".join(A))
    else:
        permutations(k - 1, A)
        for i in range(k-1):
            if k % 2 == 0:
                A[i],A[k-1] = A[k-1],A[i]
            else:
                A[0],A[k-1] = A[k-1],A[0]
            permutations(k - 1, A)


perms = []
permutations(9,list("123456789"))
perms=list(set(perms))
perms.sort()

products = set()
for perm in perms:
    for lengthA in range(1,9):
        for lengthB in range(1,9):
            if lengthA + lengthB < 9:
                if int(perm[:lengthA])*int(perm[lengthA:lengthA+lengthB])==int(perm[lengthA+lengthB:]):
                    products.add(int(perm[lengthA+lengthB:]))
                    print(f"{perm[:lengthA]}*{perm[lengthA:lengthA+lengthB]}={perm[lengthA+lengthB:]}")
sum = 0
for product in products:
    sum += product
print(sum)
