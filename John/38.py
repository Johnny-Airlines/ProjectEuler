'''
Problem 38
An n-digit number is pandigital if it makes use of all the digits 1 to n exactly once; for example, the 5-digit number, 15234, is 1 through 5 pandigital.

By concatatenating each product of 192 * (1,2,3), we get the 1 to 9 pandigital, 192384576. We will call 192384576 the concatenated product of 192 and (1,2,3).
The same can be achieved by starting with 9 and multiplying by 1,2,3,4,5 , giving the pandigital 918273645, which is the concatatenated product of 9 and (1,2,3,4,5).
What is the largest 1 to 9 pandigital 9-digit number that can be formed as the concatenated product of an integer with (1,2,...,n) where n > 1?
'''
max = 0
for i in range(9999):
    products = []
    n = 1
    while len("".join(products)) < 9:
        products.append(str(i*n))
        n += 1
    if len("".join(products)) == 9:
        product = "".join(products)
        if len(list(product)) == len(set(product)) and not "0" in list(product):
            if int(product) > max:
                max = int(product)

print(max)
