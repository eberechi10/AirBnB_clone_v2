#!/usr/bin/python3

""" This module defines the Place class."""

from os import getenv
from sqlalchemy import Column, Float, ForeignKey, Integer, String, Table
from sqlalchemy.orm import relationship

import models
from models.amenity import Amenity
from models.base_model import Base, BaseModel
from models.review import Review

own_table = Table(
    "place_amenity",
    Base.metadata,
    Column(
        "place_id",
        String(60),
        ForeignKey("places.id"),
        primary_key=True,
        nullable=False,
    ),
    Column(
        "amenity_id",
        String(60),
        ForeignKey("amenities.id"),
        primary_key=True,
        nullable=False,
    ),
)


class Place(BaseModel, Base):
    """ initializes the Place for database.

    Inherits from SQLAlchemy Base and links to the MySQL table places.

    Attributes:
        amenities (sqlalchemy relationship): Place-Amenity relationship.
        amenity_ids (list): An id list of all linked amenities.
    """

    __tablename__ = "places"
    city_id = Column(String(60), ForeignKey("cities.id"), nullable=False)
    user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024))
    number_rooms = Column(Integer, default=0)
    number_bathrooms = Column(Integer, default=0)
    max_guest = Column(Integer, default=0)
    price_by_night = Column(Integer, default=0)
    latitude = Column(Float)
    longitude = Column(Float)
    reviews = relationship("Review", backref="place", cascade="delete")
    amenities = relationship(
        "Amenity", secondary="place_amenity", viewonly=False
    )
    amenity_ids = []

    if getenv("HBNB_TYPE_STORAGE", None) != "db":

        @property
        def reviews(self):
            """Get a list of all linked Reviews."""
            return [
                review
                for review in list(models.storage.all(Review).values())
                if review.place_id == self.id
            ]

        @property
        def amenities(self):
            """Get/set linked Amenities."""
            return [
                amenity
                for amenity in list(models.storage.all(Amenity).values())
                if amenity.id in self.amenity_ids
            ]

        @amenities.setter
        def amenities(self, value):
            if isinstance(value, Amenity):
                self.amenity_ids.append(value.id)
