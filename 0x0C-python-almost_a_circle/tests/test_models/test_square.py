#!/usr/bin/python3

"""
Get the unittest module
Get the Square class from models/square.py
Get patch from inittest.moc
get StringIO from io
"""

import unittest
from unittest.mock import patch
from io import StringIO
from models.square import Square

"""start of unittest class """


class TestSquare(unittest.TestCase):

    """set up function"""
    @classmethod
    def setUpClass(cls):
        cls.s1 = Square(5)
        cls.s2 = Square(2)
        cls.s3 = Square(8)
        cls.s4 = Square(3)
        cls.s5 = Square(2)
        cls.s6 = Square(4)

    """test id None"""
    def test_None(self):
        self.assertTrue(type(TestSquare.s1.id), int)

    """test id with int"""
    def test_int(self):
        TestSquare.s3.update(3)
        self.assertEqual(TestSquare.s3.id, 3)

    """test width value """
    def test_size_nonInt(self):
        with self.assertRaises(TypeError):
            TestSquare.s3.size = "5"

    """test width value -ve """
    def test_size_negative(self):
        with self.assertRaises(ValueError):
            TestSquare.s3.size = -1

    """test x value """
    def test_x_nonInt(self):
        with self.assertRaises(TypeError):
            TestSquare.s3.x = "1"

    """test x value -ve """
    def test_x_negative(self):
        with self.assertRaises(ValueError):
            TestSquare.s3.x = -1

    """test y value """
    def test_y_nonInt(self):
        with self.assertRaises(TypeError):
            TestSquare.s3.y = "1"

    """test y value -ve """
    def test_y_negative(self):
        with self.assertRaises(ValueError):
            TestSquare.s3.y = -1

    """ test area"""
    def test_area(self):
        self.assertEqual(TestSquare.s3.area(), 64)
        self.assertEqual(TestSquare.s2.area(), 4)

    """test Display"""

    def test_display(self):
        output = "#####\n#####\n#####\n#####\n#####\n"
        with patch('sys.stdout', new=StringIO()) as fake_out:
            TestSquare.s1.display()
            self.assertEqual(fake_out.getvalue(), output)
        output = "\n\n\n ###\n ###\n ###\n"
        with patch('sys.stdout', new=StringIO()) as fake_out:
            TestSquare.s5 = Square(3, 1, 3)
            TestSquare.s5.display()
            self.assertEqual(fake_out.getvalue(), output)

    """test __str__"""
    def test_string(self):
        output = "[Square] (6) 0/0 - 4\n"
        TestSquare.s6.update(6, 4)
        with patch('sys.stdout', new=StringIO()) as fake_out:
            print(TestSquare.s6)
            self.assertEqual(fake_out.getvalue(), output)

    """test update"""
    def test_update(self):
        output = "[Square] (89) 4/8 - 2\n"
        with patch('sys.stdout', new=StringIO()) as fake_out:
            TestSquare.s6.update(89, 2, 4, 8)
            print(TestSquare.s6)
            self.assertEqual(fake_out.getvalue(), output)
        output = "[Square] (89) 1/3 - 2\n"
        with patch('sys.stdout', new=StringIO()) as fake_out:
            TestSquare.s6.update(x=1, size=2, y=3)
            print(TestSquare.s6)
            self.assertEqual(fake_out.getvalue(), output)

    def test_to_dictionary(self):
        output = {'id': 89, 'size': 2, 'x': 4, 'y': 8}
        TestSquare.s6.update(89, 2, 4, 8)
        progOutput = TestSquare.s6.to_dictionary()
        self.assertEqual(progOutput, output)


if __name__ == "__main__":
    unittest.main()
