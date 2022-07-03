#!/usr/bin/python3
# File : 8-multiple_returns.py
# More returns!
# Auth : Yitagesu K Areda


def multiple_returns(sentence):
    """Returns the length of a string and its first character."""
    if sentence == "":
        return (0, None)
    return (len(sentence), sentence[0])
