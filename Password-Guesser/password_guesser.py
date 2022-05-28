'''
Please note: The purpose of creating this program is not 
to promote any kind of illegal practice.

password_guesser.py

Date: 12/2021

Author: Filip J. Cierkosz
'''

from hashlib import sha1
from string import ascii_lowercase
from itertools import product

# Function to crack a password which consists of lowercase letters 
# and has length 1-n (where n>1).
def password_cracker(hash, n):
    # Iterate through different lengths to create possible guesses.
    for i in range(1, n+1):
        for i in product(ascii_lowercase, repeat=i):
            guess = ''.join(i)

            # Create a SHA1 hash object.
            hex_guess = sha1(guess.encode()).hexdigest()

            # Compare the created hash with the argument of the function. 
            # If they match, return the decoded password.
            if (hex_guess==hash): return guess

    # Otherwise, there are no matches.
    return 'There are no matches to the hash.'
