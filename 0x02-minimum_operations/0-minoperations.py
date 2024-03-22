#!/usr/bin/python3
def minOperations(n: int) -> int:
    """
    Calculate the minimum number of operations needed to obtain 'n' H characters.
    """
    if n <= 1:
        return 0
    
    operations = 0
    copied_chars = 'H'  # Initially, there's only one 'H' in the text file
    
    while len(copied_chars) < n:
        if n % len(copied_chars) == 0:
            # If the current length of the string is a factor of n, we can double the string
            operations += 2
            copied_chars *= 2
        else:
            # Otherwise, we append the content already in the text file
            operations += 1
            copied_chars += copied_chars
    
    # If the final length of the string matches n, return the number of operations
    if len(copied_chars) == n:
        return operations
    else:
        return 0  # If it's impossible to achieve 'n' characters, return 0