#!/usr/bin/python3
"""
From JSON string to Object
"""
import json


def save_to_json_file(my_obj, filename):
    """function that writes an Object to a text
    file, using a JSON representation
    """
    with open(filename, mode="w", encoding="UTF-8") as sf:
        json.dump(my_obj, sf)
