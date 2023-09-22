#!/usr/bin/python3

"""A module to defines unittests for the console.py."""

import unittest
import pep8
import models
import os
from io import StringIO
from unittest.mock import patch
from console import HBNBCommand

from models.engine.db_storage import DBStorage
from models.engine.file_storage import FileStorage


class TestHBNBCommand(unittest.TestCase):
    """Initialize unittests for testing the HBNB command interpreter."""

    @classmethod
    def setUpClass(cls):
        """defines HBNBCommand testing setup.

        """
        try:
            os.rename("file.json", "tmp")
        except IOError:
            pass
        cls.HBNB = HBNBCommand()

    @classmethod
    def tearDownClass(cls):
        """defines HBNBCommand testing teardown.

        """
        try:
            os.rename("tmp", "file.json")
        except IOError:
            pass
        del cls.HBNB
        if type(models.storage) == DBStorage:
            models.storage._DBStorage__session.close()

    def setUp(self):
        """A module to reset FileStorage objects dictionary."""
        FileStorage._FileStorage__objects = {}

    def tearDown(self):
        """it delete any created file.json."""
        try:
            os.remove("file.json")
        except IOError:
            pass

    def test_pep8(self):
        """Test for Pep8 styling."""
        style = pep8.StyleGuide(quiet=True)
        pep = style.check_files(["console.py"])
        self.assertEqual(pep.total_errors, 0, "fix Pep8")

    def test_docstrings(self):
        """Check for the docstrings."""
        self.assertIsNotNone(HBNBCommand.__doc__)
        self.assertIsNotNone(HBNBCommand.emptyline.__doc__)
        self.assertIsNotNone(HBNBCommand.do_quit.__doc__)
        self.assertIsNotNone(HBNBCommand.do_EOF.__doc__)
        self.assertIsNotNone(HBNBCommand.do_create.__doc__)
        self.assertIsNotNone(HBNBCommand.do_show.__doc__)
        self.assertIsNotNone(HBNBCommand.do_destroy.__doc__)
        self.assertIsNotNone(HBNBCommand.do_all.__doc__)
        self.assertIsNotNone(HBNBCommand.do_update.__doc__)
        self.assertIsNotNone(HBNBCommand.default.__doc__)

    def test_emptyline(self):
        """Test for the empty line input."""
        with patch("sys.stdout", new=StringIO()) as file:
            self.HBNB.onecmd("\n")
            self.assertEqual("", file.getvalue())

    # def test_quit(self):
    #     """Test for the quit command input."""
    #     with patch("sys.stdout", new=StringIO()) as file:
    #         self.HBNB.onecmd("quit")
    #         self.assertEqual("", file.getvalue())

    # def test_eof(self):
    #     """Test that EOF quits."""
    #     with patch("sys.stdout", new=StringIO()):
    #         self.assertTrue(self.HBNB.onecmd("EOF"))

    def test_create_errors(self):
        """Test create command errors."""
        with patch("sys.stdout", new=StringIO()) as file:
            self.HBNB.onecmd("create")
            self.assertEqual("** class name missing **\n", file.getvalue())
        with patch("sys.stdout", new=StringIO()) as file:
            self.HBNB.onecmd("create asdfsfsd")
            self.assertEqual("** class doesn't exist **\n", file.getvalue())

    @unittest.skipIf(
        isinstance(models.storage, DBStorage), "Testing DBStorage"
    )
    def test_create(self):
        """Test for the creating command."""
        with patch("sys.stdout", new=StringIO()) as file:
            self.HBNB.onecmd("create User")
            user = file.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as file:
            self.HBNB.onecmd("create State")
            state = file.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as file:
            self.HBNB.onecmd("create Place")
            place = file.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as file:
            self.HBNB.onecmd("create City")
            city = file.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as file:
            self.HBNB.onecmd("create Review")
            review = file.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as file:
            self.HBNB.onecmd("create Amenity")
            amenity = file.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as file:
            self.HBNB.onecmd("all User")
            self.assertIn(user, file.getvalue())
        with patch("sys.stdout", new=StringIO()) as file:
            self.HBNB.onecmd("all State")
            self.assertIn(state, file.getvalue())
        with patch("sys.stdout", new=StringIO()) as file:
            self.HBNB.onecmd("all Place")
            self.assertIn(place, file.getvalue())
        with patch("sys.stdout", new=StringIO()) as file:
            self.HBNB.onecmd("all City")
            self.assertIn(city, file.getvalue())
        with patch("sys.stdout", new=StringIO()) as file:
            self.HBNB.onecmd("all Review")
            self.assertIn(review, file.getvalue())
        with patch("sys.stdout", new=StringIO()) as file:
            self.HBNB.onecmd("all Amenity")
            self.assertIn(amenity, file.getvalue())

    @unittest.skipIf(
        isinstance(models.storage, DBStorage), "Testing DBStorage"
    )
    def test_create_kwargs(self):
        """Test create command with kwargs."""
        with patch("sys.stdout", new=StringIO()) as file:
            call = (
                'create Place city_id="0001" name="My_house" '
                "number_rooms=4 latitude=37.77 longitude=a")

            self.HBNB.onecmd(call)
            place = file.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as file:
            self.HBNB.onecmd("all Place")
            output = file.getvalue()
            self.assertIn(place, output)
            self.assertIn("'city_id': '0001'", output)
            self.assertIn("'name': 'My house'", output)
            self.assertIn("'number_rooms': 4", output)
            self.assertIn("'latitude': 37.77", output)
            self.assertNotIn("'longitude'", output)

    def test_show(self):
        """Test for the show command."""
        with patch("sys.stdout", new=StringIO()) as file:
            self.HBNB.onecmd("show")
            self.assertEqual("** class name missing **\n", file.getvalue())
        with patch("sys.stdout", new=StringIO()) as file:
            self.HBNB.onecmd("show asdfsdrfs")
            self.assertEqual("** class doesn't exist **\n", file.getvalue())
        with patch("sys.stdout", new=StringIO()) as file:
            self.HBNB.onecmd("show BaseModel")
            self.assertEqual("** instance id missing **\n", file.getvalue())
        with patch("sys.stdout", new=StringIO()) as file:
            self.HBNB.onecmd("show BaseModel abcd-123")
            self.assertEqual("** no instance found **\n", file.getvalue())

    def test_destroy(self):
        """Test destroy command input."""
        with patch("sys.stdout", new=StringIO()) as file:
            self.HBNB.onecmd("destroy")
            self.assertEqual("** class name missing **\n", file.getvalue())
        with patch("sys.stdout", new=StringIO()) as file:
            self.HBNB.onecmd("destroy Galaxy")
            self.assertEqual("** class doesn't exist **\n", file.getvalue())
        with patch("sys.stdout", new=StringIO()) as file:
            self.HBNB.onecmd("destroy User")
            self.assertEqual("** instance id missing **\n", file.getvalue())
        with patch("sys.stdout", new=StringIO()) as file:
            self.HBNB.onecmd("destroy BaseModel 12345")
            self.assertEqual("** no instance found **\n", file.getvalue())

    @unittest.skipIf(
        isinstance(models.storage, DBStorage), "Testing DBStorage")
    def test_all(self):
        """Test all command input."""
        with patch("sys.stdout", new=StringIO()) as file:
            self.HBNB.onecmd("all asdfsdfsd")
            self.assertEqual("** class doesn't exist **\n", file.getvalue())
        with patch("sys.stdout", new=StringIO()) as file:
            self.HBNB.onecmd("all State")
            self.assertEqual("[]\n", file.getvalue())


if __name__ == "__main__":
    unittest.main()
