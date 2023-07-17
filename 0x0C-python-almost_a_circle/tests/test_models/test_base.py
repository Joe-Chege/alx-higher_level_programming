import unittest
import pep8
import os
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.base_instance = Base()
        cls.rect_instance = Rectangle(10, 7, 2, 8, 70)
        cls.square_instance = Square(5, 3, 4, 80)

    def test_pep8_base(self):
        syntax = pep8.StyleGuide(quiet=True)
        result = syntax.check_files(['models/base.py'])
        self.assertEqual(result.total_errors, 0, "Found code style errors (and warnings).")

    def test_base_id_as_positive(self):
        self.assertEqual(self.base_instance.id, 1)
        self.assertEqual(Base(115).id, 115)
        self.assertEqual(Base(67).id, 67)

    def test_base_id_as_negative(self):
        self.assertEqual(Base(-91).id, -91)
        self.assertEqual(Base(-4).id, -4)

    def test_base_id_as_none(self):
        self.assertEqual(Base().id, 1)
        self.assertEqual(Base(None).id, 2)

    def test_base_id_as_string(self):
        self.assertEqual(Base('Monty Python').id, 'Monty Python')
        self.assertEqual(Base('Python is cool').id, 'Python is cool')

    def test_to_json_string(self):
        rect_data = self.rect_instance.to_dictionary()
        json_data = Base.to_json_string([rect_data])
        self.assertIsInstance(json_data, str)
        self.assertEqual(json_data, '[{"id": 70, "width": 10, "height": 7, "x": 2, "y": 8}]')

    def test_to_json_string_empty_list(self):
        json_data = Base.to_json_string([])
        self.assertEqual(json_data, '[]')

    def test_to_json_string_none(self):
        json_data = Base.to_json_string(None)
        self.assertEqual(json_data, '[]')

    def test_instance(self):
        self.assertIsInstance(self.base_instance, Base)

    def test_load_from_file(self):
        if os.path.exists("Base.json"):
            os.remove("Base.json")

        rect_output = Rectangle.load_from_file()
        self.assertEqual(rect_output, [])

        square_output = Square.load_from_file()
        self.assertEqual(square_output, [])

    def test_create(self):
        rect_data = {'id': 31, 'x': 14, 'y': 11, 'width': 3, 'height': 3}
        rect_instance = Rectangle.create(**rect_data)
        self.assertIsInstance(rect_instance, Rectangle)
        self.assertEqual(rect_instance.to_dictionary(), rect_data)

        square_data = {'id': 42, 'size': 5, 'x': 3, 'y': 4}
        square_instance = Square.create(**square_data)
        self.assertIsInstance(square_instance, Square)
        self.assertEqual(square_instance.to_dictionary(), square_data)


if __name__ == '__main__':
    unittest.main()
