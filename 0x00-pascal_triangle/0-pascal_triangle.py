#!/usr/bin/python3
"""This script generates Pascal's triangle for a given number of rows."""


def pascal_triangle(n):
    """
    Generates Pascal's triangle up to the nth row.
    
    Args:
        n (int): The number of rows of Pascal's triangle to generate.
        
    Returns:
        List[List[int]]: A list of lists where each sublist represents a row
    """


    triangle_list = []

    if n <= 0:
        return triangle_list

    for row in range(n):
        current_row = []

        for col in range(row + 1):
            if col == 0 or col == row:
                current_row.append(1)
            else:
                current_row.append(triangle_list[row - 1][col - 1] + triangle_list[row - 1][col])
                
        triangle_list.append(current_row)

    return triangle_list
