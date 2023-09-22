#!/usr/bin/python3

"""A module to test for state"""

import os
import unittest
import pep8

from models.base_model import BaseModel
from models.state import State


class TestState(unittest.TestCase):
    """test for the State class"""
    @classmethod
    def setUpClass(cls):
        """ initializes the test"""
        cls.state = State()
        cls.state.name = "CA"

    @classmethod
    def teardown(cls):
        """test for tear it down"""
        del cls.state

    def tearDown(self):
        """test for teardown"""
        try:
            os.remove("file.json")
        except Exception:
            pass

    def test_pep8_review(self):
        """test for pep8 style"""
        style = pep8.StyleGuide(quiet=True)
        pep = style.check_files(['models/state.py'])
        self.assertEqual(pep.total_errors, 0, "fix pep8")

    def test_attributes_state(self):
        """test for State attributes"""
        self.assertTrue('id' in self.state.__dict__)
        self.assertTrue('created_at' in self.state.__dict__)
        self.assertTrue('updated_at' in self.state.__dict__)
        self.assertTrue('name' in self.state.__dict__)

    def test_is_subclass_state(self):
        """test for State is subclass of BaseModel"""
        self.assertTrue(issubclass(self.state.__class__, BaseModel), True)

    def test_attribute_types_state(self):
        """test attribute type for State"""
        self.assertEqual(type(self.state.name), str)

    def test_checking_for_docstring_state(self):
        """test for docstrings"""
        self.assertIsNotNone(State.__doc__)

    @unittest.skipIf(
        os.getenv('HBNB_TYPE_STORAGE') == 'db',
        "test only work in Filestorage")
    def test_save_state(self):
        """test if the saving"""
        self.state.save()
        self.assertNotEqual(self.state.created_at, self.state.updated_at)

    def test_to_dict_state(self):
        """test if dictionary works"""
        self.assertEqual('to_dict' in dir(self.state), True)


if __name__ == "__main__":
    unittest.main()
