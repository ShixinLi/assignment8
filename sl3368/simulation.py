import numpy as np 

class Simulation():

	'''
	class Simulation takes inputs postions, num_trials, and budget. It also has
	a function investment
	'''

	def __init__(self, positions, num_trials, budget):

		self.positions = positions
		self.num_trials = num_trials

		if budget >= 0:		
			self.budget = budget
		else:
			raise ValueError('budget cannot be negative')

	# A function used to calculate the outcome of the investment for each day 
	def investment(self):

		daily_ret = []

		for position in self.positions:

			position_value = self.budget / position 
			cumu_ret = []

			for trial in range(self.num_trials):

				# number of 1s, representing the number of times we gain.
				revenue_numbers = (np.random.choice([0, 1], size = position, p = [0.49, 0.51])).sum()

				cumu_ret.append(revenue_numbers*position_value*2)

			daily = [(cumu/float(self.budget)) - 1 for cumu in cumu_ret] # calculate daily returns 
			daily_ret.append(daily)

		return daily_ret



