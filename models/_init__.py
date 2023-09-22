#!/usr/bin/python3

""" A module to create a storage object.
    when variable 'HBNB_TYPE_STORAGE' is set to 'db',.
"""
from os import getenv


if getenv("HBNB_TYPE_STORAGE") == "db":
    from models.engine.db_storage import DBStorage
    storage = DBStorage()
else:
    from models.engine.file_storage import FileStorage
    storage = FileStorage()
storage.reload()
