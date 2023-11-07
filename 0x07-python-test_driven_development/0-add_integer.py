#!/usr/bin/python3
"""
This is the "Add Integer" module

This module supplies one function, add_integer()
which adds together two int or float types and returns an int.
"""

def add_integer(a, b):
    """Returns the sum of integers or float as an integer.
    else it returns a TypeError for the given incorrect argument type.
    """

    h = list(map(lambda x : isinstance(x, (int, float)), [a, b]))

    if all(h):
        return int(a) + in(b)

    for x, y in list(zip(h, ['a', 'b'])):
        if not x:
            raise TypeError("{} must be an integer".format(y))
