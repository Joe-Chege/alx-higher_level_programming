#!/usr/bin/python3

"""Defines a JSON file-writing function."""
import json


def save_to_json_file(my_obj, filename):
    """
    Save an object to a text file in JSON format.

    Args:
        my_obj: The object to be saved.
        filename: The name of the file to save the object to.

    Returns:
        None
    """
    with open(filename, 'w') as file:
        json.dump(my_obj, file)
