#!/usr/bin/python3

"""
<<<<<<< HEAD
Test for the Rectangle class
"""

import unittest
import pep8
import inspect
import io
import json
import os
from contextlib import redirect_stdout
from models import rectangle
=======
Get the unittest module
Get the Rectangle class from models/rectangle.py
Get patch from inittest.moc
get StringIO from io
"""

import unittest
from unittest.mock import patch
from io import StringIO
>>>>>>> 225805f61cce19d5d0cd81de87282de8a626ec63
from models.base import Base
Rectangle = rectangle.Rectangle


class TestRectangleDocs(unittest.TestCase):
    """Tests the Rectangle class' style and documentation"""
    @classmethod
    def setUpClass(cls):
        """Set up for the doc tests"""
        cls.rect_funcs = inspect.getmembers(Rectangle, inspect.isfunction)

    def test_pep8_conformance_rectangle(self):
        """Test that models/rectangle.py conforms to PEP8."""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/rectangle.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_pep8_conformance_test_rectangle(self):
        """Test that tests/test_models/test_rectangle.py conforms to PEP8."""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['tests/test_models/test_rectangle.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_module_docstring(self):
        """Tests for the presence of a module docstring"""
        self.assertTrue(len(rectangle.__doc__) >= 1)

    def test_class_docstring(self):
        """Tests for the presence of a class docstring"""
        self.assertTrue(len(Rectangle.__doc__) >= 1)

    def test_func_docstrings(self):
        """Tests for the presence of docstrings in all functions"""
        for func in self.rect_funcs:
            self.assertTrue(len(func[1].__doc__) >= 1)

"""start of unittest class """


class TestRectangle(unittest.TestCase):
<<<<<<< HEAD
    """Test the functionality of the Rectangle class"""
    @classmethod
    def setUpClass(cls):
        """"""
        Base._Base__nb_objects = 0
        cls.r1 = Rectangle(10, 10)
        cls.r2 = Rectangle(2, 3, 4)
        cls.r3 = Rectangle(5, 6, 7, 8, 9)
        cls.r4 = Rectangle(11, 12, 13, 14)

    def test_id(self):
        """Test for functioning ID"""
        self.assertEqual(self.r1.id, 1)
        self.assertEqual(self.r2.id, 2)
        self.assertEqual(self.r3.id, 9)
        self.assertEqual(self.r4.id, 3)

    def test_width(self):
        """Test for functioning width"""
        self.assertEqual(self.r1.width, 10)
        self.assertEqual(self.r2.width, 2)
        self.assertEqual(self.r3.width, 5)
        self.assertEqual(self.r4.width, 11)

    def test_height(self):
        """Test for functioning height"""
        self.assertEqual(self.r1.height, 10)
        self.assertEqual(self.r2.height, 3)
        self.assertEqual(self.r3.height, 6)
        self.assertEqual(self.r4.height, 12)

    def test_x(self):
        """Test for functioning x"""
        self.assertEqual(self.r1.x, 0)
        self.assertEqual(self.r2.x, 4)
        self.assertEqual(self.r3.x, 7)
        self.assertEqual(self.r4.x, 13)

    def test_y(self):
        """Test for functioning y"""
        self.assertEqual(self.r1.y, 0)
        self.assertEqual(self.r2.y, 0)
        self.assertEqual(self.r3.y, 8)
        self.assertEqual(self.r4.y, 14)

    def test_mandatory_width(self):
        """Test that width is a mandatory arg"""
        with self.assertRaises(TypeError):
            r = Rectangle()

    def test_mandatory_height(self):
        """Test that height is a mandatory arg"""
        with self.assertRaises(TypeError):
            r = Rectangle(1)

    def test_width_typeerror(self):
        """Test non-ints for width"""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r = Rectangle("hello", 1)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r = Rectangle(True, 1)

    def test_height_typeerror(self):
        """Test non-ints for height"""
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            r = Rectangle(1, "hello")
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            r = Rectangle(1, True)

    def test_x_typeerror(self):
        """Test non-ints for x"""
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            r = Rectangle(1, 1, "hello")
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            r = Rectangle(1, 1, True)

    def test_y_typeerror(self):
        """Test non-ints for y"""
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            r = Rectangle(1, 1, 1, "hello")
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            r = Rectangle(1, 1, 1, True)

    def test_width_valueerror(self):
        """Test ints <= 0 for width"""
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            r = Rectangle(-1, 1)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            r = Rectangle(0, 1)

    def test_height_valueerror(self):
        """Test ints <= 0 for height"""
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            r = Rectangle(1, -1)
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            r = Rectangle(1, 0)

    def test_x_valueerror(self):
        """Test ints < 0 for x"""
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            r = Rectangle(1, 1, -1)

    def test_y_valueerror(self):
        """Test ints <= 0 for y"""
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            r = Rectangle(1, 1, 1, -1)
=======

    """set up function"""
    @classmethod
    def setUpClass(cls):
        cls.r1 = Rectangle(10, 2)
        cls.r2 = Rectangle(2, 10)
        cls.r3 = Rectangle(8, 7, 0, 0, 12)
        cls.r4 = Rectangle(3, 7)
        cls.r5 = Rectangle(2, 3, 2, 2)
        cls.r6 = Rectangle(4, 6, 2, 1, 12)

    """test id None"""
    def test_None(self):
        self.assertTrue(type(TestRectangle.r1.id), int)
        self.assertTrue(type(TestRectangle.r2.id), int)

    """test id with int"""
    def test_int(self):
        self.assertEqual(TestRectangle.r3.id, 12)

    """test width value """
    def test_width_nonInt(self):
        with self.assertRaises(TypeError):
            Rectangle("1", 4)

    """test width value -ve """
    def test_width_negative(self):
        with self.assertRaises(ValueError):
            Rectangle(-1, 4)
            Rectangle(0, 4)

    """test height value """
    def test_height_nonInt(self):
        with self.assertRaises(TypeError):
            Rectangle(1, "4")

    """test height value -ve """
    def test_height_negative(self):
        with self.assertRaises(ValueError):
            Rectangle(1, -4)
            Rectangle(1, 0)

    """test x value """
    def test_x_nonInt(self):
        with self.assertRaises(TypeError):
            Rectangle(1, 4, "8", 7)

    """test x value -ve """
    def test_x_negative(self):
        with self.assertRaises(ValueError):
            Rectangle(1, 4, -8, 7)

    """test y value """
    def test_y_nonInt(self):
        with self.assertRaises(TypeError):
            Rectangle(1, 4, 8, "7")
>>>>>>> 225805f61cce19d5d0cd81de87282de8a626ec63

    """test y value -ve """
    def test_y_negative(self):
        with self.assertRaises(ValueError):
            Rectangle(1, 4, 8, -7)

    """ test area"""
    def test_area(self):
<<<<<<< HEAD
        """test area"""
        self.assertEqual(self.r1.area(), 100)
        self.assertEqual(self.r2.area(), 6)
        self.assertEqual(self.r3.area(), 30)
        self.assertEqual(self.r4.area(), 132)

    def test_area_args(self):
        """Test too many args for area()"""
        with self.assertRaises(TypeError):
            r = self.r1.area(1)

    def test_basic_display(self):
        """Test display without x and y"""
        r = Rectangle(2, 3, 0, 0, 1)
        with io.StringIO() as buf, redirect_stdout(buf):
            self.r1.display()
            output = buf.getvalue()
            self.assertEqual(output, ("#" * 10 + "\n") * 10)
        with io.StringIO() as buf, redirect_stdout(buf):
            r.display()
            output = buf.getvalue()
            self.assertEqual(output, ("#" * 2 + "\n") * 3)

    def test_display_too_many_args(self):
        """Test display with too many args"""
        with self.assertRaises(TypeError):
            self.r1.display(1)

    def test_str(self):
        """Test the __str__ method"""
        self.assertEqual(str(self.r1), "[Rectangle] (1) 0/0 - 10/10")
        self.assertEqual(str(self.r2), "[Rectangle] (2) 4/0 - 2/3")
        self.assertEqual(str(self.r3), "[Rectangle] (9) 7/8 - 5/6")
        self.assertEqual(str(self.r4), "[Rectangle] (3) 13/14 - 11/12")

    def test_display_xy(self):
        """Testing the display method with x and y"""
        with io.StringIO() as buf, redirect_stdout(buf):
            self.r2.display()
            output = buf.getvalue()
            self.assertEqual(output, (" " * 4 + "#" * 2 + "\n") * 3)

        with io.StringIO() as buf, redirect_stdout(buf):
            self.r3.display()
            output = buf.getvalue()
            self.assertEqual(output, "\n" * 8 +
                             (" " * 7 + "#" * 5 + "\n") * 6)

        with io.StringIO() as buf, redirect_stdout(buf):
            self.r4.display()
            output = buf.getvalue()
            self.assertEqual(output, "\n" * 14 +
                             (" " * 13 + "#" * 11 + "\n") * 12)

    def test_update_args(self):
        """Testing the udpate method with *args"""
        r = Rectangle(1, 1, 0, 0, 1)
        self.assertEqual(str(r), "[Rectangle] (1) 0/0 - 1/1")
        r.update(89)
        self.assertEqual(str(r), "[Rectangle] (89) 0/0 - 1/1")
        r.update(89, 2)
        self.assertEqual(str(r), "[Rectangle] (89) 0/0 - 2/1")
        r.update(89, 2, 3)
        self.assertEqual(str(r), "[Rectangle] (89) 0/0 - 2/3")
        r.update(89, 2, 3, 4)
        self.assertEqual(str(r), "[Rectangle] (89) 4/0 - 2/3")
        r.update(89, 2, 3, 4, 5)
        self.assertEqual(str(r), "[Rectangle] (89) 4/5 - 2/3")

    def test_update_args_setter(self):
        """tests that the update method uses setter with *args"""
        r = Rectangle(1, 1, 0, 0, 1)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r.update(1, "hello")
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            r.update(1, 1, "hello")
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            r.update(1, 1, 1, "hello")
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            r.update(1, 1, 1, 1, "hello")
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            r.update(1, 0)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            r.update(1, -1)
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            r.update(1, 1, 0)
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            r.update(1, 1, -1)
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            r.update(1, 1, 1, -1)
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            r.update(1, 1, 1, 1, -1)

    def test_update_too_many_args(self):
        """test too many args for update"""
        r = Rectangle(1, 1, 0, 0, 1)
        r.update(1, 1, 1, 1, 1, 2)
        self.assertEqual(str(r), "[Rectangle] (1) 1/1 - 1/1")

    def test_update_no_args(self):
        """test no args for update"""
        r = Rectangle(1, 1, 0, 0, 1)
        r.update()
        self.assertEqual(str(r), "[Rectangle] (1) 0/0 - 1/1")

    def test_update_kwargs(self):
        """Testing the update method with **kwargs"""
        r = Rectangle(1, 1, 0, 0, 1)
        self.assertEqual(str(r), "[Rectangle] (1) 0/0 - 1/1")
        r.update(height=10)
        self.assertEqual(str(r), "[Rectangle] (1) 0/0 - 1/10")
        r.update(width=11, x=2)
        self.assertEqual(str(r), "[Rectangle] (1) 2/0 - 11/10")
        r.update(y=3, width=4, x=5, id=89)
        self.assertEqual(str(r), "[Rectangle] (89) 5/3 - 4/10")
        r.update(x=6, height=7, y=8, width=9)
        self.assertEqual(str(r), "[Rectangle] (89) 6/8 - 9/7")

    def test_update_kwargs_setter(self):
        """tests that the update method uses setter with **kwargs"""
        r = Rectangle(1, 1, 1, 1, 1)
        with self.assertRaises(TypeError):
            r.update(width="hello")
        with self.assertRaises(TypeError):
            r.update(height="hello")
        with self.assertRaises(TypeError):
            r.update(x="hello")
        with self.assertRaises(TypeError):
            r.update(y="hello")
        with self.assertRaises(ValueError):
            r.update(width=-1)
        with self.assertRaises(ValueError):
            r.update(width=0)
        with self.assertRaises(ValueError):
            r.update(height=-1)
        with self.assertRaises(ValueError):
            r.update(height=0)
        with self.assertRaises(ValueError):
            r.update(x=-1)
        with self.assertRaises(ValueError):
            r.update(y=-1)

    def test_mix_args_kwargs(self):
        """tests output for mixed args and kwargs"""
        r = Rectangle(1, 1, 0, 0, 1)
        r.update(2, 2, 2, 2, 2, width=3, height=3, x=3, y=3, id=3)
        self.assertEqual(str(r), "[Rectangle] (2) 2/2 - 2/2")

    def test_extra_kwargs(self):
        """tests for random kwargs"""
        r = Rectangle(1, 1, 0, 0, 1)
        r.update(hello=2)
        self.assertEqual(str(r), "[Rectangle] (1) 0/0 - 1/1")

    def test_to_dict(self):
        """test regular to_dictionary"""
        d1 = self.r1.to_dictionary()
        self.assertEqual({"id": 1, "width": 10, "height": 10, "x": 0, "y": 0},
                         d1)
        d2 = self.r2.to_dictionary()
        self.assertEqual({"id": 2, "width": 2, "height": 3, "x": 4, "y": 0},
                         d2)
        d3 = self.r3.to_dictionary()
        self.assertEqual({"id": 9, "width": 5, "height": 6, "x": 7, "y": 8},
                         d3)
        d4 = self.r4.to_dictionary()
        self.assertEqual({"id": 3, "width": 11, "height": 12, "x": 13,
                          "y": 14}, d4)
        self.assertTrue(type(d1) is dict)
        self.assertTrue(type(d2) is dict)
        self.assertTrue(type(d3) is dict)
        self.assertTrue(type(d4) is dict)
        r = Rectangle(1, 1, 1, 1, 1)
        r.update(**d4)
        self.assertEqual(str(r), str(self.r4))
        self.assertNotEqual(r, self.r4)

    def test_save_to_file(self):
        """test regular use of save_to_file"""
        r1 = Rectangle(1, 1, 1, 1, 1)
        r2 = Rectangle(2, 2, 2, 2, 2)
        l = [r1, r2]
        Rectangle.save_to_file(l)
        with open("Rectangle.json", "r") as f:
            ls = [r1.to_dictionary(), r2.to_dictionary()]
            self.assertEqual(json.dumps(ls), f.read())

    def test_stf_empty(self):
        """test save_to_file with empty list"""
        l = []
        Rectangle.save_to_file(l)
        with open("Rectangle.json", "r") as f:
            self.assertEqual("[]", f.read())

    def test_stf_None(self):
        """test save_to_file with None"""
        Rectangle.save_to_file(None)
        with open("Rectangle.json", "r") as f:
            self.assertEqual("[]", f.read())

    def test_create(self):
        """test normal use of create"""
        r1 = {"id": 2, "width": 2, "height": 3, "x": 4, "y": 0}
        r2 = {"id": 9, "width": 5, "height": 6, "x": 7, "y": 8}
        r1c = Rectangle.create(**r1)
        r2c = Rectangle.create(**r2)
        self.assertEqual("[Rectangle] (2) 4/0 - 2/3", str(r1c))
        self.assertEqual("[Rectangle] (9) 7/8 - 5/6", str(r2c))
        self.assertIsNot(r1, r1c)
        self.assertIsNot(r2, r2c)
        self.assertNotEqual(r1, r1c)
        self.assertNotEqual(r2, r2c)

    def test_load_from_file_no_file(self):
        """Checks use of load_from_file with no file"""
        try:
            os.remove("Rectangle.json")
        except:
            pass
        self.assertEqual(Rectangle.load_from_file(), [])

    def test_load_from_file_empty_file(self):
        """Checks use of load_from_file with empty file"""
        try:
            os.remove("Rectangle.json")
        except:
            pass
        open("Rectangle.json", 'a').close()
        self.assertEqual(Rectangle.load_from_file(), [])

    def test_load_from_file(self):
        """test normal use of load_from_file"""
        r1 = Rectangle(1, 2, 3, 4, 5)
        r2 = Rectangle(6, 7, 8, 9, 10)
        li = [r1, r2]
        Rectangle.save_to_file(li)
        lo = Rectangle.load_from_file()
        self.assertTrue(type(lo) is list)
        self.assertEqual(len(lo), 2)
        r1c = lo[0]
        r2c = lo[1]
        self.assertTrue(type(r1c) is Rectangle)
        self.assertTrue(type(r2c) is Rectangle)
        self.assertEqual(str(r1), str(r1c))
        self.assertEqual(str(r2), str(r2c))
        self.assertIsNot(r1, r1c)
        self.assertIsNot(r2, r2c)
        self.assertNotEqual(r1, r1c)
        self.assertNotEqual(r2, r2c)
=======
        self.assertEqual(TestRectangle.r3.area(), 56)
        self.assertEqual(TestRectangle.r2.area(), 20)

    """test Display"""
    def test_display(self):
        output = "\n\n  ##\n  ##\n  ##\n"
        with patch('sys.stdout', new=StringIO()) as fake_out:
            TestRectangle.r5.display()
            self.assertEqual(fake_out.getvalue(), output)
        output = " ###\n ###\n"
        with patch('sys.stdout', new=StringIO()) as fake_out:
            TestRectangle.r5 = Rectangle(3, 2, 1, 0)
            TestRectangle.r5.display()
            self.assertEqual(fake_out.getvalue(), output)

    """test __str__"""
    def test_string(self):
        output = "[Rectangle] (12) 2/1 - 4/6\n"
        TestRectangle.r6.update(12)
        with patch('sys.stdout', new=StringIO()) as fake_out:
            print(TestRectangle.r6)
            self.assertEqual(fake_out.getvalue(), output)
        output = "[Rectangle] (1) 0/0 - 10/2\n"
        TestRectangle.r1.update(1)
        with patch('sys.stdout', new=StringIO()) as fake_out:
            print(TestRectangle.r1)
            self.assertEqual(fake_out.getvalue(), output)

    """test update"""
    def test_update(self):
        output = "[Rectangle] (89) 4/8 - 2/3\n"
        with patch('sys.stdout', new=StringIO()) as fake_out:
            TestRectangle.r6.update(89, 2, 3, 4, 8)
            print(TestRectangle.r6)
            self.assertEqual(fake_out.getvalue(), output)
        output = "[Rectangle] (89) 1/3 - 4/2\n"
        with patch('sys.stdout', new=StringIO()) as fake_out:
            TestRectangle.r6.update(x=1, height=2, y=3, width=4)
            print(TestRectangle.r6)
            self.assertEqual(fake_out.getvalue(), output)

    """test to_dictionary"""
    def test_to_dictionary(self):
        output = {'id': 89, 'width': 2, 'height': 3, 'x': 4, 'y': 8}
        TestRectangle.r6.update(89, 2, 3, 4, 8)
        progOutput = TestRectangle.r6.to_dictionary()
        self.assertEqual(progOutput, output)


if __name__ == "__main__":
    unittest.main()
>>>>>>> 225805f61cce19d5d0cd81de87282de8a626ec63
