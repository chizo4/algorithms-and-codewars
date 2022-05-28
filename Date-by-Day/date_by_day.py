'''
Function to determine the date by day number and boolean 
defining it is leap.

Date: 07/2021

Author: Filip J. Cierkosz
'''

import datetime

def get_date(day, is_leap):
    months = {1:'January', 2:'February', 3:'March', 4:'April', 5:'May', 6:'June',
              7:'July', 8:'August', 9:'September', 10:'October', 11:'November', 12:'December'}
    
    # Return the date for a leap year.
    if (is_leap):
        date = datetime.datetime.strptime('2020'+'-'+f'{day}', '%Y-%j').strftime('%m, %d')
        return f'{months[int(date[:2])]}, {int(date[-2:])}'
    # Return the date for a non-leap year.
    else:
        date = datetime.datetime.strptime(str(day), '%j').strftime('%m, %d')
        return f'{months[int(date[:2])]}, {int(date[-2:])}'
