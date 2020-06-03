#!/usr/bin/python3
"""
Write to a file
"""


def append_write(filename="", text=""):
    """function that appends a string at the end of a text file
    (UTF8) and returns the number of characters added
    """
    with open(filename, mode="a", encoding="UTF-8") as af:
        af.write(text)
        return len(text)
