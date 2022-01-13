# Written by: Filip J. Cierkosz
# Date: 11/2021

# Function to turn string input into hash.
def str_to_hash(s):
    s = s.replace("=", " ").replace(",", " ")
    arrChars = [c for c in s.split() if c.isalpha()]
    arrInts = [int(d) for d in s.split() if d.isdigit()]
    return dict(zip(arrChars, arrInts))