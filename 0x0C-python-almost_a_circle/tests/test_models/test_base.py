#!/usr/bin/python3
"""
Unittest for class Base
"""
import unittest
import os
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBase(unittest.TestCase):
    """Testing Base
    """
    def tearDown(self):
        """Tears down obj count
        """
        Base._Base__nb_objects = 0
        self.assertEqual(Base._Base__nb_objects, 0)

    def test_instance(self):
        """Test instantiation
        """
        o1 = Base()
        o2 = Base(9)
        o3 = Base(9.5)
        o4 = Base(float('inf'))
        o5 = Base("string")
        o6 = Base(["list", 4, 2.5])
        o7 = Base(None)

        self.assertEqual(o1.id, 1)
        self.assertEqual(o2.id, 9)
        self.assertEqual(o3.id, 9.5)
        self.assertEqual(o4.id, float('inf'))
        self.assertEqual(o5.id, "string")
        self.assertEqual(o6.id, ["list", 4, 2.5])
        self.assertEqual(o7.id, 2)
        self.assertEqual(Base._Base__nb_objects, 2)

if __name__ == '__main__':
    unittest.main()
