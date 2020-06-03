#!/usr/bin/python3
"""
Read file
"""


def read_file(filename=""):
    """function that reads a text file (UTF8)
    """
    with open(filename, encoding="UTF-8") as r:
        print(r.read(), end="")
