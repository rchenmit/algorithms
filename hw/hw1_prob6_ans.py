#hw1_prob6_ans.py

def determine_if_sum_T_in_arr(sorted_arr, T):
	exists = False;
	i = 1
	j = n

	while (i < j): # while the condition holds that i<j
		if sorted_arr[i] + sorted_arr[j] > T: # if its too big
			j = j - 1
		elif sorted_arr[i] + sorted_arr[j] < T: # if its too small
			i = i + 1
		else:
			exists = True 

	return exists



def sort(input_arr):
	count_arr: initialize array w/ size m_max #although we only need indexes m_min to m_max

	for a = 1 .. n 	     # initialize a OUTPUT array
		output_arr[a] = NIL
	for i = m_min .. m_max       #  initialize a "counting" array with M elements 
		count_arr[i] = 0
	for j = 1 .. n 				# loop thru input_arr and increment the counting array
							    #  this loop is O(n)
		count_arr[input_arr[j]] = count_arr[input_arr[j]] + 1 #increment by 1
	for i = m_min+1 .. m_max             #
		count_arr[i] = count_arr[i] + count_arr[i-1] # record the number of elts 
													 # in input_arr that are <=i
													 # this is O(M)
	for j = n .. 1 #count decrementing by 1
		output_arr[count_arr[input_arr[j]]] = input_arr[j]  
		count_arr[input_arr[j]] = count_arr[input_arr[j]] - 1 

	return output_arr



