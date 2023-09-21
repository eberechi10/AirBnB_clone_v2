#!/usr/bin/python3

"""A module to test for BaseModel"""

import os
import unittest
import pep8

from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """test base model class"""
    @classmethod
    def setUpClass(cls):
        """initialize for the test"""
        cls.base = BaseModel()
        cls.base.name = "Kev"
        cls.base.num = 20

    @classmethod
    def teardown(cls):
        del cls.base

    def tearDown(self):
        """ """
        try:
            os.remove("file.json")
        except Exception:
            pass

    def test_checking_for_docstring_baseModel(self):
        """checking for docstrings"""
        self.assertIsNotNone(BaseModel.__doc__)
        self.assertIsNotNone(BaseModel.__init__.__doc__)
        self.assertIsNotNone(BaseModel.__str__.__doc__)
        self.assertIsNotNone(BaseModel.save.__doc__)
        self.assertIsNotNone(BaseModel.to_dict.__doc__)

    def test_method_basemodel(self):
        """checking if Basemodel have methods"""
        self.assertTrue(hasattr(BaseModel, "__init__"))
        self.assertTrue(hasattr(BaseModel, "save"))
        self.assertTrue(hasattr(BaseModel, "to_dict"))

    def test_pep8_basemodel(self):
        """Test for pep8"""
        style = pep8.StyleGuide(quiet=True)
        pep = style.check_files(['models/base_model.py'])
        self.assertEqual(pep.total_errors, 0, "fix pep8")
    
    def test_init_basemodel(self):
        """test for type BaseModel"""
        self.assertTrue(isinstance(self.base, Basemodel))


if __name__ == "__main__":
    unittest.main()
