#!/usr/bin/python3
"""Defines module for write_file method."""


def write_file(filename="", text=""):
    """writes a string to a text file.

    Return: number of bytes written.
    """
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
