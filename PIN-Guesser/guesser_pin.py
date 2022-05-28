'''
Program to guess 5-digit PIN. 

guesser_pin.py

Date: 06/2021

Author: Filip J. Cierkosz
'''

import hashlib

def crack(input_hash):
    for i in range(10):
        for j in range(10):
            for k in range(10):
                for l in range(10):
                    for m in range(10):
                        # Combine a PIN from digits and hash it.
                        curr_pin = f'{i}{j}{k}{l}{m}'
                        tested_hash = hashlib.md5(curr_pin.encode("utf-8")).hexdigest()
                        
                        # If the tested hash is the same as the input one,
                        # return the attempted PIN as it has been guessed.
                        if (tested_hash==input_hash): 
                            return curr_pin
