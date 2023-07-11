#!/usr/bin/python3

"""
Has definition of class Rectangle that inherits from BaseGeometry.
"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Definition of  the class Rectangle that inherits from BaseGeometry.
       Attributes:
            width (int): width of the rectangle.
            height (int) height of the rectangle.
    """

    def __init__(self, width, height):
        """Initializes an instance of class Rectangle"""

        self.integer_validator("width", width)
        self.integer_validator("height", height)

        self.__width = width
        self.__height = height
