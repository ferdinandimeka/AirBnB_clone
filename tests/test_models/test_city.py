#!/usr/bin/python3
"""Unittest for City class"""
import unittest
from models.city import City
from models.base_model import BaseModel
import os


class TestCity(unittest.TestCase):
    """Runs tests for City class"""

    def setUp(self):
        """Sets up the testing environment"""

        self.c1 = City()
        self.c2 = City()
        self.c2.name = "Santa_Cruz"

    def tearDown(self):
        """Breaks down the testing environment"""

        del self.c1
        del self.c2
        if os.path.exists("file.json"):
            os.remove("file.json")

    def test_checks_attributes(self):
        """Checks for class specific attributes"""

        self.assertTrue(hasattr(City(), "state_id"))
        self.assertTrue(hasattr(City(), "name"))

    def test_new_instances(self):
        """Checks that new instances were created"""

        self.assertTrue(self.c1)
        self.assertTrue(self.c2)

    def test_new_instances_attribute_creation(self):
        """Checks that new instances have designated attributes"""

        self.assertIn("name", self.c2.__dict__)
        self.assertEqual(self.c2.name, "Santa_Cruz")

    def test_non_existant_instance(self):
        """Checks for a non-existant instance"""

        self.c3 = City()
        self.assertIsInstance(self.c3, City)

    def test_inheritence(self):
        """Checks to make sure City inherits from BaseModel"""

        self.assertTrue(issubclass(City, BaseModel))
