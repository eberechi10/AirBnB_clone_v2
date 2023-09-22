#!/usr/bin/python3

"""A module the Database Storage engine."""

from os import getenv

from sqlalchemy import create_engine
from sqlalchemy.orm import relationship, scoped_session, sessionmaker
from models.amenity import Amenity
from models.base_model import Base, BaseModel
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User


class DBStorage:

    """ this module initializes the database storage engine.

    """

    __engine = None
    __session = None

    def __init__(self):
        """ A module to define new Database Storage."""

        self.__engine = create_engine("mysql+mysqldb://{}:{}@{}/{}".
                                      format(getenv("HBNB_MYSQL_USER"),
                                             getenv("HBNB_MYSQL_PWD"),
                                             getenv("HBNB_MYSQL_HOST"),
                                             getenv("HBNB_MYSQL_DB")),
                                      pool_pre_ping=True)
        if getenv("HBNB_ENV") == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):

        if cls is None:
            objs = self._extracted_from_all_10()
        else:
            if isinstance(cls, str):
                cls = eval(cls)
            objs = self.__session.query(cls)
        return {f"{type(o).__name__}.{o.id}": o for o in objs}

    def _extracted_from_all_10(self):
        result = self.__session.query(State).all()
        result.extend(self.__session.query(City).all())
        result.extend(self.__session.query(User).all())
        result.extend(self.__session.query(Place).all())
        result.extend(self.__session.query(Review).all())
        result.extend(self.__session.query(Amenity).all())
        return result

    def new(self, obj):
        """Add obj to the current database session."""
        self.__session.add(obj)

    def close(self):
        self.__session.close()

    def save(self):
        """Commit all changes to the current database session."""
        self.__session.commit()

    def delete(self, obj=None):
        """Delete obj from the current database session."""
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """Create all tables in the database and initialize a new session."""
        Base.metadata.create_a
        (self.__engine)
        session_factory = sessionmaker(
            bind=self.__engine, expire_on_commit=False
        )
        session = scoped_session(session_factory)
        self.__session = session()
