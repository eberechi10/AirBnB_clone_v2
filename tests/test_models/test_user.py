#!/usr/bin/python3

"""A module to test for user class"""

import os
import unittest
import pep8

from models.base_model import BaseModel
from models.user import User


class TestUser(unittest.TestCase):
    """test for the User class"""

    @classmethod
    def setUpClass(cls):
        """ initializes the test"""
        cls.user = User()
        cls.user.first_name = "Kevn"
        cls.user.last_name = "Sook"
        cls.user.email = "sunoob00607@gmamil.com"
        cls.user.password = "secret"

    @classmethod
    def teardown(cls):
        """test for tear it down"""
        del cls.user

    def tearDown(self):
        """test for teardown"""
        try:
            os.remove("file.json")
        except Exception:
            pass

    def test_pep8_user(self):
        """Test for pep8 style"""
        style = pep8.StyleGuide(quiet=True)
        pep = style.check_files(["models/user.py"])
        self.assertEqual(pep.total_errors, 0, "fix pep8")

    def test_for_docstring_user(self):
        """test for docstrings"""
        self.assertIsNotNone(User.__doc__)

    def test_attributes_user(self):
        """TEST FOR User have attributes"""
        self.assertTrue("email" in self.user.__dict__)
        self.assertTrue("id" in self.user.__dict__)
        self.assertTrue("created_at" in self.user.__dict__)
        self.assertTrue("updated_at" in self.user.__dict__)
        self.assertTrue("password" in self.user.__dict__)
        self.assertTrue("first_name" in self.user.__dict__)
        self.assertTrue("last_name" in self.user.__dict__)

    def test_is_subclass_user(self):
        """test if User is subclass of Basemodel"""
        self.assertTrue(issubclass(self.user.__class__, BaseModel), True)

    def test_attribute_types_user(self):
        """test attribute type for User"""
        self.assertEqual(type(self.user.email), str)
        self.assertEqual(type(self.user.password), str)
        self.assertEqual(type(self.user.first_name), str)
        self.assertEqual(type(self.user.first_name), str)

    def test_save_user(self):
        """test if the save works"""
        self.user.save()
        self.assertNotEqual(self.user.created_at, self.user.updated_at)

    def test_to_dict_user(self):
        """test if dictionary works"""
        self.assertEqual("to_dict" in dir(self.user), True)


if __name__ == "__main__":
    unittest.main()
