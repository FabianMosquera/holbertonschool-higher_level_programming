#!/usr/bin/python3
"""
My integer
"""


class MyInt(int):
    """MyInt that inherits from int
    """
    def __equal__(self, value):
        """ equal (=) inverted
        """
        return False

    def __nequal__(self, value):
        """ not equal (!=) inverted
        """
        return True
