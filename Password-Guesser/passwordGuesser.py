'''
Date: 12/2021

@author Filip J. Cierkosz
'''

# Please note: The purpose of creating this program is not to promote
# any kind of illegal practice.

from hashlib import sha1
from string import ascii_lowercase
from itertools import product

# Function to crack a password which consists of lowercase letters 
# and has length 1-n (where n>1).
def passwordCracker(hash, n):
    # Iterate through different lengths to create possible guesses.
    for i in range(1, n+1):
        for i in product(ascii_lowercase, repeat=i):
            guess = ''.join(i)

            # Create a SHA1 hash object.
            hexGuess = sha1(guess.encode()).hexdigest()

            # Compare the created hash with the argument of the function. 
            # If they match, return the decoded password.
            if (hexGuess==hash): return guess

    # Otherwise, there are no matches.
    return 'There are no matches to the hash.'

# Test harness.
# Create SHA1 hash objects.
hashOne = sha1('tests'.encode()).hexdigest()
hashTwo = sha1('fuc'.encode()).hexdigest()
hashThree = sha1('tests'.encode()).hexdigest()
hashFour = sha1('longer'.encode()).hexdigest()

# Test the algorithm.
print(passwordCracker(hashOne, 6))      # return: 'tests'
print(passwordCracker(hashTwo, 4))      # return: 'fuc'
print(passwordCracker(hashThree, 2))    # return: 'There are no matches to the hash.'
print(passwordCracker(hashFour, 7))     # return: 'longer'