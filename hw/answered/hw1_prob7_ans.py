#hw1_prob7_ans.py

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






