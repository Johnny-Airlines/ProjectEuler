'''
Problem 31
How many different ways can £2 be made using any number of coins?

Forgive me, for in this solution I have sinned - 6 for loops each nested and 7 levels of indentation
'''

count = 1
for pounds in range(int(200/100)+1+1):
    for fifties in range(int(200/50)+1+1):
        for twenties in range(int(200/20)+1+1):
            for tens in range(int(200/10)+1+1):
                for fives in range(int(200/5)+1+1):
                    for twos in range(int(200/2)+1+1):
                        total = pounds*100+fifties*50+twenties*20+tens*10+fives*5+twos*2
                        if total <= 200:
                            print(total,pounds,fifties,twenties,tens,fives,twos)
                            count += 1

print(count)
