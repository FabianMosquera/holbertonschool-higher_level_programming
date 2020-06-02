#!/usr/bin/python3
"""
My integer
"""


class MyInt(int):
    """MyInt that inherits from int
    """
    def __eq__(self, value):
        """ equal (=) inverted
        """
        return super().__ne__(value)

    def __ne__(self, value):
        """ not equal (!=) inverted
        """
        return super().__eq__(value)
