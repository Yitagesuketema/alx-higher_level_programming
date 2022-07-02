#!/bin/python3

def print_list_integer(my_list=[]):
    for x in range(0,len(my_list)):
        text="{number:d}"
        print(text.format(number=my_list[x])
