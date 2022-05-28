'''
Simple vector operations.

vector_ops.py

Date created: 06/2021

Date edited: 01/2022

Author: Filip J. Cierkosz
'''

import numpy as np

class Vector:
    # Class constructor.
    def __init__(self, input_vals):
        self.vals = np.array(input_vals)
        self.length = np.array(input_vals).size

    # Method 1: Display the vector object as a string.
    def __str__(self):
        return f'{self.vals}'.replace('[', '(').replace(']', ')')

    # Method 2: Check if two vectors are equal.
    def check_if_equal(self, other):
        return (self.vals==other.vals).all()

    # Method 3: Check if two vectors have the same size.
    def check_size(self, other):
        return self.length==other.length

    # Method 4: Addition.
    def add(self, other):
        # The operation can be executed if vectors have the same size.
        if (self.check_size(other)):
            v = (self.vals).__add__(other.vals)
            return Vector(v)
        else:
            raise Exception('An error occurred while attempting to perform addition!')

    # Method 5: Subtraction.
    def subtract(self, other):
        # The operation can be executed if vectors have the same size.
        if (self.check_size(other)):
            v = (self.vals).__sub__(other.vals)
            return Vector(v)
        else:
            raise Exception('An error occurred while attempting to perform subtraction!')

    # Method 6: Dot product.
    def dot(self, other):
        if (self.check_size(other)):
            v = (self.vals).__mul__(other.vals)
            return Vector(v)
        else:
            raise Exception('An error occurred while attempting to calculate the dot product!')

    # Method 7: Norm.
    norm = lambda self: np.linalg.norm(self.vals)

# Test harness.
def main():
    vec_one = Vector([1, 2, 3])
    vec_two = Vector([4, 5, 6])
    print(vec_one)
    print(vec_two)

    # Compare vectors.
    print(vec_one.check_if_equal(vec_two))

    # Perform calculations.
    print(vec_one.add(vec_two))
    print(vec_one.subtract(vec_two))
    print(vec_one.dot(vec_two))
    print(vec_one.norm())
    print(vec_two.norm())

# Run the tests.
if (__name__=='__main__'):
    main()
