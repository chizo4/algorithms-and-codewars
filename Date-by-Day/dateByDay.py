# Written by: Filip J. Cierkosz
# Date: 07/2021

import datetime

# Function to determine the date by day number and boolean defining it is leap.
def getDate(day, isLeap):
    # Dictionary of months.
    months = {1:'January', 2:'February', 3:'March', 4:'April', 5:'May', 6:'June',
              7:'July', 8:'August', 9:'September', 10:'October', 11:'November', 12:'December'}
    
    # Return the date for a leap year.
    if (isLeap):
        date = datetime.datetime.strptime('2020'+'-'+f'{day}', '%Y-%j').strftime('%m, %d')
        return f'{months[int(date[:2])]}, {int(date[-2:])}'
    # Return the date for a non-leap year.
    else:
        date = datetime.datetime.strptime(str(day), '%j').strftime('%m, %d')
        return f'{months[int(date[:2])]}, {int(date[-2:])}'

# Test harness.
print(getDate(41, False))     # returns 'February, 10'
print(getDate(60, False))     # returns 'March, 1'
print(getDate(60, True))      # returns 'February, 29'
print(getDate(365, False))    # returns 'December, 31'
print(getDate(100, True))     # returns 'April 9'
print(getDate(366, True))     # returns 'December, 31'
