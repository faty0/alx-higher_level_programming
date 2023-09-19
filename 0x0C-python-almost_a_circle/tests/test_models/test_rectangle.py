#!/usr/bin/python3

import unittest

from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
	def setUp(self):
		rec1 = Rectangle()
		rec2 = Rectangle()
		rec3 = Rectangle()
		rec4 = Rectangle()

	def test_id(self):
		
