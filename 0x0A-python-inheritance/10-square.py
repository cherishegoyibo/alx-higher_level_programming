#!/usr/bin/python3
"""Defines a subclass square"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Represents a subclass square that inherits from class rectangle"""
    def __init__(self, size):
        """initialises an instance of class square"""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """"returns the area of the square"""
        return self.__size ** 2
