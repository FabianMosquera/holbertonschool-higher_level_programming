#!/usr/bin/python3
"""
Read n lines
"""


def read_lines(filename="", nb_lines=0):
    """function that reads n lines of a text file (UTF8) and print
    """
    count = 0
    with open(filename, encoding="UTF-8") as r:
        while True:
            line = r.readline()
            count += 1
            print(line, end="")
            if count >= nb_lines and nb_lines > 0:
                break
            if not line:
                break
