#!/usr/bin/python3
"""
Load, add, save
"""
import sys
save_to_json_file = __import__('7-save_to_json_file').save_to_json_file
load_from_json_file = __import__('8-load_from_json_file').load_from_json_file

try:
    lf = load_from_json_file("add_item.json")
except FileNotFoundError:
    lf = []
argc = len(sys.argv)
for idx in range(1, argc):
    lf.append(sys.argv[idx])
save_to_json_file(lf, "add_item.json")
