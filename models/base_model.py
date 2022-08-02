#!/usr/bin/python3
"""Defines a base model class.

This class defines all common attributes/methods for other classes.
"""

# Imports
from datetime import datetime
from uuid import uuid4

class BaseModel:
	"""Represents the "base" for all other classes."""

	# kwargs is a dictionary
	def __init__(self, *args, **kwargs):
		"""Initialize a new BaseModel/ Instance

		Args:
			id (int): Unique id for each BaseModel
			created_at: Date of object creation
			updated_at: Date of object change
		"""
		self.id = str(uuid4())
		self.created_at = datetime.now()
		self.updated_at = datetime.now()

	def save(self):
		"""Updates the public instance attribute updated_at with
			the current datetime.
		"""
		self.updated_at = datetime.now()

	def to_dict(self):
		"""Return a dictionary containing all keys/values of __dict__ of
			the instance
		"""
		dictionary = self.__dict__
		dictionary["created_at"] = self.created_at.isoformat()
		dictionary["updated_at"] = self.updated_at.isoformat()
		dictionary["__class__"] = self.__class__
		return dictionary
    
	def __str__(self):
		"""Return the printable representation of model"""
		return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)
