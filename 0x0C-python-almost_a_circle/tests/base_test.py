#!/usr/bin/python3

import unittest

from models.base import Base

class TestBase(unittest.TestCase):
	def test_id(self):
		inst1 = Base()
		self.assertEqual(inst1.id, 1)
		inst2 = Base()
		self.assertEqual(inst2.id, 2)
		inst3 = Base(77)
		self.assertEqual(inst3.id, 77)

