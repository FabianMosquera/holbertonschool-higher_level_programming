#!/usr/bin/python3
def weight_average(my_list=[]):
    if my_list == [] or my_list is None:
        return 0
    add_t = result = 0
    for (i, j) in my_list:
        add_t += i * j
        result += j
    return add_t / result
