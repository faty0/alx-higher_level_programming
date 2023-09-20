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

    def tearDown(self):
        pass
