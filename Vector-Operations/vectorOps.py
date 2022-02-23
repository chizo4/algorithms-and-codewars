'''
Date created: 06/2021

Date edited: 01/2022

@author Filip J. Cierkosz
'''

import numpy as np

#~~~~~~~~~~VECTOR CLASS~~~~~~~~~~
class Vector:
    #~~~~~~~~~~CONSTRUCTOR~~~~~~~~~~
    # Initialize a vector class instance.
    def __init__(self, inputVals):
        self.vals = np.array(inputVals)
        self.length = np.array(inputVals).size

    #~~~~~~~~~~METHODS~~~~~~~~~~
    # Method 1: Display the vector object as a string.
    def __str__(self):
        return f'{self.vals}'.replace('[', '(').replace(']', ')')

    # Method 2: Check if two vectors are equal.
    def checkIfEqual(self, other):
        return (self.vals==other.vals).all()

    # Method 3: Check if two vectors have the same size.
    def checkSize(self, other):
        return self.length==other.length

    # Method 4: Addition.
    def add(self, other):
        # The operation can be executed if vectors have the same size.
        if (self.checkSize(other)):
            v = (self.vals).__add__(other.vals)
            return Vector(v)
        # Otherwise, raise an exception.
        else:
            raise Exception('An error occurred while attempting to perform addition!')

    # Method 5: Subtraction.
    def subtract(self, other):
        # The operation can be executed if vectors have the same size.
        if (self.checkSize(other)):
            v = (self.vals).__sub__(other.vals)
            return Vector(v)
        # Otherwise, raise an exception.
        else:
            raise Exception('An error occurred while attempting to perform subtraction!')

    # Method 6: Dot product.
    def dot(self, other):
        if (self.checkSize(other)):
            v = (self.vals).__mul__(other.vals)
            return Vector(v)
        # Otherwise, raise an exception.
        else:
            raise Exception('An error occurred while attempting to calculate the dot product!')

    # Method 7: Norm.
    norm = lambda self: np.linalg.norm(self.vals)

# Test harness.
def main():
    # Initialize two vectors.
    vecOne = Vector([1, 2, 3])
    vecTwo = Vector([4, 5, 6])

    # Print vectors.
    print(vecOne)
    print(vecTwo)

    # Compare vectors.
    print(vecOne.checkIfEqual(vecTwo))

    # Perform calculations.
    print(vecOne.add(vecTwo))
    print(vecOne.subtract(vecTwo))
    print(vecOne.dot(vecTwo))
    print(vecOne.norm())
    print(vecTwo.norm())

# Run the tests.
main()
