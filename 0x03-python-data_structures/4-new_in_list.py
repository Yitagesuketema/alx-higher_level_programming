#!/usr/bin/python3
# File : 4-new_in_list.py
# Replace in a copy
# Auth : Yitagesu K Areda


def new_in_list(my_list, idx, element):
    while idx >= 0 and idx < len(my_list):
        copy_list = my_list.copy()
        copy_list[idx] = element
        return(copy_list)
    return(my_list)
