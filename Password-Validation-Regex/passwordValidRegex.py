'''
Date: 07/2021

@author Filip J. Cierkosz
'''

import re

# Function to validate a password using regular expression.
# The password has to be at least 6-character long, with at least
# one uppercase letter, one lowercase letter, and one digit.
# It cannot contain any special signs.
def validPassword(pswrd):
    # Regex pattern.
    regex = "^(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9])[A-Za-z0-9]{6,}$"

    # Check if the input matches the pattern.
    matches = re.findall(regex, pswrd)

    # If there are any matches, the password is valid.
    if (len(matches)==1): return True
    
    # Otherwise, the input password is not valid.
    return False