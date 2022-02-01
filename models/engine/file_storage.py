#!/usr/bin/python3
"""
Contains the Filestorage Class
"""

import json
from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User

classes = {"Amenity": Amenity, "BaseModel": BaseModel, "City": City,
           "Place": Place, "Review": Review, "State": State, "User": User}


class FileStorage:
    """serializes instances to a Json file & deserializes back to instances"""
    
    # string - path to json file
    __file_path = "file.json"
    # dictionary - empty will store all objects by <class name>.id
    __objects = {}
    
    def all(self, itm=None):
        """returns the dictionary __objects"""
        if itm is not None:
            new_dict = {}
            for key, value in self.__objects.items():
                if itm == value.__class__ or itm == value.__class__.__name__:
                    new_dict[key] = value
            return new_dict
        return self.__objects
    
    def new(self, obj=None):
        """sets in __objects the obj with key <obj class name>.id"""
        if obj is not None:
            key = obj.__class__.__name__ + "." + obj.id
            self.__objects[key] = obj
            
    def save(self):
        """serializes __objects to the json file (path: __file_path)"""
        json_objects = {}
        for key in self.__objects:
            json_objects[key] = self.__objects[key].to_dict()
            #dumping it from file
        with open(self.__file_path, 'w') as f:
            json.dump(json_objects, f)
            
    def reload(self):
        """deserializes the json file to __objects"""
        try:
        # retreiving data from a file
            with open(self.__file_path, 'r') as f:
                d = json.load(f)
            for key in d:
                self.__objects[key] = classes[d[key]["__class__"]]
        except:
            pass
        
    def delete(self, obj=None):
        """delete obj from __objects if it exist"""
        if obj is not None:
            key = obj.__class__.__name__ + '.' + obj.id
            if key in self.__objects:
                del self.__objects[key]
            
    def close(self):
        """call reload method for deserializing the json file"""
        self.reload()