#!/usr/bin/python3
"""
class Base
"""
import json
import os
import csv
import turtle as tr


class Base():
    """
    declare private class atribute
    """

    __nb_objects = 0

    """
    initiate class base
        Arguments
        @id: is int
    """
    def __init__(self, id=None):
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
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        if cls.__name__ == "Rectangle":
            dummy = cls(4, 5)
        elif cls.__name__ == "Square":
            dummy = cls(4)
        else:
            return
        dummy.update(**dictionary)
        return dummy

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
