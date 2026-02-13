import time

lengths = {
    1: "one",
    2: "two",
    3: "three",
    4: "four",
    5: "five",
    6: "six",
    7: "seven",
    8: "eight",
    9: "nine",
    20: "twenty",
    30: "thirty",
    40: "forty",
    50: "fifty",
    60: "sixty",
    70: "seventy",
    80: "eighty",
    90: "ninety"
}

otherLengths = {
    0: "ten",
    1: "eleven",
    2: "twelve",
    3: "thirteen",
    4: "fourteen",
    5: "fifteen",
    6: "sixteen",
    7: "seventeen",
    8: "eighteen",
    9: "nineteen",
}

def translate(i):
    if i == 1000:
        print("onethousand")
        return "onethousand"

    word = ""
    ones = int(str(i)[-1])
    if i > 9:
        tens = int(str(i)[-2])
        if i > 99:
            hundreds = int(str(i)[-3])
            word += lengths[hundreds]
            word += "Hundred"
            if ones != 0 or tens != 0:
                word += "And"
        if tens == 1:
            word += otherLengths[ones]
        else:
            if tens != 0:
                word += lengths[tens * 10]
            if ones != 0:
                word += lengths[ones]
    else:
        word += lengths[ones]
    print(word)
    return(word)

sum = 0
for i in range(1,1001):
        #time.sleep(0.01)
    word = translate(i)
    sum += len(word) 

print(sum)
