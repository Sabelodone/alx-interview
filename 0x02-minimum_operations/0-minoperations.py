#!/usr/bin/python3
def minOperations(n: int) -> int:
    """
    Finds the minimum operations needed to result in exactly n H characters in a file
    """
    if n <= 1:
        return 0

    operations = 0
    current_chars = 1
    clipboard = 0

    while current_chars < n:
        if n % current_chars == 0:  # If current characters evenly divides n
            clipboard = current_chars
            current_chars += clipboard
            operations += 1
        else:
            current_chars += clipboard
            operations += 1

    return operations
