def getColumn(matrix,i):
    return [row[i] for row in matrix]

def prettyPrint(matrix):
    for row in matrix:
        print(row)

triangle = """3
7 4
2 4 6
8 5 9 3"""
badRows = triangle.split("\n")
rows = []
for row in badRows:
    row = row.split(" ")
    rows.append(row)
print(rows)
distances = [[9999999 for j in range(len(rows))] for i in range(len(rows))]
for i in range(len(rows)):
    row = rows[i]
    for j in range(len(row)):
        distance = row[j]
        print(j)
        distances[i][j] = int(distance) * -1
        if i == j:
            distances[i][j] = "-"
'''
distances = [
 ["-",7,5,10,float('inf')],
 [7,"-",4,17,3],
 [5,4,"-",6,float('inf')],
 [10,17,6,"-",3],
 [float('inf'),3,float('inf'),3,"-"]
]
'''
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
