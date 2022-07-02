#!/usr/bin/python3
# 2-replace_in_list.py
# Replace element
# Auth - Yitagesu K Areda

def replace_in_list(my_list, idx, element):
    while idx >= 0 and idx < len(my_list):
        my_list[idx] = element
        return (my_list)
    return (my_list)
