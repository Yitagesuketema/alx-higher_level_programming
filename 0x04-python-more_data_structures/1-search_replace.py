#!/usr/bin/python3
# File : 1-search_replace.py
# Search and replace
# Auth : Yitagesu K Areda


def search_replace(my_list, search, replace):
    new_list = my_list[:]
    for i in range(len(new_list)):
        if new_list[i] == search:
            new_list[i] = replace
    return (new_list)
