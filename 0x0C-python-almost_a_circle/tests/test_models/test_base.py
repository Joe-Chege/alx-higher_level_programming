#!/usr/bin/python3

"""
Get the unittest module
Get the base class from models/base.py
"""

import unittest
from models.base import Base
from models.rectangle import Rectangle

"""start of unittest class """


class TestBase(unittest.TestCase):

    """set up function"""
    @classmethod
    def setUpClass(cls):
        cls.b1 = Base()
        cls.b2 = Base(57)

    """test id None"""
    def test_None(self):
        self.assertTrue(type(TestBase.b1.id), int)

    """test id with int"""
    def test_int(self):
        self.assertEqual(TestBase.b2.id, 57)

    """test_to_json_string"""
    def test_to_json_string(self):
        output = '[{"id": 89, "width": 2, "height": 3, "x": 4, "y": 8}]'
        r6 = Rectangle(55, 24)
        r6.update(89, 2, 3, 4, 8)
        dictionary = r6.to_dictionary()
        progOutput = Base.to_json_string([dictionary])
        self.assertEqual(progOutput, output)

    """ test Json to file"""
    def test_save_to_file(self):
        output = '[{"id": 6, "width": 10, "height": 7, "x": 2, "y": 8}]'
        r7 = Rectangle(10, 7, 2, 8)
        Rectangle.save_to_file([r7])
        with open("Rectangle.json", "r") as myfile:
            progOutput = myfile.read()
            self.assertEqual(progOutput, output)

    """ test from_json_string to dic"""
    def test_save_to_file(self):
        output = [{'id': 89, 'width': 10, 'height': 4
                   }, {'id': 7, 'width': 1, 'height': 7}]
        list_input = [{'id': 89, 'width': 10, 'height': 4
                       }, {'id': 7, 'width': 1, 'height': 7}]
        json_list_input = Rectangle.to_json_string(list_input)
        progOutput = Base.from_json_string(json_list_input)
        self.assertEqual(progOutput, output)

    """ test creat method """
    def test_create(self):
        r8 = Rectangle(3, 5, 1)
        r8.update(3, 5, 1, 0, 0)
        r8dictionary = r8.to_dictionary()
        r8ins = r8.create(**r8dictionary)
        self.assertTrue(isinstance(r8ins, Rectangle))

    """ test load_from_file method """
    def test_load_from_file(self):
        r8 = Rectangle(3, 5, 1)
        list_input = [r8]
        Rectangle.save_to_file(list_input)
        list_output = Rectangle.load_from_file()
        self.assertTrue(isinstance(list_output[0], Rectangle))

    """ test save_to_file_csv"""
    def test_save_to_file_csv(self):
        output = "3,5,1,0,0\n"
        r8 = Rectangle(3, 5, 1)
        r8.update(3, 5, 1, 0, 0)
        Rectangle.save_to_file_csv([r8])
        with open("Rectangle.csv", mode="r", encoding="utf-8") as myfile:
            progOutput = myfile.read()
            self.assertEqual(progOutput, output)

    """text load_from_file_csv"""
    def test_load_from_file_csv(self):
        with open("Rectangle.csv", mode="w", encoding="utf-8") as myfile:
            myfile.write("3,5,1,0,0")
        progOutput = Rectangle.load_from_file_csv()
        self.assertTrue(isinstance(progOutput[0], Rectangle))


if __name__ == "__main__":
    unittest.main()
