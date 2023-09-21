#!/usr/bin/python3

"""A module to define the database Storage engine."""

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
    """a database storage engine

    """

    __engine = None
    __session = None

    def __init__(self):
        """Initialize a new database Storage instance."""

        self.__engine = create_engine("mysql+mysqldb://{}:{}@{}/{}".
                                      format(getenv("HBNB_MYSQL_USER"),
                                             getenv("HBNB_MYSQL_PWD"),
                                             getenv("HBNB_MYSQL_HOST"),
                                             getenv("HBNB_MYSQL_DB")),
                                      pool_pre_ping=True)
        if getenv("HBNB_ENV") == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """Query curret database session all objects of the given class.

        """
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

    def delete(self, obj=None):
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """Create all tables in database and initialize a new session."""
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(
            bind=self.__engine, expire_on_commit=False
        )
        session = scoped_session(session_factory)
        self.__session = session()

    def close(self):
        """Close the working SQLAlchemy session."""
        self.__session.close()    

    def new(self, obj):
        """Add to current database session."""
        self.__session.add(obj)

    def save(self):
        """Commit all changes to current database session."""
        self.__session.commit()
