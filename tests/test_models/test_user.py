#!/usr/bin/python3
""" Unittest for User """
import unittest
from datetime import datetime
from models.user import User
from models.base_model import BaseModel
import os


class TestUser(unittest.TestCase):
    """ Runs Test for User.py """

    def setUp(self):
        """ Sets Up Testing Environment """

        self.a = User()
        self.b = User()

        self.attributes = {
            "User":
            {"email": str,
             "password": str,
             "first_name": str,
             "last_name": str},
        }

    def test_createNewUser(self):
        """Checks for successful creation of new user"""

        self.assertTrue(self.a)

    def test_createUserId(self):
        """Checks ID is present"""

        self.assertTrue(self.a.id)

    def test_uniqueUserId(self):
        """Checks IDs against eachother"""

        self.assertNotEqual(self.a.id, self.b.id)

    def test_Instantation(self):
        """Checks that User inherits from BaseModel"""

        self.assertIsInstance(self.a, User)
        self.assertTrue(issubclass(type(self.a), BaseModel))
        self.assertEqual(str(type(self.a)), "<class 'models.user.User'>")

    def test_toDict(self):
        """Checks output when using to_dict()"""

        self.assertFalse("__class__" in self.a.__dict__)
        self.assertFalse("__class__" in self.b.__dict__)
        dict_check = self.a.to_dict()
        self.assertTrue("__class__" in dict_check)
        self.assertFalse("__class__" in self.b.__dict__)

    def test_setting_attributeValues(self):
        """Checks you can change the name"""

        self.a.first_name = "Marc"
        self.a.last_name = "Cav"
        self.a.email = "mark@test.com"
        self.a.password = "pass"
        self.assertTrue(self.a.first_name, "Marc")
        self.assertTrue(self.a.last_name, "Cav")
        self.assertTrue(self.a.email, "mark@test.com")
        self.assertTrue(self.a.password, "pass")

    def test_attribute_and_values(self):
        """Checks through attributes"""

        attributes = self.attributes["User"]
        mark = User()
        for k, v in attributes.items():
            self.assertTrue(hasattr(mark, k))
            self.assertEqual(type(getattr(mark, k, None)), v)
            self.assertTrue(type(v), str)

    def test_compare_create_and_update(self):
        """Makes sure create and update are slightly different"""

        self.assertNotEqual(self.a.created_at, self.b.updated_at)

    def test_updateAt_updates(self):
        """Makes sure updated_at updates"""

        tmp = self.a.updated_at
        self.a.save()
        self.assertNotEqual(tmp, self.a.updated_at)

    def test_consistent_idLength(self):
        """Checks to make sure id is the right amount of characters"""

        self.assertTrue(len(self.a.id), 36)
        self.assertTrue(len(self.b.id), 36)

    def test_diff_ids(self):
        """Checks to make sure id is the right amount of characters"""

        self.assertNotEqual(self.a.id, self.b.id)

    def test_to_dict(self):
        """Tests the to_dict() method"""

        self.assertEqual(dict, type(self.a.to_dict()))
        self.assertEqual(dict, type(self.b.to_dict()))

    def tearDown(self):
        """Tears down testing environment"""

        if os.path.exists("file.json"):
            os.remove("file.json")
