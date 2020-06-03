#!/usr/bin/python3
"""
Number of lines
"""


def number_of_lines(filename=""):
    """function that returns the number of lines of a text file
    """
    with open(filename, encoding="UTF-8") as r:
        n_lines = 0
        for i in r:
            n_lines += 1
        return n_lines
