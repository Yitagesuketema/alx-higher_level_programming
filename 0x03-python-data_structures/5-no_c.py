#!/usr/bin/python3
# File - 5-no_c.py
# Can you C me now?
# Auth - Yitagesu K Areda


def no_c(my_string):
    removed_string = []
    for x in range(0, len(my_string)):
        if my_string[x] != 'C' and my_string[x] != 'c':
            removed_string.append(my_string[x])
    return ("".join(removed_string))
