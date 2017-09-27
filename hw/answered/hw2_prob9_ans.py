# CS 6505 HW2 problem 9
import numpy as np
nan = np.nan

def binary_search_unknown_length(A = [1,2,3,4, nan, nan, nan , nan]):
	# goal is to find index i such that x<A[i] 
	# start at i = 1
	# if x > A[i] then double i 
	# repeat until x <= A[i]; 
	# return x if x == A[i], else return "NO"
	i = 1
	if x == A[i]:
		return x
	while (x  > A[i] and A[i] != np.nan): # check that x > A[i] and A[i] not undefined
		if x > A[i]:
			i = i+2  #keep doing this until we find upper bound for i
					# this i will be increased at most lg(n) times
		else:
			return binary_search_unknown_length(A[0:i]) #binary search on everything up to this i






