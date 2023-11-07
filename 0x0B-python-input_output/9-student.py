#!/usr/bin/python3
"""Defines module for class Student."""


class Student:
    """Represents a student"""

    def __init__(self, first_name, last_name, age):
        """
            Initialises a Student instance.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Gets a dictionary representation of a Student."""
        return self.__dict__
