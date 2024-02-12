#!/usr/bin/python3
"""Defines a base model class."""
import json
import csv
import turtle


class Base:
    """Base class for managing instances."""

    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize a new Base instance."""
        if id is not None:
            if not isinstance(id, int):
                raise TypeError("id must be an integer")
            if id < 0:
                raise ValueError("id must be >= 0")
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @classmethod
    def save_to_file(cls, list_objs):
        """Write the JSON string representation of list_objs to a file."""
        filename = cls.__name__ + ".json"
        with open(filename, "w") as file:
            if list_objs is None:
                file.write("[]")
            else:
                json_list = [obj.to_dictionary() for obj in list_objs]
                file.write(cls.to_json_string(json_list))

    @classmethod
    def create(cls, **dictionary):
        """Return an instance with all attributes already set."""
        if cls.__name__ == "Rectangle":
            instance = cls(1, 1)  # dummy instance
        elif cls.__name__ == "Square":
            instance = cls(1)  # dummy instance
        instance.update(**dictionary)
        return instance

    @classmethod
    def load_from_file(cls):
        """Return a list of instances based on the JSON string representation loaded from a file."""
        filename = cls.__name__ + ".json"
        instances = []
        try:
            with open(filename, "r") as file:
                json_str = file.read()
                json_list = cls.from_json_string(json_str)
                for dict_item in json_list:
                    instances.append(cls.create(**dict_item))
        except FileNotFoundError:
            pass
        return instances

    @staticmethod
    def to_json_string(list_dictionaries):
        """Return the JSON string representation of list_dictionaries."""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @staticmethod
    def from_json_string(json_string):
        """Return the list of the JSON string representation json_string."""
        if json_string is None or json_string == "":
            return []
        return json.loads(json_string)

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Write the CSV representation of list_objs to a file."""
        filename = cls.__name__ + ".csv"
        with open(filename, "w", newline="") as file:
            writer = csv.writer(file)
            for obj in list_objs:
                if cls.__name__ == "Rectangle":
                    writer.writerow([obj.id, obj.width, obj.height, obj.x, obj.y])
                elif cls.__name__ == "Square":
                    writer.writerow([obj.id, obj.size, obj.x, obj.y])

    @classmethod
    def load_from_file_csv(cls):
        """Return a list of instances based on the CSV representation loaded from a file."""
        filename = cls.__name__ + ".csv"
        instances = []
        try:
            with open(filename, "r", newline="") as file:
                reader = csv.reader(file)
                for row in reader:
                    if cls.__name__ == "Rectangle":
                        instance = cls(int(row[0]), int(row[1]), int(row[2]), int(row[3]), int(row[4]))
                    elif cls.__name__ == "Square":
                        instance = cls(int(row[0]), int(row[1]), int(row[2]), int(row[3]))
                    instances.append(instance)
        except FileNotFoundError:
            pass
        return instances

    @staticmethod
    def draw(list_rectangles, list_squares):
        """Draw rectangles and squares using the Turtle graphics module."""
        turtle.speed(0)
        turtle.bgcolor("lightgreen")

        for rectangle in list_rectangles:
            turtle.penup()
            turtle.goto(rectangle.x, rectangle.y)
            turtle.pendown()
            for _ in range(2):
                turtle.forward(rectangle.width)
                turtle.left(90)
                turtle.forward(rectangle.height)
                turtle.left(90)

        for square in list_squares:
            turtle.penup()
            turtle.goto(square.x, square.y)
            turtle.pendown()
            for _ in range(4):
                turtle.forward(square.size)
                turtle.left(90)

        turtle.done()
