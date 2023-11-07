#!/usr/bin/python3
"""Defines a text file-reading method"""


def read_file(filename=""):
    """Prints the contents of a UTF8 text file to stdout"""
    with open(filename, "r", encoding="utf-8") as f:
        print(f.read(), end="")
