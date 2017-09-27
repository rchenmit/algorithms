# CS 6505 HW2 problem 4 
# coin changing problem

from numpy import min
import numpy as np
infinity = np.infty

## VARIANT A

def coin_change_a(x , v):
	# inputs:
	# 	x: array of coin denominations
	#	v: value you want to make
	# output:
	#	minimum number of coins whose total value is v

	## declare lookup table T 
	n = len(x) # n= number of different coins

	T[0, 0] = 0
	for j in range(1,v):
		T[0,j] = infinity
	for i in range(1, n) 
		for j in range(1, v):
			if x[i] <= j:
				T(i,j) = min( [ T(i-1, j-m*x[i])+m, ... T(i-1, j) ]) , such that j = m*x[i]
														  	   # the best way to make value j is 
															   # either simply add current coin i,
															   # i.e., T(i-1, j-x[i])+ 1
															   # OR, use whatever best combo of 
															   # coins up to last coin i-1 that 
															   # still yielded value j
															   # i.e., T(i-1, j)
			else:
				T(i,j) = T(i-1, j) # if current coin bigger than 
								   # target value j, then you can only use 
								   # whatever best combo up to x_{i-1} is
	return T(n,v) # return the min number of coins 
				  # from x1...xn that yield value v



## VARIANT B
## also finds number of coins of each needed to make value v

def coin_change_b( x , v ):
	# inputs:
	# 	x: array of coin denominations
	#	v: value you want to make
	# output:
	#	min_coins = minimum number of coins whose total value is v
	#	l_num_each_coin = array ( n elts) of number of coins from x_1 ... x_n
	#

	## declare lookup table T 
	n = len(x) # n= number of different coins
	l_num_each_coin = []       # initialize list of coin counts
	for i in range(1, n): 		
		l_num_each_coin[i] = 0 #initialize coin counts to 0

	T[0, 0] = 0
	for j in range(1,v):
		T[0,j] = infinity
	for i in range(1, n) 
		for j in range(1, v):
			if x[i] <= j:
				T(i,j) = min( [ T(i-1, j-m*x[i])+m, ... T(i-1, j) ]) , such that j = m*x[i]
															   # the best way 
															   # to make value j is 
															   # either simply add any number m of current coin i,
															   # i.e., T(i-1, j-x[i])+ 1
															   # OR, use whatever best combo of 
															   # coins up to last coin i-1 that 
															   # still yielded value j
															   # i.e., T(i-1, j)
				if T(i-1, j- m * x[i])+ m <  T(i-1, j): # 
					print "add m of coin i"
					l_num_each_coin[i] += 1 # add one of coin i
				else: #	
					print "do nothing" # don't add any new coins because there's already a
											# more optimal solution involving coins x1 to x_{i-1}
			else:
				T(i,j) = T(i-1, j) # if current coin bigger than 
								   # target value j, then you can only use 
								   # whatever best combo up to x_{i-1} is
	min_coins = T(n,v)


	return min_coins, l_num_each_coin # return the min number of coins 
				  # from x1...xn that yield value v





