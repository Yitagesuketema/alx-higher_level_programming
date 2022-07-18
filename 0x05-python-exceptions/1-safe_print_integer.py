#!/usr/bin/python3
from tempfile import TemporaryFile


def safe_print_integer(value):
    try:
        print("{:d}".format(value))
        return (True)
    except Exception as e:
        return (False)
