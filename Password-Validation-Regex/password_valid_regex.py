'''
Function to validate a password using regular expression.
The password has to be at least 6-character long, with at 
least one uppercase letter, one lowercase letter, and one 
digit. It cannot contain any special signs.

python_valid_regex.py

Date: 07/2021

Author: Filip J. Cierkosz
'''

import re

def valid_password(pswrd):
    pattern = '^(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9])[A-Za-z0-9]{6,}$'
    matches = re.findall(pattern, pswrd)

    if (len(matches)==1): 
        return True
    
    return False
