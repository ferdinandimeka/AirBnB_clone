#!/usr/bin/python3
"""
initializes the models package
"""

from os import getenv
from models.engine.db_storage import DBStorage
from models.engine.file_storage import FileStorage

storage_db = getenv("HBNB_TYPE_STORAGE")

if storage_db == "db":
    storage = DBStorage()
else:
    storage_db = FileStorage()
storage.reload()
