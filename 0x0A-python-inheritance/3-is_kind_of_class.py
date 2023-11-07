#!/usr/bin/python3
"""checks if object is an instance of a class or inherited class"""


def is_kind_of_class(obj, a_class):
    """Returns true if object is an instance of a class or inherited,
    else false

    Args:
        obj (unknown): The object to check.
        a_class (type): The class to match the type of obj to.
    """
    return isinstance(obj, a_class)
