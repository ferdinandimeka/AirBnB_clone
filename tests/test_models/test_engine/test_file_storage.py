#!/usr/bin/python3
"""Module that holds tests for file_storage.py"""
import unittest
import json
import models
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
import os


class TestFileStorage(unittest.TestCase):
    """Class to test file_storage"""

    def setUp(self):
        """Sets up the class test"""

        self.b1 = BaseModel()
        self.a1 = Amenity()
        self.c1 = City()
        self.p1 = Place()
        self.r1 = Review()
        self.s1 = State()
        self.u1 = User()
        self.storage = FileStorage()
        if os.path.exists("file.json"):
            pass
        else:
            os.mknod("file.json")

    def tearDown(self):
        """Tears down the testing environment"""

        del self.b1
        del self.a1
        del self.c1
        del self.p1
        del self.r1
        del self.s1
        del self.u1
        del self.storage
        if os.path.exists("file.json"):
            os.remove("file.json")

    def test_storage_all(self):
        """Checks storage.all() is not empty"""

        self.assertIsNotNone(self.storage.all())

    def test_storage_all_contents(self):
        """Checks to make sure storage.all() contains instances"""

        self.assertIn("{}.{}".format(self.b1.__class__.__name__, self.b1.id),
                      models.storage.all())
        self.assertIn("{}.{}".format(self.a1.__class__.__name__, self.a1.id),
                      models.storage.all())
        self.assertIn("{}.{}".format(self.c1.__class__.__name__, self.c1.id),
                      models.storage.all())
        self.assertIn("{}.{}".format(self.p1.__class__.__name__, self.p1.id),
                      models.storage.all())
        self.assertIn("{}.{}".format(self.r1.__class__.__name__, self.r1.id),
                      models.storage.all())
        self.assertIn("{}.{}".format(self.s1.__class__.__name__, self.s1.id),
                      models.storage.all())
        self.assertIn("{}.{}".format(self.u1.__class__.__name__, self.u1.id),
                      models.storage.all())

    def test_storage_all_type(self):
        """Checks the type of storage.all()"""

        self.assertEqual(dict, type(self.storage.all()))


if __name__ == "__main__":
    unittest.main()
