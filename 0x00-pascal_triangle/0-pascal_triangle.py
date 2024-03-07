#!/usr/bin/python3


def pascal_triangle(n):
    if n <= 0:
        return []

    triangle = []

    for row in range(n):
        current_row = []
        for col in range(row + 1):
            if col == 0 or col == row:
                current_row.append(1)
            else:
                # Calculate element using combination formula
                element = triangle[row - 1][col - 1] + triangle[row - 1][col]
                current_row.append(element)
        triangle.append(current_row)

    return triangle

def print_triangle(triangle):
    for row in triangle:
        print("[{}]".format(",".join(map(str, row))))

if __name__ == "__main__":
    triangle = pascal_triangle(5)
    print_triangle(triangle)
