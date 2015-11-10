import unittest
from unittest import TestCase
from simulation import *

''' test for assignment8'''

class AssignmentTest(TestCase):

	def setUp(self):
		pass

	# test the value of the budget 
	def test_budget(self):

		positions = [1, 10, 100, 1000]
		num_trials = 10000

		test = Simulation(positions, num_trials, 1000)
		self.assertEqual(test.budget, 1000)

	# test the ValueError when the budget is negative 
	def test_negative_budget(self):

		positions = [1, 10, 100, 1000]
		num_trials = 10000

		with self.assertRaises(ValueError):

			Simulation(positions, num_trials, -1)

if __name__ == '__main__':
	unittest.main()

	