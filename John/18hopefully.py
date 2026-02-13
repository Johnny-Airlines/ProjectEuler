def getColumn(matrix,i):
    return [row[i] for row in matrix]

def prettyPrint(matrix):
    for row in matrix:
        print(row)
'''
triangle = """3
7 4
2 4 6
8 5 9 3"""
badRows = triangle.split("\n")
rows = []
for row in badRows:
    row = row.split(" ")
    rows.append(row)

rows.pop(0)
print(rows)
j = 0
for row in rows:
    for x in row:
        j += 1
distances = [[float('inf') for j in range(j)] for i in range(j+1)]
for i in range(len(distances)):
    distances[i].insert(i,"-")
print(distances)

i = 0
a = 0
j = 0
offset = 0
while i < 4:
    row = rows[a]
    #j = 0
    b = j
    k = i+offset
    running = True
    while running:
        if distances[i][k] == "-":
            k += 1
        else:
            distances[i][k] = row[j]
            j += 1
            k += 1
            if j >= b+2:
                running = False
    if row[j-1] == row[-1]:
        i += 1
        a += 1
        j = 0
        offset += len(row)
    else:
        print(row[j-1])
        i += 1
        j -=1
        '''

'''
distances = [
 ["-",7,5,10,float('inf')],
 [7,"-",4,17,3],
 [5,4,"-",6,float('inf')],
 [10,17,6,"-",3],
 [float('inf'),3,float('inf'),3,"-"]
]
'''
# Simple Python3 program to find mirror of
# matrix across diagonal.
MAX = 100


def imageSwap(mat, n):

    # for diagonal which start from at
    # first row of matrix
    row = 0

    # traverse all top right diagonal
    for j in range(n):

        # here we use stack for reversing
        # the element of diagonal
        s = []
        i = row
        k = j
        while (i < n and k >= 0):
            s.append(mat[i][k])
            i += 1
            k -= 1

        # push all element back to matrix
        # in reverse order
        i = row
        k = j
        while (i < n and k >= 0):
            mat[i][k] = s[-1]
            k -= 1
            i += 1
            s.pop()

    # do the same process for all the
    # diagonal which start from last
    # column
    column = n - 1
    for j in range(1, n):

        # here we use stack for reversing
        # the elements of diagonal
        s = []
        i = j
        k = column
        while (i < n and k >= 0):
            s.append(mat[i][k])
            i += 1
            k -= 1

        # push all element back to matrix
        # in reverse order
        i = j
        k = column
        while (i < n and k >= 0):
            mat[i][k] = s[-1]
            i += 1
            k -= 1
            s.pop()

distances = [
    ["-",7,4,float('inf'),float('inf'),float('inf'),float('inf'),float('inf'),float('inf'),float('inf')],
    [float('inf'),"-",float('inf'),2,4,float('inf'),float('inf'),float('inf'),float('inf'),float('inf')],
    [float('inf'),float('inf'),"-",float('inf'),4,6,float('inf'),float('inf'),float('inf'),float('inf')],
    [float('inf'),float('inf'),float('inf'),"-",float('inf'),float('inf'),8,5,float('inf'),float('inf')],
    [float('inf'),float('inf'),float('inf'),float('inf'),"-",float('inf'),float('inf'),5,9,float('inf')],
    [float('inf'),float('inf'),float('inf'),float('inf'),float('inf'),"-",float('inf'),float('inf'),9,3],
    [float('inf'),float('inf'),float('inf'),float('inf'),float('inf'),float('inf'),"-",float('inf'),float('inf'),float('inf')],
    [float('inf'),float('inf'),float('inf'),float('inf'),float('inf'),float('inf'),float('inf'),"-",float('inf'),float('inf')],
    [float('inf'),float('inf'),float('inf'),float('inf'),float('inf'),float('inf'),float('inf'),float('inf'),"-",float('inf')],
    [float('inf'),float('inf'),float('inf'),float('inf'),float('inf'),float('inf'),float('inf'),float('inf'),float('inf'),"-"]
]
distances = imageSwap(distances,10)
for i in range(len(distances)):
    row = distances[i]
    for j in range(len(row)):
        if row[j] != "-" and row[j] != float('inf'):
            distances[i][j] *= 1
    
prettyPrint(distances)

for k in range(len(distances)):
    row = distances[k]
    column = getColumn(distances,k)
    for i in range(len(distances)):
        for j in range(len(distances)):
            if i != k and j != k and distances[i][j] != "-":
                sum = row[i] + column[j]
                if sum < distances[i][j]:
                    distances[i][j] = sum
prettyPrint(distances)
