#!/usr/bin/python3

"""Defines a Pascal triangle function"""


def pascal_triangle(n):
    """
    Generate Pascal's triangle of n.
    Args:
        n (int): The number of rows in the triangle.
    Returns:
        list: List of lists representing Pascal's triangle.
    """
    triangle = []
    if n <= 0:
        return triangle

    # Generate each row of the triangle
    for i in range(n):
        row = [1]  # First element of each row is always 1
        if i > 0:
            # Calculate remaining elements of the row based on the previous row
            prev_row = triangle[i - 1]
            for j in range(len(prev_row) - 1):
                row.append(prev_row[j] + prev_row[j + 1])
            row.append(1)  # Last element of each row is always 1
        triangle.append(row)

    return triangle
