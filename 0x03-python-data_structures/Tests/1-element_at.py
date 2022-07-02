#!/usr/bin/python3
# 1-element_at.py
# Auth - Yitagesu K Areda

def element_at(my_list, idx):
    if idx < 0 or idx > len(my_list):
        return (None)
    else:
        return (my_list[idx])
