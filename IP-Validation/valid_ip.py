'''
valid_ip.py

Date: 02/2022

Author: Filip J. Cierkosz
'''

from re import search

# An IP address is said to be valid if it has a structure:
# n.n.n.n where 0 <= n <= 255. The function to check if a
# given IP address is valid using regex pattern.
def check_ip_validity(ip):
    # Pattern to detect n.n.n.n where 0 <= n <= 999.
    pattern = '[\d]{1,3}\.[\d]{1,3}\.[\d]{1,3}\.[\d]{1,3}$'

    # If IP matches the pattern, then check if each of its 
    # numbers is in the desired range: 0 <= n <= 255. If so,
    # the address is valid and so return True.
    if (search(pattern, ip) and len([n for n in ip.split('.') if 0<=int(n)<256])==4):
        return True

    # Otherwise, IP is NOT valid, i.e. return False.
    return False
