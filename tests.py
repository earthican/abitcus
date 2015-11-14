from abitcus import *
import unittest

class SpecieTestCase(unittest.TestCase):
	def setUp(self):
		self.s = Specie(value=10)

	def fee_test_case(self):
		self.assertEqual(self.s.fee, 0.15)

if __name__ == '__main__':
	unittest.main()
