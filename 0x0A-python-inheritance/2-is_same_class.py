#!/usr/bin/python3
"""Module to check if object is an exactly instance of a class"""


def is_same_class(obj, a_class):
    """Check if an object is exactly an instance of a class.

    Args:
        obj (unknown): object whose type is to be checked.
        a_class (type): class to match the type of obj to.

    """
    return (type(obj) == a_class)
