#!/usr/bin/python3
"""
Write to a file
"""


def write_file(filename="", text=""):
    """ function that writes a string to a text file
    (UTF8) and returns the number of characters written
    """
    with open(filename, mode="w", encoding="UTF-8") as wf:
        wf.write(text)
        return len(text)
