#!/usr/bin/python3

""" a module to define the amenity class for HBNB project """

from models.base_model import BaseModel, Base

from models import storage_type
from sqlalchemy import Column, String


class Amenity(BaseModel, Base):
    '''amenity class for the databse'''

    __tablename__ = 'amenities'
    if storage_type == 'db':
        name = Column(String(128), nullable=False)
    else:
        name = ""
