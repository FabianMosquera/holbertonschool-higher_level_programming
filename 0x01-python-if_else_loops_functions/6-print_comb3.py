#!/usr/bin/python3
for i in range(9):
    for j in range(1, 10):
        if j < i or j == i:
            continue
        if i != 8:
            print("{:d}{:d}".format(i, j), end=", ")
        else:
            print("{:d}{:d}".format(i, j))
