#!/usr/bin/python3

""" A module to defince review class."""

from sqlalchemy import Column, ForeignKey, String
from sqlalchemy.orm import relationship
from models.base_model import Base, BaseModel


class Review(BaseModel, Base):
    """ initial class review.

    from SQLAlchemy Base and links to the MySQL table reviews.

    """

    __tablename__ = "reviews"
    text = Column(String(1024), nullable=False)
    place_id = Column(String(60), ForeignKey("places.id"), nullable=False)
    user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
