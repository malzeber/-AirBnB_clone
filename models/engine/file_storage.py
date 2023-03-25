#!/usr/bin/python3
""" FileStorage """


import json
import datetime
import os


class FileStorage:
    """ Store first object """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """ Store first object """
        return FileStorage.__objects

    def new(self, obj):
        """ Store first object """
        key = "{}.{}".format(type(obj).__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """ Store first object """
        with open(FileStorage.__file_path, "w", encoding="utf-8") as writer:
            d = {key: value.to_dict() for
                 key, value in FileStorage.__objects.items()}
            json.dump(d, writer)

    def classes(self):
        from models.base_model import BaseModel
        from models.user import User
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.place import Place
        from models.review import Review
        classes = {"BaseModel": BaseModel,
                   "User": User,
                   "State": State,
                   "City": City,
                   "Amenity": Amenity,
                   "Place": Place,
                   "Review": Review}
        return classes

    def reload(self):
        """ Store first object """
        if not os.path.isfile(FileStorage.__file_path):
            return
        with open(FileStorage.__file_path, "r", encoding="utf-8") as opener:
            objDict = json.load(opener)
            objDict = {k: self.classes()[v["__class__"]](**v)
                       for k, v in objDict.items()}
            FileStorage.__objects = objDict

    def attributes(self):
        """ returns the valid attributes """
        attributes = {
            "BaseModel":
                     {"id": str,
                      "created_at": datetime.datetime,
                      "updated_at": datetime.datetime},
            "User":
                     {"email": str,
                      "password": str,
                      "first_name": str,
                      "last_name": str},
            "State":
                     {"name": str},
            "City":
                     {"state_id": str,
                      "name": str},
            "Amenity":
                     {"name": str},
            "Place":
                     {"city_id": str,
                      "user_id": str,
                      "name": str,
                      "description": str,
                      "number_rooms": int,
                      "number_bathrooms": int,
                      "max_guest": int,
                      "price_by_night": int,
                      "latitude": float,
                      "longitude": float,
                      "amenity_ids": list},
            "Review":
            {"place_id": str,
                         "user_id": str,
                         "text": str}
        }
        return attributes
