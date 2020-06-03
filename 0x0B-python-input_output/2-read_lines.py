#!/usr/bin/python3
"""
Read n lines
"""


def read_lines(filename="", nb_lines=0):
    """function that reads n lines of a text file (UTF8) and print
    """
    count = 0
    with open(filename, encoding="UTF-8") as r:
        if nb_lines <= 0:
            print(r.read(), end="")
        for i in r:
            if count < nb_lines:
                print(count, end="")
                count += 1
