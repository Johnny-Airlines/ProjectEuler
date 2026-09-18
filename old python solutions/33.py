'''
Problem 33
The fraction 49/98 is a curios fraction, as it could be correctly incorrectly simplified by cancelling the 9's to give 4/8, which is correct.
We shall consider fractions like, 30/50 = 3/5, to be trivial examples.
The are exactly 4 non-trivial examples of this type of fraction, less than one in value, and containing two digits in the numerator and denominator.
If the product of these four fractions is given in its lowest common terms, find the value of the denominator.
'''

def simplify(a,b):
    for i in range(a+1,2,-1):
        if a % i == 0 and b % i == 0:
            a /= i
            b /= i
    return (a,b)

productA = 1
productB = 1
for a in range(10,100):
    for b in range(a+1,100):
        if str(a)[1] != "0" and str(b)[1] != "0":
            commonDigit = False
            if str(a)[0] in str(b):
                commonDigit = str(a)[0]
            elif str(a)[1] in str(b):
                commonDigit = str(a)[1]
            if commonDigit:
                aCancelledList = list(str(a))
                bCancelledList = list(str(b))
                aCancelledList.remove(commonDigit)
                bCancelledList.remove(commonDigit)
                aCancelled = int("".join(aCancelledList))
                bCancelled = int("".join(bCancelledList))
                if a/b == aCancelled/bCancelled:
                    print(a,b,aCancelled,bCancelled)
                    productA *= a
                    productB *= b
             
productA,productB = simplify(productA,productB)
print(int(productB))
