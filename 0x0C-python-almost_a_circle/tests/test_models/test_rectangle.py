#!/usr/bin/python3

import unittest

from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    def setUp(self):
        self.rec1 = Rectangle(5, 6, id=4)
        self.rec2 = Rectangle(4, 8)
        self.rec3 = Rectangle(3, 9, 3, 3)
        self.rec4 = Rectangle(2, 2, 3, 4, 5)

    """ def test_id(self):
        self.assertEqual(self.rec1.id, 4)
        self.assertEqual(self.rec2.id, 3)
        self.assertEqual(self.rec3.id, 4)
        self.assertEqual(self.rec4.id, 5) """

    def test_width(self):
        self.assertEqual(self.rec1.width, 5)
        self.assertEqual(self.rec2.width, 4)
        self.assertEqual(self.rec3.width, 3)
        self.assertEqual(self.rec4.width, 2)
        with self.assertRaises(TypeError):
            rec5 = Rectangle('w', 2, 3, 4, 5)
        with self.assertRaises(ValueError):
            rec6 = Rectangle(-7, 2, 3, 4, 5)
        self.rec1.width = 10
        self.rec2.width = 20
        self.rec3.width = 30
        self.rec4.width = 40
        self.assertEqual(self.rec1.width, 10)
        self.assertEqual(self.rec2.width, 20)
        self.assertEqual(self.rec3.width, 30)
        self.assertEqual(self.rec4.width, 40)

    def test_height(self):
        self.assertEqual(self.rec1.height, 6)
        self.assertEqual(self.rec2.height, 8)
        self.assertEqual(self.rec3.height, 9)
        self.assertEqual(self.rec4.height, 2)
        with self.assertRaises(TypeError):
            rec5 = Rectangle(2, 'h', 3, 4, 5)
        with self.assertRaises(ValueError):
            rec6 = Rectangle(7, -2, 3, 4, 5)
        self.rec1.height = 10
        self.rec2.height = 20
        self.rec3.height = 30
        self.rec4.height = 40
        self.assertEqual(self.rec1.height, 10)
        self.assertEqual(self.rec2.height, 20)
        self.assertEqual(self.rec3.height, 30)
        self.assertEqual(self.rec4.height, 40)

    def test_x(self):
        self.assertEqual(self.rec1.x, 0)
        self.assertEqual(self.rec2.x, 0)
        self.assertEqual(self.rec3.x, 3)
        self.assertEqual(self.rec4.x, 3)
        with self.assertRaises(TypeError):
            self.rec5 = Rectangle(2, 2, 'x', 4, 5)
        with self.assertRaises(ValueError):
            rec6 = Rectangle(7, 2, -3, 4, 5)
        self.rec1.x = 1
        self.rec2.x = 2
        self.rec3.x = 4
        self.rec4.x = 5
        self.assertEqual(self.rec1.x, 1)
        self.assertEqual(self.rec2.x, 2)
        self.assertEqual(self.rec3.x, 4)
        self.assertEqual(self.rec4.x, 5)

    def test_y(self):
        self.assertEqual(self.rec1.y, 0)
        self.assertEqual(self.rec2.y, 0)
        self.assertEqual(self.rec3.y, 3)
        self.assertEqual(self.rec4.y, 4)
        with self.assertRaises(TypeError):
            self.rec5 = Rectangle(2, 2, 3, 'y', 5)
        with self.assertRaises(ValueError):
            rec6 = Rectangle(7, 2, 3, -4, 5)
        self.rec1.y = 1
        self.rec2.y = 2
        self.rec3.y = 4
        self.rec4.y = 5
        self.assertEqual(self.rec1.y, 1)
        self.assertEqual(self.rec2.y, 2)
        self.assertEqual(self.rec3.y, 4)
        self.assertEqual(self.rec4.y, 5)

    def test_area(self):
        self.assertEqual(self.rec1.area(), 30)
        self.assertEqual(self.rec2.area(), 32)
        self.assertEqual(self.rec3.area(), 27)
        self.assertEqual(self.rec4.area(), 4)

    def tearDown(self):
        pass
