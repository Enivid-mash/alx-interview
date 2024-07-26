#!/usr/bin/python3
"""A script to determine Pascal's triangle for any number"""


def pascal_triangle(n):
    """
    returns a list of lists of integers representing the Pascal’s triangle of n
    """


    result = []

    if n <= 0:
        return result

    for row_index in range(n):
        row = [1] * (row_index + 1)
        for col_index in range(1, row_index):
            row[col_index] = result[row_index - 1][col_index - 1] +
                              result[row_index - 1][col_index]
        result.append(row)
        
    return result
