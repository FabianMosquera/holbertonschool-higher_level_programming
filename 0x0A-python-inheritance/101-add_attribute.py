#!/usr/bin/python3
"""
Can I?
"""


def add_attribute(obj, name, value):
    """adds a new attrbute
    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, name, value)
