#!/usr/bin/python3

import unittest

from models.base import Base


class TestBase(unittest.TestCase):
    def setUp(self):
        self.inst1 = Base()
        self.inst3 = Base()
        self.inst2 = Base(5)

    def test_id(self):
        self.assertEqual(self.inst1.id, 1)
        self.assertEqual(self.inst3.id, 2)
        self.assertEqual(self.inst2.id, 5)

    def test_to_json_string(self):
        self.assertEqual(Base().to_json_string([{}]), "[{}]")
        self.assertEqual(Base().to_json_string([]), "[]")
        dict = {
            'x': 2,
            'width': 10,
            'id': 1,
            'height': 7,
            'y': 8
        }
        self.assertEqual(Base.to_json_string([dict]), '[{"x": 2, "width": 10, "id": 1, "height": 7, "y": 8}]')

    def tearDown(self):
        del self.inst1
        del self.inst2
        del self.inst3
        Base.__nb_objects = 0
