'''
Problem 24
When arranged in ascending order, what is the millionth permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?
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
#perms.append("".join(list(i)))
perms.sort()
print(perms[1000000-1])
