#!/usr/bin/python3
# 0-print_list_integer.py
# Auth - Yitagesu Ketema

def main ():
    def print_list_integer(my_list=[]):
        for x in range(len(my_list)):
            print("{:d}".format(my_list[x]))
if __name__ == "__main__":
    main()