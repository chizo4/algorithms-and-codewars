'''
hashing.py

Date: 06/2021

Author: Filip J. Cierkosz
'''

import hashlib

# Function to turn an input string into an MD5 hash.
def str_to_hash(input_str):
    output_hash = hashlib.md5(input_str.encode("utf-8")).hexdigest()
    return output_hash

# Test harness.
print(str_to_hash('12345'))
