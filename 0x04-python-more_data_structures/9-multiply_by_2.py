#!/usr/bin/python3
# File : 9-multiple_by_2.py
# Multiply by 2
# Auth : Yitagesu K areda


def multiply_by_2(a_dictionary):
    """Return a new dictionary with all values multipled by 2."""
    return ({k: a_dictionary[k] * 2 for k in a_dictionary})
