#!/usr/bin/python3
"""
    Calculates the minimum number of operations needed to obtain 'n' H characters.
    
    Parameters:
        n (int): The target number of H characters.
        
    Returns:
        int: The minimum number of operations needed.
            Returns 0 if it's impossible to achieve 'n' H characters.
    """
    next_char = 'H'  # The next character to append
    copied_chars = 'H'  # Initially, there's only one 'H' in the text file
    operations = 0  # Count of operations performed
    
    while len(copied_chars) < n:
        if n % len(copied_chars) == 0:
            # If the current length of the string is a factor of n, we can double the string
            operations += 2
            next_char = copied_chars  # Update the next character to append
            copied_chars *= 2  # Double the string
        else:
            # Otherwise, we append the content already in the text file
            operations += 1
            copied_chars += next_char
    
    # If the final length of the string matches n, return the number of operations
    if len(copied_chars) == n:
        return operations
    else:
        return 0  # If it's impossible to achieve 'n' characters, return 0