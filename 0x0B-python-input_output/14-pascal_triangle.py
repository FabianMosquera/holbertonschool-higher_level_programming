#!/usr/bin/python3
"""
Pascal's Triangle
"""


def pascal_triangle(n):
    """returns a list of lists of integers
    representing the Pascal’s triangle of n
    """
    if n <= 0:
        return []
    new_list = []
    for i in range(n):
        if i == 0:
            new_list.append([1])
            continue
        if i == 1:
            new_list.append([1, 1])
            continue
        row = []
        # init row
        for j in range(i + 1):
            row.append(j)
        for j in range(1, i):
            row[0] = 1
            row[i] = 1
            row[j] = new_list[i - 1][j] + new_list[i - 1][j - 1]
        new_list.append(row)
    return new_list