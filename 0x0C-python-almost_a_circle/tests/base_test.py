import unittest

class TestBase(unittest.TestCase):
	def setUp(self):
		self.inst1 = Base()
		self.inst2 = Base(5)
		self.inst3 = Base()
		self.inst4 = Base()

	def test_id(self):
		self.assertEqual(inst1.id, 1)
		self.assertEqual(inst2.id, 5)
		self.assertEqual(inst3.id, 2)
		self.assertEqual(inst4.id, 3)
