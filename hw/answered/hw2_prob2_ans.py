# CS 6505 HW2 problem 2 
import numpy as np
NIL = np.nan

def hotel_trip(a):
	# input: a, a list of hotel mile posts 
	# output: the best optimal cost, and the best sequence for that 

	T = [] # initialize table
	
	T[0] = 0 # base case

	best_cost_path = []

	for i in range(1, n):
		best_cost = infinity
		best_j_for_this_i = NIL

		for j in range(0, i-1):
			cost_this_i_to_this_j = T[j] + (200-(a[j]- a[i]))^2 
			if cost_this_i_to_this_j < best_cost:
				best_cost = cost_this_i_to_this_j
				best_j_for_this_i = j
		
		T[i] = best_cost #record best cost to point i
		best_cost_path.append(best_j_for_this_i) #append to optimal seq up to point i


	return T[n], best_cost_path

