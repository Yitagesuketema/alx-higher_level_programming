#!/usr/bin/python3
# File : 8-simple_delete.py
# Simple delete by key
#Auth : Yitagesu K Areda


def simple_delete(a_dictionary, key=""):
    if key in a_dictionary:
        del a_dictionary[key]
    return (a_dictionary)
