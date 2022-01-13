# Written by: Filip J. Cierkosz
# Date: 06/2021

import hashlib

# Function to guess 5-digit PIN.
def crack(inputHash):
    # Iterate through different digits.
    for i in range(10):
        for j in range(10):
            for k in range(10):
                for l in range(10):
                    for m in range(10):
                        # Combine a PIN from digits and hash it.
                        attemptedPIN = f'{i}{j}{k}{l}{m}'
                        testedHash = hashlib.md5(attemptedPIN.encode("utf-8")).hexdigest()
                        
                        # If the tested hash is the same as the input one,
                        # return the attempted PIN as the PIN has been guessed.
                        if (testedHash==inputHash): return attemptedPIN

# Test harness.
print(crack())