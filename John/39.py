'''
Probelm 39
If p is the perimeter of a right angle triangle with integral length sides, {a,b,c}, there are exactly three solution for p = 120.
{20,48,52},{24,45,51},{30,40,50}
For which value of p <= 1000, is the number of solutions maximised?
'''

solutions = {}
for a in range(1,500):
    for b in range(a,500):
        c = (a**2+b**2)**0.5
        if c == int(c):
            p = int(a+b+c)
            if p in solutions.keys():
                solutions[p] += 1
            else:
                solutions[p] = 1
maxP = 0
maxSolutions = 0
for key,val in solutions.items():
    if val > maxSolutions:
        maxSolutions = val
        maxP = key
print(maxP)
