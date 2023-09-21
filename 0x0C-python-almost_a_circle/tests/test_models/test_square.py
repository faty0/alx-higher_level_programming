#!/usr/bin/python3

import unittest

from models.square import Square
from models.base import Base


class TestSquare(unittest.TestCase):
    def setUp(self):
        self.squ1 = Square(5, 6, id=4)
        self.squ2 = Square(4, 8)
        self.squ3 = Square(3, 9, 3, 3)
        self.squ4 = Square(2)

    def test_id(self):
        self.assertEqual(self.squ1.id, 4)
        self.assertEqual(self.squ2.id, 23)
        self.assertEqual(self.squ3.id, 3)
        self.assertEqual(self.squ4.id, 24)

    def test_width(self):
        self.assertEqual(self.squ1.width, 5)
        self.assertEqual(self.squ2.width, 4)
        self.assertEqual(self.squ3.width, 3)
        self.assertEqual(self.squ4.width, 2)
        with self.assertRaises(TypeError):
            squ5 = Square('w', 2, 3, 4)
        with self.assertRaises(ValueError):
            squ6 = Square(-7, 2, 3, 4)

    def test_height(self):
        self.assertEqual(self.squ1.height, 5)
        self.assertEqual(self.squ2.height, 4)
        self.assertEqual(self.squ3.height, 3)
        self.assertEqual(self.squ4.height, 2)
        with self.assertRaises(TypeError):
            squ5 = Square(6, 'h', 3, 4)
        with self.assertRaises(ValueError):
            squ6 = Square(7, -2, 3, 4)

    def test_x(self):
        self.assertEqual(self.squ1.x, 6)
        self.assertEqual(self.squ2.x, 8)
        self.assertEqual(self.squ3.x, 9)
        self.assertEqual(self.squ4.x, 0)
        with self.assertRaises(TypeError):
            self.squ5 = Square(2, 'x', 4)
        with self.assertRaises(ValueError):
            squ6 = Square(7, 2, -3, 4)

    def test_y(self):
        self.assertEqual(self.squ1.y, 0)
        self.assertEqual(self.squ2.y, 0)
        self.assertEqual(self.squ3.y, 3)
        self.assertEqual(self.squ4.y, 0)
        with self.assertRaises(TypeError):
            self.squ5 = Square(2, 4, 'y')
        with self.assertRaises(ValueError):
            squ6 = Square(7, 3, -4)

    def test_size(self):
        self.assertEqual(self.squ1.size, 5)
        self.assertEqual(self.squ2.size, 4)
        self.assertEqual(self.squ3.size, 3)
        self.assertEqual(self.squ4.size, 2)
        with self.assertRaises(TypeError):
            squ5 = Square('w', 2, 3)
        with self.assertRaises(ValueError):
            squ6 = Square(-7, 2, 3)
        self.squ1.size = 10
        self.squ2.size = 20
        self.squ3.size = 30
        self.squ4.size = 40
        self.assertEqual(self.squ1.size, 10)
        self.assertEqual(self.squ2.size, 20)
        self.assertEqual(self.squ3.size, 30)
        self.assertEqual(self.squ4.size, 40)

    def tearDown(self):
        self.squ1 = None
        self.squ2 = None
        self.squ3 = None
        self.squ4 = None
        self.squ5 = None
        self.squ6 = None
        Base.__nb_objects = 0