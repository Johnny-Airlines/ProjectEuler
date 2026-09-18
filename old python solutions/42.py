'''
Problem 42
By converting each letter in a word to a number corresponding to its alphabetical position and adding these values we form a word value. For example, the wor value for SKY is 19+11+25=55=10th triangle number. If the word value is a triangle number then we shall call the word a triangle word.
Using words.txt, a 16K text file containing nearly two-thousand common English words, how many are triangle words?
'''

alphabet = "abcdefghijklmnopqrstuvwxyz".upper()

def wordValue(word):
    value = 0
    for letter in word:
        value += alphabet.index(letter)+1
    return value

def isTriangleNumber(t):
    t *= 2
    n = int(t**0.5)
    return n*(n+1)==t

with open("./resources/0042_words.txt","r") as f:
    words = f.read()
words = words.split(",")
words = [word.replace('"','') for word in words]

count = 0
for word in words:
    if isTriangleNumber(wordValue(word)):
        count += 1
print(count)
