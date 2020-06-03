#!/usr/bin/python3
"""
Create object from a JSON file
"""
import json


def load_from_json_file(filename):
    """function that creates an Object from a “JSON file”
    """
    with open(filename, mode="r", encoding="UTF-8") as rf:
        return json.load(rf)
