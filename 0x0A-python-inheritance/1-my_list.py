#!/usr/bin/python3
"""
My list
"""


class MyList(list):
    """Contains list
    """
    def print_sorted(self):
        """prints the list, but sorted
        """
        print(sorted(self))
