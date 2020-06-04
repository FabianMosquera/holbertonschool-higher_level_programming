#!/usr/bin/python3
"""append_after
"""


def append_after(filename="", search_string="", new_string=""):
    """Insert new_string after search_string into filename
    """
    with open(filename, mode="r+", encoding="utf-8") as rf:
        tmp = rf.readlines()

    count = 0
    with open(filename, mode="w", encoding="utf-8") as wf:
        for i in tmp:
            count += 1
            if search_string in i:
                tmp.insert(count, new_string)
        for i in tmp:
            wf.write(lines)
