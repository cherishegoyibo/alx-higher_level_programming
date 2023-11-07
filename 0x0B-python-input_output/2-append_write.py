#!/usr/bin/python3
"""Defines module for append_write method."""


def append_write(filename="", text=""):
    """Appends a string to the end of a text file.

        Returns: the number of characters written.
    """
    with open(filename, "a", encoding='utf-8') as f:
        return f.write(text)
