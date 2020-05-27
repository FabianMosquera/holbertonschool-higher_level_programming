#!/usr/bin/python3
"""
Locked Class
"""


class LockedClass:
    """prevents the user from dynamically creating new instance attributes
    """
    __slots__ = ['first_name']

    def __init__(self, first_n=""):
        self.first_name = first_n
