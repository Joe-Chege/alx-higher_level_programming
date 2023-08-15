#!/usr/bin/python3
"""
Get the unittest module
Get the base class from models/base.py
"""

import unittest
<<<<<<< HEAD
import inspect
import pep8
import json
from models import base
Base = base.Base


class TestBaseDocs(unittest.TestCase):
    """Tests to check the documentation and style of Base class"""
    @classmethod
    def setUpClass(cls):
        """Set up for the doc tests"""
        cls.base_funcs = inspect.getmembers(Base, inspect.isfunction)

    def test_pep8_conformance_base(self):
        """Test that models/base.py conforms to PEP8."""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/base.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_pep8_conformance_test_base(self):
        """Test that tests/test_models/test_base.py conforms to PEP8."""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['tests/test_models/test_base.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_module_docstring(self):
        """Tests for the module docstring"""
        self.assertTrue(len(base.__doc__) >= 1)

    def test_class_docstring(self):
        """Tests for the Base class docstring"""
        self.assertTrue(len(Base.__doc__) >= 1)

    def test_func_docstrings(self):
        """Tests for the presence of docstrings in all functions"""
        for func in self.base_funcs:
            self.assertTrue(len(func[1].__doc__) >= 1)


class TestBase(unittest.TestCase):
    """Tests to check functionality of Base class"""
    def test_too_many_args(self):
        """test too many args to init"""
        with self.assertRaises(TypeError):
            b = Base(1, 1)

    def test_no_id(self):
        """Tests id as None"""
        b = Base()
        self.assertEqual(b.id, 1)

    def test_id_set(self):
        """Tests id as not None"""
        b98 = Base(98)
        self.assertEqual(b98.id, 98)

    def test_no_id_after_set(self):
        """Tests id as None after not None"""
        b2 = Base()
        self.assertEqual(b2.id, 2)

    def test_nb_private(self):
        """Tests nb_objects as a private instance attribute"""
        b = Base(3)
        with self.assertRaises(AttributeError):
            print(b.nb_objects)
        with self.assertRaises(AttributeError):
            print(b.__nb_objects)

    def test_to_json_string(self):
        """Tests regular to json string"""
        Base._Base__nb_objects = 0
        d1 = {"id": 9, "width": 5, "height": 6, "x": 7, "y": 8}
        d2 = {"id": 2, "width": 2, "height": 3, "x": 4, "y": 0}
        json_s = Base.to_json_string([d1, d2])
        self.assertTrue(type(json_s) is str)
        d = json.loads(json_s)
        self.assertEqual(d, [d1, d2])

    def test_empty_to_json_string(self):
        """Test for passing empty list/ None"""
        json_s = Base.to_json_string([])
        self.assertTrue(type(json_s) is str)
        self.assertEqual(json_s, "[]")

    def test_None_to_json_String(self):
        json_s = Base.to_json_string(None)
        self.assertTrue(type(json_s) is str)
        self.assertEqual(json_s, "[]")

    def test_from_json_string(self):
        """Tests regular from_json_string"""
        json_str = '[{"id": 9, "width": 5, "height": 6, "x": 7, "y": 8}, \
{"id": 2, "width": 2, "height": 3, "x": 4, "y": 0}]'
        json_l = Base.from_json_string(json_str)
        self.assertTrue(type(json_l) is list)
        self.assertEqual(len(json_l), 2)
        self.assertTrue(type(json_l[0]) is dict)
        self.assertTrue(type(json_l[1]) is dict)
        self.assertEqual(json_l[0],
                         {"id": 9, "width": 5, "height": 6, "x": 7, "y": 8})
        self.assertEqual(json_l[1],
                         {"id": 2, "width": 2, "height": 3, "x": 4, "y": 0})

    def test_fjs_empty(self):
        """Tests from_json_string with an empty string"""
        self.assertEqual([], Base.from_json_string(""))

    def test_fjs_None(self):
        """Tests from_json_string with an empty string"""
        self.assertEqual([], Base.from_json_string(None))
=======
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
>>>>>>> 225805f61cce19d5d0cd81de87282de8a626ec63
