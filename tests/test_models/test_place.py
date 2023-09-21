#!/usr/bin/python3

"""A module to test for city"""
import os
import unittest
import pep8

from models.base_model import BaseModel
from models.city import City


class TestCity(unittest.TestCase):
    """test the city class"""

    @classmethod
    def setUpClass(cls):
        """initiallizes up for test"""
        cls.city = City()
        cls.city.name = "LA"
        cls.city.state_id = "CA"

    @classmethod
    def teardown(cls):

        """test for tear it down"""
        del cls.city

    def tearDown(self):
        """test for teardown"""
        try:
            os.remove("file.json")
        except Exception:
            pass

    def test_pep8_city(self):
        """test for pep8 style"""
        style = pep8.StyleGuide(quiet=True)
        pep = style.check_files(["models/city.py"])
        self.assertEqual(pep.total_errors, 0, "fix pep8")

    def test_attributes_city(self):
        """test for City attributes"""
        self.assertTrue("id" in self.city.__dict__)
        self.assertTrue("created_at" in self.city.__dict__)
        self.assertTrue("updated_at" in self.city.__dict__)
        self.assertTrue("state_id" in self.city.__dict__)
        self.assertTrue("name" in self.city.__dict__)

    def test_is_subclass_city(self):
        """test for City is subclass of Basemodel"""
        self.assertTrue(issubclass(self.city.__class__, BaseModel), True)

    def test_checking_for_docstring_city(self):
        """test for docstrings"""
        self.assertIsNotNone(City.__doc__)
    
    def test_attribute_types_city(self):
        """test attribute type for City"""
        self.assertEqual(type(self.city.name), str)
        self.assertEqual(type(self.city.state_id), str)

    @unittest.skipIf(
        os.getenv("HBNB_TYPE_STORAGE") == "db",
        "This test only work in Filestorage",)

    def test_save_city(self):
        """test if the save"""
        self.city.save()
        self.assertNotEqual(self.city.created_at, self.city.updated_at)

    def test_to_dict_city(self):
        """test if dictionary"""
        self.assertEqual("to_dict" in dir(self.city), True)


if __name__ == "__main__":
    unittest.main()
