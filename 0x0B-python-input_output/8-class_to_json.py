#!/usr/bin/python3
"""Defines a python class_to_json method."""


def class_to_json(obj):
    """Returns dictionary representation of a simple data structure."""
    return obj.__dict__
