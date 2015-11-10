'''
Author: Shixin Li 

This is the main funtion to run the program with positions set to [1, 10, 100, 1000] and 
num_trials set to 10000. This program will then generate four plots and a results.txt 
'''

from simulation import *
import matplotlib.pyplot as plt
import sys

# main function 
def main():

	initial_input = raw_input('Run a simulation with positions set to [1, 10, 100, 1000] and num_trials set to 10000? Yes or No?\n')

	if initial_input == 'Yes':
		positions = [1, 10, 100, 1000]
		num_trials = 10000

		# create a Simulation object and call the function 
		investment_sim = Simulation(positions, num_trials, 1000)
		daily_return = investment_sim.investment() 

		results = open("results.txt", "w")

		# for loop 
		for i in range(len(daily_return)):

			mean = np.mean(daily_return[i])
			standard_deviation = np.std(daily_return[i])

			# write the results.txt
			results.write("When position is " + str(positions[i]) + "\n")
			results.write("The mean of the daily return is " + str(mean) + "\n")
			results.write("The standard deviation of the daily return is " + str(standard_deviation) + "\n")

			# draw the plots
			results.flush()
			plt.figure()
			plt.hist(daily_return[i],100,range=[-1,1])
			plt.xlim([-1, 1])
			plt.title("The histogram of the result for position " + str(positions[i]))
			plt.savefig("histogram_" + str(positions[i]).zfill(4) + "_pos.pdf")

		results.close()

		print 'The plots and results will be saved'

	elif initial_input == 'No':
		sys.exit()

	else:
		print 'Run again and Please only enter Yes or No next time!'
		sys.exit()


if __name__ == "__main__":
	try:
		main()
	except EOFError:
		pass
	except TypeError:
		pass
	except ZeroDivisionError:
		pass
	except ArithmeticError, OverflowError:
		pass
	except KeyboardInterrupt, ValueError:
		pass 



