#!/usr/bin/python3
"""Unittest for BaseModel class"""
import unittest
from models.base_model import BaseModel
from datetime import datetime
from time import sleep
import os


class TestBaseModel(unittest.TestCase):
    """Runs tests for base_model.py"""

    def setUp(self):
        """Sets up testing environment"""

        self.b1 = BaseModel()
        self.b2 = BaseModel()

    def tearDown(self):
        """Breaks down the testing environment"""

        del self.b1
        del self.b2
        if os.path.exists("file.json"):
            os.remove("file.json")

    def test_create(self):
        """Tests the creation of a BaseModel class"""

        self.assertTrue(self.b1)
        self.assertTrue(self.b2)

    def test_id_check(self):
        """Checks for ID and compares them"""

        self.assertNotEqual(self.b1.id, self.b2.id)

    def test_attr_check(self):
        """Checks for user created attributes"""

        self.b1.name = "Marc"
        self.b2.name = "Tywan"
        self.assertEqual(self.b1.name, "Marc")
        self.assertEqual(self.b2.name, "Tywan")
        self.assertNotEqual(self.b1.name, self.b2.name)

    def test_toDict(self):
        """Checks output when using to_dict()"""

        self.assertFalse("__class__" in self.b1.__dict__)
        self.assertFalse("__class__" in self.b2.__dict__)
        dict_check = self.b1.to_dict()
        self.assertTrue("__class__" in dict_check)
        self.assertFalse("__class__" in self.b2.__dict__)

    def test_change_name(self):
        """Checks you can change the name"""

        self.b1.name = "Marc"
        self.b2.name = "Tywan"
        self.b1.name = "Rhulad"
        self.assertTrue(self.b1.name, "Rhulad")
        self.assertTrue(self.b2.name, "Tywan")

    def test_compare_create_and_update(self):
        """Makes sure create and update are slightly different"""

        self.assertNotEqual(self.b1.created_at, self.b1.updated_at)

    def test_updateAt_updates(self):
        """Makes sure updated_at updates"""

        tmp = self.b1.updated_at
        self.b1.save()
        self.assertNotEqual(tmp, self.b1.updated_at)

    def test_id_length(self):
        """Checks to make sure id is the right amount of characters"""

        self.assertTrue(len(self.b1.id), 36)
        self.assertTrue(len(self.b2.id), 36)

    def test_user_attr(self):
        """Checks to see if a user created attribute is updated"""

        self.assertFalse("number" in self.b1.__dict__)
        self.assertFalse("number" in self.b2.__dict__)
        self.b1.number = 22
        self.assertTrue("number" in self.b1.__dict__)
        self.assertFalse("number" in self.b2.__dict__)

    def test_to_dict(self):
        """Tests the to_dict() method"""

        self.assertEqual(dict, type(self.b1.to_dict()))

    def test_to_dict_contents(self):
        """Tests that the correct keys are being added to to_dict()"""

        self.assertIn("created_at", self.b1.to_dict())
        self.assertIn("updated_at", self.b1.to_dict())
        self.assertIn("__class__", self.b1.to_dict())
        self.assertNotIn("name", self.b1.to_dict())
        self.b1.name = "Marc"
        self.assertIn("name", self.b1.to_dict())

    def test_two_dicts_one_instance(self):
        """Makes sure to_dict() and __dict__ are not equal"""

        self.assertNotEqual(self.b1.to_dict(), self.b1.__dict__)

    def test_created_at_updated_at_type(self):
        """Checks that created_at and updated_at are of datetime type"""

        self.assertEqual(datetime, type(self.b1.created_at))
        self.assertEqual(datetime, type(self.b1.updated_at))
        self.assertEqual(datetime, type(self.b2.created_at))
        self.assertEqual(datetime, type(self.b2.updated_at))

    def test_id_type(self):
        """Checks id is of the string type"""

        self.assertEqual(str, type(BaseModel().id))
        self.assertEqual(str, type(self.b1.id))
        self.assertEqual(str, type(self.b2.id))

    def test_created_at_type(self):
        """Check created_at is of the datetime type"""

        self.assertEqual(datetime, type(BaseModel().created_at))
        self.assertEqual(datetime, type(self.b1.created_at))
        self.assertEqual(datetime, type(self.b2.created_at))

    def test_updated_at_type(self):
        """Check updated_at is of the datetime type"""

        self.assertEqual(datetime, type(BaseModel().updated_at))
        self.assertEqual(datetime, type(self.b1.updated_at))
        self.assertEqual(datetime, type(self.b2.updated_at))

    def test_kwarg_creation(self):
        """Tests when passing attribute values through kwargs"""

        b3 = BaseModel(id="1212")
        self.assertEqual(b3.id, "1212")

    def test_extra_arg_for_class_creation(self):
        """Checks if extra arg is passed through  when creating an instance"""

        with self.assertRaises(NameError) as e:
            b3 = BaseModel(friend)
        excep = e.exception
        self.assertEqual(str(excep), "name 'friend' is not defined")

    def test_multiplie_args_for_to_dict(self):
        """Checks for when to_dict() receives too many arguments"""

        with self.assertRaises(TypeError) as e:
            self.b1.to_dict("Greetings")
        excep = e.exception
        self.assertEqual(str(excep), "to_dict() takes 1 positional argument " +
                         "but 2 were given")

    def test_multiple_args_for_save(self):
        """Checks for when save() receives too many arguments"""

        with self.assertRaises(TypeError) as e:
            self.b1.save(22)
        excep = e.exception
        self.assertEqual(str(excep), "save() takes 1 positional argument " +
                         "but 2 were given")
        with self.assertRaises(TypeError) as e2:
            self.b2.save("hi")
        excep2 = e2.exception
        self.assertEqual(str(excep2), "save() takes 1 positional argument " +
                         "but 2 were given")

    def test_file(self):
        """Tests that info is saved to file"""

        b3 = BaseModel()
        b3.save()
        with open("file.json", "r") as f:
            self.assertIn(b3.id, f.read())

    def test_pass_in_dict(self):
        """Checks when a dictionary is passed in for new instance"""

        self.b2.name = "Rhulad"
        self.b2.zodiac = "Scorpio"
        my_dict = self.b2.to_dict()
        b4 = BaseModel(**my_dict)
        self.assertEqual(self.b2.id, b4.id)
        self.assertEqual(self.b2.created_at, b4.created_at)
        self.assertEqual(self.b2.updated_at, b4.updated_at)
        self.assertEqual(self.b2.name, b4.name)
        self.assertEqual(self.b2.zodiac, b4.zodiac)
