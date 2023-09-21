#!/usr/bin/python3

""" A module to test for amenity"""

import os
import unittest
import pep8

from models.amenity import Amenity
from models.base_model import BaseModel


class TestAmenity(unittest.TestCase):
    """Initialie the test for the Amenity class"""
    @classmethod
    def setUpClass(cls):
        cls.amenity = Amenity()
        cls.amenity.name = "Breakfast"

    @classmethod
    def teardown(cls):
        """test tear it down"""
        del cls.amenity

    def tearDown(self):
        """ """
        try:
            os.remove("file.json")
        except Exception:
            pass

    def test_pep8_amenity(self):
        """Tests pep8 style"""
        style = pep8.StyleGuide(quiet=True)
        pep = style.check_files(['models/amenity.py'])
        self.assertEqual(pep.total_errors, 0, "fix pep8")

    def test_is_subclass_amenity(self):
        """test if Amenity is subclass of Basemodel"""
        self.assertTrue(issubclass(self.amenity.__class__, BaseModel), True)

    def test_attribute_types_amenity(self):
        """test attribute type for Amenity"""
        self.assertEqual(type(self.amenity.name), str)

    @unittest.skipIf(
        os.getenv('HBNB_TYPE_STORAGE') == 'db',
        "This test only work in Filestorage")
    def test_save_amenity(self):
        self.amenity.save()
        self.assertNotEqual(self.amenity.created_at, self.amenity.updated_at)

    def test_checking_for_docstring_amenity(self):
        """checking for docstrings"""
        self.assertIsNotNone(Amenity.__doc__)

    def test_attributes_amenity(self):
        """A module to vcheck for amenity attibutes"""
        self.assertTrue('id' in self.amenity.__dict__)
        self.assertTrue('created_at' in self.amenity.__dict__)
        self.assertTrue('updated_at' in self.amenity.__dict__)
        self.assertTrue('name' in self.amenity.__dict__)
   
    def test_to_dict_amenity(self):
        """ test for the dictionary works"""
        self.assertEqual('to_dict' in dir(self.amenity), True)


if __name__ == "__main__":
    unittest.main()
