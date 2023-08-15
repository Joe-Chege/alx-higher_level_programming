#!/usr/bin/python3
<<<<<<< HEAD

"""Defines the base model class."""
=======
"""
class Base
"""
>>>>>>> 225805f61cce19d5d0cd81de87282de8a626ec63
import json
import os
import csv
import turtle as tr


<<<<<<< HEAD
class Base:
    """Base model class.

    Represents the base for all other classes in project 0x0C*.

    Private Class Attributes:
        __nb_objects (int): Number of instantiated Base objects.
=======
class Base():
    """
    declare private class atribute
>>>>>>> 225805f61cce19d5d0cd81de87282de8a626ec63
    """

    __nb_objects = 0

    """
    initiate class base
        Arguments
        @id: is int
    """
    def __init__(self, id=None):
<<<<<<< HEAD
        """Initialize a new Base object.

        Args:
            id (int): The identity of the new Base object.
        """
=======
>>>>>>> 225805f61cce19d5d0cd81de87282de8a626ec63
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """ turn dictionary to json """
        if list_dictionaries is None:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
<<<<<<< HEAD
        """Write the JSON serialization of a list of objects to a file.

        Args:
            list_objs (list): A list of inherited Base instances.
        """
        filename = cls.__name__ + ".json"
        with open(filename, "w") as jsonfile:
            if list_objs is None:
                jsonfile.write("[]")
            else:
                list_dicts = [o.to_dictionary() for o in list_objs]
                jsonfile.write(Base.to_json_string(list_dicts))

    @staticmethod
    def from_json_string(json_string):
        """Return the deserialization of a JSON string.

        Args:
            json_string (str): A JSON string representation of a list of dictionaries.
        Returns:
            If json_string is None or empty - an empty list.
            Otherwise - the Python list represented by json_string.
        """
        if json_string is None or json_string == "[]":
=======
        filename = cls.__name__+".json"
        jsonToSave = []
        jsonToSaveString = "["
        if list_objs is None or list_objs == []:
            with open(filename, mode='w', encoding='utf-8') as my_file:
                my_file.write(str(jsonToSave))
        else:
            for obj in list_objs:
                dictionary = cls.to_dictionary(obj)
                jsonString = cls.to_json_string(dictionary)
                jsonToSave.append(jsonString)
            for index, item in enumerate(jsonToSave):
                if index == 0:
                    jsonToSaveString += item
                elif index != len(jsonToSave):
                    jsonToSaveString += ", " + item
                with open(filename, mode='w', encoding='utf-8') as my_file:
                    my_file.write(jsonToSaveString+"]")

    @staticmethod
    def from_json_string(json_string):
        if json_string is None:
>>>>>>> 225805f61cce19d5d0cd81de87282de8a626ec63
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
<<<<<<< HEAD
        """Return a class instantiated from a dictionary of attributes.

        Args:
            **dictionary (dict): Key/value pairs of attributes to initialize.
        """
        if dictionary and dictionary != {}:
            if cls.__name__ == "Rectangle":
                new = cls(1, 1)
            else:
                new = cls(1)
            new.update(**dictionary)
            return new
=======
        if cls.__name__ == "Rectangle":
            dummy = cls(4, 5)
        elif cls.__name__ == "Square":
            dummy = cls(4)
        else:
            return
        dummy.update(**dictionary)
        return dummy
>>>>>>> 225805f61cce19d5d0cd81de87282de8a626ec63

    @classmethod
    def load_from_file(cls):
        mylist = []
        filename = cls.__name__+".json"
        jsonstring = ""
        if os.path.exists(filename):
            with open(filename, mode="r", encoding="utf-8") as myfile:
                jsonstring = myfile.read()
            pythonDic = cls.from_json_string(jsonstring)
            for dic in pythonDic:
                mylist.append(cls.create(**dic))
            return mylist
        else:
            return mylist

<<<<<<< HEAD
        Returns:
            If the file does not exist - an empty list.
            Otherwise - a list of instantiated classes.
        """
        filename = str(cls.__name__) + ".json"
        try:
            with open(filename, "r") as jsonfile:
                list_dicts = Base.from_json_string(jsonfile.read())
                return [cls.create(**d) for d in list_dicts]
        except IOError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Write the CSV serialization of a list of objects to a file.

        Args:
            list_objs (list): A list of inherited Base instances.
        """
        filename = cls.__name__ + ".csv"
        with open(filename, "w", newline="") as csvfile:
            if list_objs is None or list_objs == []:
                csvfile.write("[]")
            else:
                if cls.__name__ == "Rectangle":
                    fieldnames = ["id", "width", "height", "x", "y"]
                else:
                    fieldnames = ["id", "size", "x", "y"]
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                for obj in list_objs:
                    writer.writerow(obj.to_dictionary())

    @classmethod
    def load_from_file_csv(cls):
        """Return a list of classes instantiated from a CSV file.

        Reads from '<cls.__name__>.csv'.

        Returns:
            If the file does not exist - an empty list.
            Otherwise - a list of instantiated classes.
        """
        filename = cls.__name__ + ".csv"
        try:
            with open(filename, "r", newline="") as csvfile:
                if cls.__name__ == "Rectangle":
                    fieldnames = ["id", "width", "height", "x", "y"]
                else:
                    fieldnames = ["id", "size", "x", "y"]
                list_dicts = csv.DictReader(csvfile, fieldnames=fieldnames)
                list_dicts = [dict([k, int(v)] for k, v in d.items())
                              for d in list_dicts]
                return [cls.create(**d) for d in list_dicts]
        except IOError:
            return []

    @staticmethod
    def draw(list_rectangles, list_squares):
        """Draw rectangles and squares using the turtle module.

        Args:
            list_rectangles (list): A list of Rectangle objects to draw.
            list_squares (list): A list of Square objects to draw.
        """
        turt = turtle.Turtle()
        turt.screen.bgcolor("#b7312c")
        turt.pensize(3)
        turt.shape("turtle")

        turt.color("#ffffff")
        for rect in list_rectangles:
            turt.showturtle()
            turt.up()
            turt.goto(rect.x, rect.y)
            turt.down()
            for i in range(2):
                turt.forward(rect.width)
                turt.left(90)
                turt.forward(rect.height)
                turt.left(90)
            turt.hideturtle()

        turt.color("#b5e3d8")
        for sq in list_squares:
            turt.showturtle()
            turt.up()
            turt.goto(sq.x, sq.y)
            turt.down()
            for i in range(2):
                turt.forward(sq.width)
                turt.left(90)
                turt.forward(sq.height)
                turt.left(90)
            turt.hideturtle()

        turtle.exitonclick()
=======
    @classmethod
    def save_to_file_csv(cls, list_objs):
        if list_objs:
            filename = cls.__name__ + ".csv"
            with open(filename, mode="w", encoding="utf-8") as myfile:
                writer = csv.writer(myfile)
                for obj in list_objs:
                    if cls.__name__ == "Rectangle":
                        writer.writerow([obj.id, obj.
                                        width, obj.height, obj.x, obj.y])
                    elif cls.__name__ == "Square":
                        writer.writerow([obj.id, obj.size, obj.x, obj.y])

    @classmethod
    def load_from_file_csv(cls):
        filename = cls.__name__ + ".csv"
        objects = []
        with open(filename, 'r', encoding="utf-8") as myfile:
            reader = csv.reader(myfile)
            for line in reader:
                if cls.__name__ == "Rectangle":
                    id, width, height, x, y = map(int, line)
                    obj = cls(width, height, x, y, id)
                elif cls.__name__ == "Square":
                    id, size, x, y = map(int, line)
                    obj = cls(size, x, y, id)
                objects.append(obj)
        return objects

    @staticmethod
    def draw(list_rectangles, list_squares):
        if list_rectangles:
            rec_dics = []
            for rec in list_rectangles:
                rec_dics.append(rec.to_dictionary())
            for rec_dic in rec_dics:
                tr.setpos(rec_dic['x'], rec_dic['y'])
                tr.pendown()
                tr.forward(rec_dic["width"])
                tr.left(90)
                tr.forward(rec_dic["height"])
                tr.left(90)
                tr.forward(rec_dic["width"])
                tr.left(90)
                tr.forward(rec_dic["height"])
                tr.penup()
        if list_squares:
            sq_dics = []
            for sq in list_squares:
                sq_dics.append(sq.to_dictionary())
            for sq_dic in sq_dics:
                tr.setposition(sq_dic['x'], sq_dic['y'])
                tr.pendown()
                tr.forward(sq_dic["size"])
                tr.left(90)
                tr.forward(sq_dic["size"])
                tr.left(90)
                tr.forward(sq_dic["size"])
                tr.left(90)
                tr.forward(sq_dic["size"])
                tr.penup()
>>>>>>> 225805f61cce19d5d0cd81de87282de8a626ec63
