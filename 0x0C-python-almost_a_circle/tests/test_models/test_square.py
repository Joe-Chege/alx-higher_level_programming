#!/usr/bin/python3
"""
A module that test differents behaviors
of the Square class
"""
import unittest
import pep8
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square



class TestSquare(unittest.TestCase):
    def test_init(self):
        square = Square(5, 2, 4, 1)
        self.assertEqual(square.width, 5)
        self.assertEqual(square.height, 5)
        self.assertEqual(square.x, 2)
        self.assertEqual(square.y, 4)
        self.assertEqual(square.id, 1)

    def test_size(self):
        square = Square(5)
        self.assertEqual(square.size, 5)
        square.size = 10
        self.assertEqual(square.size, 10)
        self.assertEqual(square.width, 10)
        self.assertEqual(square.height, 10)
        with self.assertRaises(ValueError):
            square.size = -5
        with self.assertRaises(TypeError):
            square.size = "invalid"

    def test_x(self):
        square = Square(5)
        self.assertEqual(square.x, 0)
        square.x = 5
        self.assertEqual(square.x, 5)
        with self.assertRaises(ValueError):
            square.x = -5
        with self.assertRaises(TypeError):
            square.x = "invalid"

    def test_y(self):
        square = Square(5)
        self.assertEqual(square.y, 0)
        square.y = 5
        self.assertEqual(square.y, 5)
        with self.assertRaises(ValueError):
            square.y = -5
        with self.assertRaises(TypeError):
            square.y = "invalid"

    def test_area(self):
        square = Square(5)
        self.assertEqual(square.area(), 25)

    def test_display(self):
        square = Square(3, 1, 1)
        expected_output = " ###\n" \
                          " ###\n" \
                          " ###\n"
        with unittest.mock.patch("sys.stdout", new=unittest.mock.StringIO()) as mock_output:
            square.display()
            self.assertEqual(mock_output.getvalue(), expected_output)

    def test_str(self):
        square = Square(5, 2, 4, 1)
        expected_output = "[Square] (1) 2/4 - 5"
        self.assertEqual(str(square), expected_output)

    def test_update(self):
        square = Square(5, 2, 4, 1)
        square.update(2, 10, 3, 5)
        self.assertEqual(square.id, 2)
        self.assertEqual(square.size, 10)
        self.assertEqual(square.width, 10)
        self.assertEqual(square.height, 10)
        self.assertEqual(square.x, 3)
        self.assertEqual(square.y, 5)

    def test_to_dictionary(self):
        square = Square(5, 2, 4, 1)
        expected_dict = {
            "id": 1,
            "size": 5,
            "x": 2,
            "y": 4
        }
        self.assertEqual(square.to_dictionary(), expected_dict)


if __name__ == "__main__":
    unittest.main()
