'''
A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.
1 Jan 1900 was a Monday
Thirty days has September,
April, June and November.
All the rest have thirty-one,
Saving February alone,
Which has twenty-eight, rain or shine.
And on leap years, twenty-nine.
How many Sunday fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?
'''

months = [31,28,31,30,31,30,31,31,30,31,30,31]
monthsLeapYear = [31,29,31,30,31,30,31,31,30,31,30,31]
year = 1900
all = []
while year < 2002:
    if year % 4 == 0:
        if year % 400 == 0 or year % 100 != 0:
            all += monthsLeapYear
    else:
        all += months
    year += 1
cumulative = [all[0]]
for i in range(1,len(all)):
    cumulative.append(cumulative[i-1]+all[i])
cumulativeMod = [i%7 for i in cumulative][12:]
sum = 0
for i in range(len(cumulativeMod)):
    if cumulativeMod[i] == 0 :
        sum += 1
print(sum)
