#!/usr/bin/python3
"""
checks if object is an instance of a class that
inherited from a class or not
"""


def inherits_from(obj, a_class):
    """Return true if obj is instance of a class
    that inherited from it, else False

    Args:
        obj (unknown): object whose type is to be checked.
        a_class (type): class criteria to validate.
    """

    return (issubclass(type(obj), a_class) and type(obj) != a_class)
