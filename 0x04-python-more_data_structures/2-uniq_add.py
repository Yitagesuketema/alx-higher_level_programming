#!/usr/bin/python3
# File : 2-uniq_add.py
# Unique addition
# Auth : Yitagesu K Areda


def uniq_add(my_list=[]):
    result = 0
    for x in set(my_list):
        result += x
    return (result)
