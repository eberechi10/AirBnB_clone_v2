#!/usr/bin/pyhthon3

"""A module to test for the MySQL"""

import os
import unittest
import io
from os import getenv
from unittest.mock import patch
from console import HBNBCommand
from models.engine.db_storage import DBStorage

import MySQLdb

@unittest.skipIf(os.getenv("HBNB_TYPE_STORAGE") != "db", "Not DBStorage")
class TestMySQL(unittest.TestCase):
    """Test for the SQL database"""

    conn = None
    curr = None

    def connection(self):
        """Connect to MySQLdb"""
        storage = DBStorage()
        storage.reload()
        self.conn = MySQLdb.connect(
            getenv("HBNB_MYSQL_HOST"),
            getenv("HBNB_MYSQL_USER"),
            getenv("HBNB_MYSQL_PWD"),
            getenv("HBNB_MYSQL_DB"),)
        self.curr = self.conn.cursor()

    def test_create_city(self):
        """Test create of a City"""
        self.connection()
        with patch("sys.stdout", new=io.StringIO()) as file:
            HBNBCommand().onecmd('create State name="California"')
        city_id = file.getvalue()[:-1]
        with patch("sys.stdout", new=io.StringIO()) as file:
            HBNBCommand().onecmd(
                f'''create City state_id="{city_id}"
                                 name="San_Francisco"''')

        self.cur.execute("SELECT COUNT(*) FROM cities")
        res = self.curr.fetchone()[0]
        self.assertEqual(res, 1)
        self.disconnection()

    def disconnection(self):
        """A module to disconnect from the MySQLdb"""
        self.curr.close()
        self.conn.close()
        self.conn = None
        self.curr = None

    def test_create_state(self):
        """A module TO test for create a State"""
        self.connection()
        with patch("sys.stdout", new=io.StringIO()):
            HBNBCommand().onecmd('create State name="California"')
        self.curr.execute("SELECT COUNT(*) FROM states")
        res = self.curr.fetchone()[0]
        self.assertEqual(res, 1)
        self.disconnection()

if __name__ == "__main__":
    unittest.main()
