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
distances = [[float('-inf') if j==float('inf') else (j * 1 if j != "-" else "-" )for j in i] for i in distances]
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
                if sum > distances[j][i]:
                    distances[j][i] = sum
prettyPrint(distances)
distances[0].remove("-")
print(max(distances[0]))
