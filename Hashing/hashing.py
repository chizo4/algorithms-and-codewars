# Written by: Filip J. Cierkosz
# Date: 06/2021

import hashlib

# Function to turn an input string into an MD5 hash.
def strToHash(inputStr):
    outputHash = hashlib.md5(inputStr.encode("utf-8")).hexdigest()
    return outputHash

# Test harness.
print(strToHash("12345"))
