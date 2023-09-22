#!/usr/bin/python3

""" A module to define  class file storage for hbnb """

import json

from models.review import Review
from models.state import State
from models.user import User

from models.amenity import Amenity
from models.city import City
from models.place import Place


class FileStorage:
    """storage of hbnb models in the  JSON format"""

    __file_path = "file.json"
    __objects = {}

    def all(self, cls=None):
        """dictionary of instantiated objects in __objects.

        """
        if cls is not None:
            if isinstance(cls, str):
                cls = eval(cls)
            return {
                key: value
                for key, value in self.__objects.items()
                if isinstance(value, cls)
            }
        return self.__objects

    def new(self, obj):
        """new object to storage dictionary"""
        self.all().update({obj.to_dict()["__class__"] + "." + obj.id: obj})

    def save(self):
        """Saves storage dictionary to file"""
        with open(FileStorage.__file_path, "w", encoding="UTF-8") as file:
            temp = {}
            temp.update(FileStorage.__objects)
            for key, val in temp.items():
                temp[key] = val.to_dict()
            json.dump(temp, file)

    def reload(self):
        """Loads storage dictionary from file"""

        from models.place import Place
        from models.review import Review
        from models.state import State
        from models.user import User
        from models.amenity import Amenity
        from models.base_model import BaseModel
        from models.city import City

        classes = {
            "BaseModel": BaseModel,
            "User": User,
            "Place": Place,
            "State": State,
            "City": City,
            "Amenity": Amenity,
            "Review": Review,
        }
        try:
            temp = {}
            with open(FileStorage.__file_path, "r", encoding="UTF-8") as file:
                temp = json.load(file)
                for key, val in temp.items():
                    self.all()[key] = classes[val["__class__"]](**val)
        except FileNotFoundError:
            pass

    def delete(self, obj=None):
        """Delete object from __objects, if exists."""
        try:
            del self.__objects["{}.{}".format(type(obj).__name__, obj.id)]
        except (AttributeError, KeyError):
            pass
