#!/usr/bin/python3
"""perimeter of an island"""


def island_perimeter(grid):
    '''returns island perimeter'''
    perimeter = 0
    for rw in range(len(grid)):
        for cn in range(len(grid[rw])):
            if grid[rw][cn] == 1:
                if rw - 1 < 0 or grid[rw - 1][cn] == 0:
                    perimeter += 1
                if cn - 1 < 0 or grid[rw][cn - 1] == 0:
                    perimeter += 1
                if cn + 1 >= len(grid[rw]) or grid[rw][cn + 1] == 0:
                    perimeter += 1
                if rw + 1 >= len(grid) or grid[rw + 1][cn] == 0:
                    perimeter += 1
    return perimeter

