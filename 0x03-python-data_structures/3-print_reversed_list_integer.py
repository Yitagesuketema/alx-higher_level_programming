#!/usr/bin/python3
# File - 3-print_reversed_list_integer.py
# Print a list of integers... in reverse!
# Auth - Yitagesu K Areda


def print_reversed_list_integer(my_list=[]):
    for x in range(1, len(my_list) + 1):
        print("{:d}".format(my_list[-x]))