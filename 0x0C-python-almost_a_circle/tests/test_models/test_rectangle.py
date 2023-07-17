#!/usr/bin/python3
"""
A module that test differents behaviors
of the Base class
"""
import unittest
import pep8
from models.base import Base
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    def test_init(self):
        rectangle = Rectangle(10, 20, 2, 4, 1)
        self.assertEqual(rectangle.width, 10)
        self.assertEqual(rectangle.height, 20)
        self.assertEqual(rectangle.x, 2)
        self.assertEqual(rectangle.y, 4)
        self.assertEqual(rectangle.id, 1)

    def test_width(self):
        rectangle = Rectangle(10, 20)
        self.assertEqual(rectangle.width, 10)
        rectangle.width = 30
        self.assertEqual(rectangle.width, 30)
        with self.assertRaises(ValueError):
            rectangle.width = -10
        with self.assertRaises(TypeError):
            rectangle.width = "invalid"

    def test_height(self):
        rectangle = Rectangle(10, 20)
        self.assertEqual(rectangle.height, 20)
        rectangle.height = 30
        self.assertEqual(rectangle.height, 30)
        with self.assertRaises(ValueError):
            rectangle.height = -10
        with self.assertRaises(TypeError):
            rectangle.height = "invalid"

    def test_x(self):
        rectangle = Rectangle(10, 20)
        self.assertEqual(rectangle.x, 0)
        rectangle.x = 5
        self.assertEqual(rectangle.x, 5)
        with self.assertRaises(ValueError):
            rectangle.x = -5
        with self.assertRaises(TypeError):
            rectangle.x = "invalid"

    def test_y(self):
        rectangle = Rectangle(10, 20)
        self.assertEqual(rectangle.y, 0)
        rectangle.y = 5
        self.assertEqual(rectangle.y, 5)
        with self.assertRaises(ValueError):
            rectangle.y = -5
        with self.assertRaises(TypeError):
            rectangle.y = "invalid"

    def test_area(self):
        rectangle = Rectangle(10, 20)
        self.assertEqual(rectangle.area(), 200)

    def test_display(self):
        rectangle = Rectangle(3, 2, 1, 1)
        expected_output = " \n" \
                          "  ###\n" \
                          "  ###\n"
        with unittest.mock.patch("sys.stdout", new=unittest.mock.StringIO()) as mock_output:
            rectangle.display()
            self.assertEqual(mock_output.getvalue(), expected_output)

    def test_str(self):
        rectangle = Rectangle(10, 20, 2, 4, 1)
        expected_output = "[Rectangle] (1) 2/4 - 10/20"
        self.assertEqual(str(rectangle), expected_output)

    def test_update(self):
        rectangle = Rectangle(10, 20, 2, 4, 1)
        rectangle.update(2, 30, 40, 5, 6)
        self.assertEqual(rectangle.id, 2)
        self.assertEqual(rectangle.width, 30)
        self.assertEqual(rectangle.height, 40)
        self.assertEqual(rectangle.x, 5)
        self.assertEqual(rectangle.y, 6)

    def test_to_dictionary(self):
        rectangle = Rectangle(10, 20, 2, 4, 1)
        expected_dict = {
            "id": 1,
            "width": 10,
            "height": 20,
            "x": 2,
            "y": 4
        }
        self.assertEqual(rectangle.to_dictionary(), expected_dict)


if __name__ == "__main__":
    unittest.main()
