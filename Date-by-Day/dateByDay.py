# Written by: Filip J. Cierkosz
# Date: 07/2021

import datetime

# Function to determine 
def get_day(day, isLeap):
    dictMonths = {1:"January",2:"February",3:"March",4:"April",5:"May",6:"June",7:"July",8:"August",9:"September",10:"October",11:"November",12:"December"}

    if isLeap == True:
        date = datetime.datetime.strptime("2020" + "-" + f"{day}", "%Y-%j").strftime("%m, %d")
        return f"{dictMonths[int(date[:2])]}, {int(date[-2:])}"

    else:
        date = datetime.datetime.strptime(str(day), "%j").strftime("%m, %d")
        return f"{dictMonths[int(date[:2])]}, {int(date[-2:])}"

# Test harness.
print()