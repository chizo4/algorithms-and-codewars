'''
hashing_alternative.py

Date: 11/2021

Author: Filip J. Cierkosz
'''

# Function to turn string input into hash.
def str_to_hash(s):
    s = s.replace("=", " ").replace(",", " ")
    arr_chars = [c for c in s.split() if c.isalpha()]
    arr_ints = [int(d) for d in s.split() if d.isdigit()]
    return dict(zip(arr_chars, arr_ints))