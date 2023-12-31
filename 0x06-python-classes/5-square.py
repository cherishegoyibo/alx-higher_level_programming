#!/usr/bin/python3
"""Define a class Square."""


class Square:
    """Represent a square."""

    def __init__(self, size=0):
        """Initialize a new square.
        size (int): The size of the new square.
        """

        self.__size = size

    @property
    def size(self):
        """retrieve size of the square."""
        return (self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Returns:  area of the current square."""

        return (self.__size * self.__size)

    def my_print(self):
        """Print the square with the character #"""
        if self.__size == 0:
            print()

        for i in range(0, self.__size):
            print("#" * self.__size)
