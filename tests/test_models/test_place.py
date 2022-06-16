#!/usr/bin/python3
"""Unittest for place.py"""
import unittest
from models.place import Place
from models.base_model import BaseModel
import os


class TestPlace(unittest.TestCase):
    """Class to test place.py"""

    def setUp(self):
        """Sets up the testing environment"""

        self.p1 = Place()
        self.p2 = Place()
        self.p2.number_rooms = 2
        self.p2.name = "House"

    def tearDown(self):
        """Tears down the testing environment"""

        del self.p1
        del self.p2
        if os.path.exists("file.json"):
            os.remove("file.json")

    def test_checks_attributes(self):
        """Checks for class specific attributes"""

        self.assertTrue(hasattr(Place(), "city_id"))
        self.assertTrue(hasattr(Place(), "user_id"))
        self.assertTrue(hasattr(Place(), "name"))
        self.assertTrue(hasattr(Place(), "description"))
        self.assertTrue(hasattr(Place(), "number_rooms"))
        self.assertTrue(hasattr(Place(), "number_bathrooms"))
        self.assertTrue(hasattr(Place(), "max_guest"))
        self.assertTrue(hasattr(Place(), "price_by_night"))
        self.assertTrue(hasattr(Place(), "latitude"))
        self.assertTrue(hasattr(Place(), "longitude"))
        self.assertTrue(hasattr(Place(), "amenity_ids"))

    def test_new_instances(self):
        """Checks that new instances were created"""

        self.assertTrue(self.p1)
        self.assertTrue(self.p2)

    def test_new_instances_attribute_creation(self):
        """Checks that new instances have designated attributes"""

        self.assertIn("number_rooms", self.p2.__dict__)
        self.assertEqual(self.p2.number_rooms, 2)
        self.assertIn("name", self.p2.__dict__)
        self.assertEqual(self.p2.name, "House")

    def test_non_existant_instance(self):
        """Checks for a non-existant instance"""

        self.p3 = Place()
        self.assertIsInstance(self.p3, Place)

    def test_inheritence(self):
        """Checks to make sure Place inherits from BaseModel"""

        self.assertTrue(issubclass(Place, BaseModel))
