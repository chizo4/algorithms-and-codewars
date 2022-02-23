'''
Date: 11/2021

@author Filip J. Cierkosz
'''

# Function to count the number of a character in a string 
# implementing lambda and dictionary comprehension.
count = lambda s: {c: s.count(c) for c in s.replace(' ', '')}

# Test harness.
print(count('this is just a test'))
print(count("knjsvksv sjdjnvikjvns vjnsf vksnv snjfmv skjvjfsnvf"))
print(count('aaaaaBBBaaaaaaaCCCCCCaaa'))