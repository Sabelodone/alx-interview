#!/usr/bin/python3
"""Returns a Pascal triangle"""


def pascal_triangle(n):
    """
    Returns a list of lists representing Pascal's triangle up to the nth row.
    """

    if n <= 0:
        return []

    pascal = [[1]]
    if n == 1:
        return pascal

    for i in range(1, n):
        row = [1]
        for j in range(1, i):
            num = pascal[i - 1][j - 1] + pascal[i - 1][j]
            row.append(num)
        row.append(1)
        pascal.append(row)

    return pascal
