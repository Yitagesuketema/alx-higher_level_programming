#!/usr/bin/python3
# File - 0-print_list_integer.py
# Auth - Yitagesu K Areda
# Print all integers of a list

def print_list_integer(my_list=[]):
    for x in range(len(my_list)):
        print("{:d}".format(my_list[x]))
