'''
Problem 40
An irrational decimal fraction is created by concatenating the postivie integers:
0.123456789101112131415161718192021...
             -
It can be seen that the 12th digit of the fractional part is 1.
If d subscript n represents the nth digit of the fractional part, find the value of the following expression.
d1*d10*d100*d1000*d10000*d100000*d1000000
'''

d = "".join([str(i) for i in range(1000000)])
print(int(d[1])*int(d[10])*int(d[100])*int(d[1000])*int(d[10000])*int(d[100000])*int(d[1000000]))
