#!/usr/bin/python3
# 0-print_list_integer.py
# Auth - Yitagesu K Areda
# Print all integers of a list
if __name__== "__main__":
    def print_list_integer(my_list=[]):
        for x in range(len(my_list)):
            print("{}".format(my_list[x]))
