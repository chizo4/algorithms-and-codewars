# Written by: Filip J. Cierkosz
# Date: 02/2022

# General Idea
# Convert time in seconds to human readable time in form:
# 'y year(s), d day(s), h hour(s), m minute(s) and s second(s).'
# Let's assume that a year has 365 days.

from random import randint

# Function 1: Check if the time unit keyword is plural i.e. 
# with 's'), or not.
checkIfPl = lambda val: 's' if (val>1) else ''

# Function 2: Convert seconds to human readable time.
def getHumanReadableTime(sec):
    # If the sec eqauls zero, return 'now'.
    if (sec==0): return 'now'

    # Determine value of seconds, minutes, hours, days, years.
    m, s = divmod(sec, 60)
    h, m = divmod(m, 60)
    d, h = divmod(h, 24)
    y, d = divmod(d, 365)

    # Create a dictionary to store values corresponding with the
    # name of the time unit. Then, using dictionary comprehension,
    # remove the items which value is equal to 0. 
    timeDict = {'year': y, 'day': d, 'hour': h, 'minute': m, 'second': s}
    timeDict = {key: val for key, val in timeDict.items() if (val>0)}

    # Initialize the output string.
    humanReadTime = ''

    # Iterate through the keys and indexes of the dictionary in
    # order to prepare the final expression.
    for i, key in enumerate(timeDict):
        if (i==len(timeDict)-1):
            humanReadTime += f'{timeDict[key]} {key}{checkIfPl(timeDict[key])}.'
        elif (i==len(timeDict)-2):
            humanReadTime += f'{timeDict[key]} {key}{checkIfPl(timeDict[key])} and '
        else: 
            humanReadTime += f'{timeDict[key]} {key}{checkIfPl(timeDict[key])}, '

    # Return the final output string.
    return humanReadTime

# Function 3: Invoke the function on 10 random integers 1-1000000000.
def main():
    # Iterate and test.
    for i in range(10):
        currInt = randint(1,1000000000)
        print(f'{currInt} seconds is equivalent to:')
        print(getHumanReadableTime(currInt))

# Test harness.
if (__name__=='__main__'): main()
