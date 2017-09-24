# CS 6505 HW2 problem 3 

def coin_change(x , v):
	# inputs:
	# 	x: array of coin denominations
	#	v: value you want to make
	# output:
	#	True if possible to make change for v with items in x
	#	False if not possible

	## declare lookup table T of size v+1, init to all Falses
	T[0] = True
	for i in range(1,v):
		T[i] = False
	for v_lookup in range(1, v):
		for j in range(1, n):
			if x[j] <= v:
				T[v_lookup] = T[v_lookup] and T[v - v_lookup] ## set to True if 
															  ## T[v_lookup] == True 
															  ## and T[v - v_lookup] == True
															  ## else set to False

			else:
				T[v_lookup] = False
	if T[v] == True:
		return "YES"
	else: 
		return "NO"
