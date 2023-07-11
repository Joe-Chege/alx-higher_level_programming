#!/usr/bin/python3


class MyInt(int):
    """
    A custom integer class that inherits from the built-in int class.
    The == and != operators are inverted.
    """

    def print_sorted(self):
        """prints the list, but sorted in ascending sort"""
        print(sorted(self)) 
