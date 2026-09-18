'''
Problem 43
The number, 1406357289, is a 0 to 9 pandigital number because it is made up of each of the digits 0 to 9 in some order, but it also has a rather interesting sub-string divisibility property.
Let d_1 be the 1st digit, d_2 be the 2nd digit, and so on. In this way, we note the following:
d_2d_3d_4=406 is divisible by 2
d_3d_4d_5=063 is divisible by 3
d_4d_5d_6=635 is divisible by 5
d_5d_6d_7=357 is divisible by 7
d_6d_7d_8=572 is divisible by 11
d_7d_8d_9=728 is divisible by 13
d_8d_9d_10=289 is divisible by 17
Find the sum of all 0 to 9 pandigital numbers with this property.
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
permutations(10,list("0123456789"))
perms=list(set(perms))
perms.sort()

perms = [perm for perm in perms if len(str(int(perm))) == 10]

sum = 0
for perm in perms:
    if int(perm[1:4]) % 2 == 0 and int(perm[2:5]) % 3 == 0 and int(perm[3:6]) % 5 == 0 and int(perm[4:7]) % 7 == 0 and int(perm[5:8]) % 11 == 0 and int(perm[6:9]) % 13 == 0 and int(perm[7:10]) % 17 == 0:
        print(perm)
        sum += int(perm)
print(sum)