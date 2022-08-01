#!/usr/bin/python3

from datetime import datetime
from uuid import uuid4


class BaseModel:
    def __init__(self, *args, **kwargs):
        self.id = str(uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
    
    def save(self):
        self.updated_at = datetime.now()
    def to_dict(self):
        dictionary = self.__dict__
        dictionary["created_at"] = self.created_at.isoformat()
        dictionary["updated_at"] = self.updated_at.isoformat()
        dictionary["__class__"] = self.__class__
        return dictionary
    
    def __str__(self):
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)
        