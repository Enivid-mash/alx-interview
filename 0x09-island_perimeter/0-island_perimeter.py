#!/usr/bin/python3
"""Calculate Island Perimeter - ALX Interview Task"""

def is_water_or_boundary(cell):
    """
    Check if the given cell is either water (0) or out of grid bounds.

    Args:
        cell (int): Cell value from the grid, should be either 0 (water) or 1 (land).

    Returns:
        int: Returns 1 if the cell is water or out of bounds, otherwise 0.
    """
    if cell == 0:
        return 1
    return 0

def island_perimeter(grid):
    """
    Computes the perimeter of the island represented by 1s in a grid.

    Args:
        grid (list of list of int): A 2D list representing the grid where 1 indicates land and 0 indicates water.

    Returns:
        int: The total perimeter of the island.
    """
    rows = len(grid)
    cols = len(grid[0])
    assert (1 <= rows <= 100 and 1 <= cols <= 100), "Grid dimensions must be between 1 and 100"

    perimeter = 0
    for i in range(rows):
        for j in range(cols):
            assert grid[i][j] in [0, 1], "Grid values must be either 0 (water) or 1 (land)"
            if grid[i][j] == 1:
                # Check above
                if i - 1 < 0:
                    perimeter += 1
                else:
                    perimeter += is_water_or_boundary(grid[i-1][j])

                # Check left
                if j - 1 < 0:
                    perimeter += 1
                else:
                    perimeter += is_water_or_boundary(grid[i][j-1])

                # Check below
                try:
                    perimeter += is_water_or_boundary(grid[i+1][j])
                except IndexError:
                    perimeter += 1

                # Check right
                try:
                    perimeter += is_water_or_boundary(grid[i][j+1])
                except IndexError:
                    perimeter += 1

    return perimeter

