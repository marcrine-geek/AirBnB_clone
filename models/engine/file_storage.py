#!/usr/bin/python3
"""Defines a class that serializes instances to a JSON file and
deserializes JSON file to instances:
"""
# imports
import json


class FileStorage:
    """Class for file storage"""
    __file_path = "storage.json"
    """path to the JSON file"""

    __objects = {}
    """Stores all basemodel objects"""

    def all(self):
        """Returns a dictionary of all objects"""
        return self.__objects

    def new(self, obj):
        """Sets in the obj with key <obj class name>.id in __objects

        Args:
            obj (BaseModel): Object to be added
        """
        self.__objects["{}.{}".format(obj.__class__.__name__, obj.id)] = obj

    def save(self):
        """"Serializes __objects to the JSON file (path: __file_path)"""
        # Open file for writing and close automatically
        temp_dictionary = {}
        for key in self.__objects:
            temp_dictionary[key] = self.__objects[key].to_dict()

        with open(self.__file_path, "w", encoding="utf-8") as file:
            json.dump(temp_dictionary, file)
                
    def reload(self):
        """"Deserializes the JSON file to __objects if file exists"""
        try:
            with open(self.__file_path, "r", encoding="utf-8") as file:
                for o in json.load(file).values():
                    print(o)
        except FileNotFoundError:
            pass
