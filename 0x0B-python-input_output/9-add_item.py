#!/usr/bin/python3
"""
Load, add, save
"""
import sys
import os
save_to_json_file = __import__('7-save_to_json_file').save_to_json_file
load_from_json_file = __import__('8-load_from_json_file').load_from_json_file

if __name__ == "__main__":
    data = "add_item.json"
    if os.path.isfile(data):
        save_file = load_from_json_file(data)
    else:
        save_file = []
    for i in range(1, len(sys.argv)):
        save_file.append(sys.argv[i])
    save_to_json_file(save_file, data)
    