'''
Convert time in seconds to human readable time in form:
'y year(s), d day(s), h hour(s), m minute(s) and s second(s).'
Let's assume that a year has 365 days.

human_read_time.py

Date: 02/2022

Author: Filip J. Cierkosz
'''

from random import randint

# Function 1: Check if the time unit keyword is plural i.e. 
# with 's'), or not.
check_if_plural = lambda val: 's' if (val>1) else ''

# Function 2: Convert seconds to human readable time.
def get_human_readable_time(sec):
    if (sec==0):
        return 'now'

    m, s = divmod(sec, 60)
    h, m = divmod(m, 60)
    d, h = divmod(h, 24)
    y, d = divmod(d, 365)

    # Create a dictionary to store values corresponding with the
    # name of the time unit. Then, using dictionary comprehension,
    # remove the items which value is equal to 0. 
    time_dict = {'year': y, 'day': d, 'hour': h, 'minute': m, 'second': s}
    time_dict = {key: val for key, val in time_dict.items() if (val>0)}

    human_read_time = ''

    for i, key in enumerate(time_dict):
        if (i==len(time_dict)-1):
            human_read_time += f'{time_dict[key]} {key}{check_if_plural(time_dict[key])}.'
        elif (i==len(time_dict)-2):
            human_read_time += f'{time_dict[key]} {key}{check_if_plural(time_dict[key])} and '
        else: 
            human_read_time += f'{time_dict[key]} {key}{check_if_plural(time_dict[key])}, '

    return human_read_time+'\n'

# Function 3: Invoke the function on 10 random integers 1-1000000000.
def main():
    for i in range(10):
        curr_int = randint(1,1000000000)
        print(f'{curr_int} seconds is equivalent to:')
        print(get_human_readable_time(curr_int))

# Test harness.
if (__name__=='__main__'): main()
