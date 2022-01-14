# Written by: Filip J. Cierkosz
# Date: 06/2021

from math import pow, sqrt

#~~~~~~~~~~VECTOR CLASS~~~~~~~~~~
class Vector:
    #~~~~~~~~~~CONSTRUCTOR~~~~~~~~~~
    # Initialize a vector class instance.
    def __init__(self, inputElements):
        self.elements = list(inputElements)

    #~~~~~~~~~~METHODS~~~~~~~~~~
    # ADDITIONAL METHODS
    # 1. Check if two vectors that are supposed to have the same values are equal
    def equals(self, other):
        return self.elements == other.elements

    # 2. Return the output as a string
    def __str__(self):
        self.elements = str(tuple(self.elements)).replace(" ", "")
        return self.elements
        
    # 1. ADD
    def add(self, other):

        # The operation is executed if lengths of inputElements' lists match
        if len(self.elements) == len(other.elements):

            # Store elements
            v = list(self.elements)

            # Adding elements of the second vector
            for i, el in enumerate(other.elements, 0):
                v[i] += el

            # Return a new Vector object defined by the inputElements arguments
            return Vector(v)

        # Exception if the lengths of inputElements do not match
        else:
            raise Exception("An error occurred and so it is impossible to execute the operation!")

    # 2. SUBTRACT
    def subtract(self, other):

        # The operation is executed if lengths of inputElements' lists match
        if len(self.elements) == len(other.elements):

            # Store elements
            v = list(self.elements)

            # Subtracting elements of the second vector
            for i, el in enumerate(other.elements, 0):
                v[i] -= el

            # Return a new Vector object defined by the inputElements arguments
            return Vector(v)

        # Exception if the lengths of inputElements' lists do not match
        else:
            raise Exception("An error occurred and so it is impossible to execute the operation!")

    # 3. DOT
    def dot(self, other):

        # The operation is executed if lengths of inputElements' lists match
        if len(self.elements) == len(other.elements):

            # Store elements
            product = 0
            v = list(self.elements)

            # Multiplying elements and incrementing the product value
            for i, el in enumerate(other.elements, 0):
                product += (v[i] * el)

            # Return the dot product value
            return product

        # Exception if the lengths of inputElements' lists do not match
        else:
            raise Exception("An error occurred and so it is impossible to execute the operation!")

    # 4. NORM
    def norm(self):

        # Store elements
        temp = 0
        v = list(self.elements)

        for i in range(len(v)):
            temp += pow(v[i], 2)

        norm = sqrt(temp)

        # Return the norm value
        return norm

    

# Test harness.
def main():
    # Initialize two vectors.
    vecOne = Vector((1, 2, 3))
    vecTwo = Vector((3, 4, 5))

    print(vecOne.add(vecTwo))
    print(vecOne.subtract(vecTwo))
    print(vecOne.dot(vecTwo))
    print(vecOne.norm())

main()