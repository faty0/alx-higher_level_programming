import unittest
max_integr = __import__("6-max_integer").max_integer

class TestMaxInteger(unittest.TestCase):

    def test_max_integer(self):
        self.assertEqual(max_integr([1, 2, 3, 4]), 4)
        self.assertEqual(max_integr([4, 3, 2, 1]), 4)
        self.assertEqual(max_integr([0, 3, 4, 2, 1]), 4)
        self.assertEqual(max_integr([-1, 0, 1, 2, 3, 4]), 4)
        self.assertEqual(max_integr([1, 2, 3, -7, 4]), 4)
        self.assertEqual(max_integr([1.55, 2, 3.50, -7, 4]), 4)
        self.assertEqual(max_integr([1.55, 2, 3.50, -7.50, 4]), 4)
        self.assertEqual(max_integr([]), None)
        self.assertEqual(max_integr(), None)
        self.assertRaises(TypeError, max_integr, ["a", 3, 4])
