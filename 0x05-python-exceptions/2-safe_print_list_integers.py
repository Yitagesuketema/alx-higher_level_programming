#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    len = 0
    for i in range(0, x):
        try:
            print("{:d}".format(my_list[i]))
            len += 1
        except Exception as e:
            continue
    print ()
    return (len)
