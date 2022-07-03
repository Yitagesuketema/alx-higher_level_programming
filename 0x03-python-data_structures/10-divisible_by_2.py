#!/usr/bin/python3
# File : 10-divisible_by_2.py
# Only by 2
# Auth : Yitagesu K Areda


def divisible_by_2(my_list=[]):
    """Find all multiples of 2 in a list."""
    multiples = []
    for i in range(len(my_list)):
        if my_list[i] % 2 == 0:
            multiples.append(True)
        else:
            multiples.append(False)

    return (multiples)
