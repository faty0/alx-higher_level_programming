#!/usr/bin/python3

import unittest

from models.rectangle import Rectangle
from models.base import Base


class TestRectangle(unittest.TestCase):
    def setUp(self):
        self.rec1 = Rectangle(5, 6, id=4)
        self.rec2 = Rectangle(4, 8)
        self.rec3 = Rectangle(3, 9, 3, 3)
        self.rec4 = Rectangle(2, 2, 3, 4, 5)

    def test_id(self):
        self.assertEqual(self.rec1.id, 4)
        self.assertEqual(self.rec2.id, 9)
        self.assertEqual(self.rec3.id, 10)
        self.assertEqual(self.rec4.id, 5)

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

    def test_display(self):
        dis = "#####\n#####\n#####\n#####\n#####\n#####"
        self.assertEqual(self.rec1.display(), dis)
        dis = "####\n####\n####\n####\n####\n####\n####\n####"
        self.assertEqual(self.rec2.display(), dis)
        dis = "\n\n\n   ###\n   ###\n   ###\n   ###\n   ###\n   ###\n   ###\n   ###\n   ###"
        self.assertEqual(self.rec3.display(), dis)
        dis = "\n\n\n\n   ##\n   ##"
        self.assertEqual(self.rec4.display(), dis)

    def test_str(self):
        self.assertEqual(self.rec1.__str__(), "[Rectangle] (4) 0/0 - 5/6")
        self.assertEqual(self.rec2.__str__(), "[Rectangle] (11) 0/0 - 4/8")
        self.assertEqual(self.rec3.__str__(), "[Rectangle] (12) 3/3 - 3/9")
        self.assertEqual(self.rec4.__str__(), "[Rectangle] (5) 3/4 - 2/2")

    def test_update(self):
        self.rec1.update(1, 1, 1, 3, 4)
        self.assertEqual(self.rec1.__str__(), "[Rectangle] (1) 3/4 - 1/1")
        self.rec2.update(1, 1)
        self.assertEqual(self.rec2.__str__(), "[Rectangle] (1) 0/0 - 1/8")
        self.rec3.update(1, 1, 1, 0)
        self.assertEqual(self.rec3.__str__(), "[Rectangle] (1) 0/3 - 1/1")
        self.rec3.update(89)
        self.assertEqual(self.rec3.__str__(), "[Rectangle] (89) 0/3 - 1/1")
        self.rec3.update(id=77, width=2, height=2, x=8, y=8)
        self.assertEqual(self.rec3.__str__(), "[Rectangle] (77) 8/8 - 2/2")
        self.rec3.update(height=6, x=10)
        self.assertEqual(self.rec3.__str__(), "[Rectangle] (77) 10/8 - 2/6")

    def tearDown(self):
        self.squ1 = None
        self.squ2 = None
        self.squ3 = None
        self.squ4 = None
        self.squ5 = None
        self.squ6 = None
        Base.__nb_objects = 0
