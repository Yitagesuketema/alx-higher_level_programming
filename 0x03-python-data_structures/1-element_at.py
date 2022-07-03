#!/usr/bin/python3
# File - 1-element_at.py
# Secure access to an element in a list
# Auth - Yitagesu K Areda

def element_at(my_list, idx):
    while idx >= 0 and idx <= (len(my_list))-1:
        return (my_list[idx])
    return (None)
