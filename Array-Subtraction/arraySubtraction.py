# Written by: Filip J. Cierkosz
# Date: 05/2021

# Function to subtract one list from another.
def arraySubtract(one, two):
    # Initialize the difference array.
    diff = []

    # Iterate through the elements of array one.
    for el in one:
        # If it is not detected in arra two, append it in diff.
        if (not el in two):
            diff.append(el)

    # Return the resultant array.
    return diff

# Test harness.
print(arraySubtract([1,2,2,3,3,4,6,6,6],[1,3,2,4]))