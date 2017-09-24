# CS 6505 HW2 problem 5

def longest_path_from_sorted_DAG(G):
	# input: G=(V,E)
	# output: LENGTH of the longest path in G
	let n = |V|  #let n = number of vertices

	# define array length_longest_path_from_this_v
	#   -- this array stores the length of longest path starting from vertex v
	length_longest_path_from_this_v = []
	for v_i in V:
		length_longest_path_from_this_v[v_i] = 0

	# loop thru all vertices in reverse topological order
	# 	-- check 
	for v_i in V (reverse order):
		if v_i has no outgoing edges:
			length_longest_path_from_this_v[v_i] = 0
		else:
			for all u in V such that (v,u) in E:
				if length_longest_path_from_this_v[v_i] < length_longest_path_from_this_v[u] + 1:
					length_longest_path_from_this_v[v_i] = length_longest_path_from_this_v[u] + 1

	return length_longest_path_from_this_v[1]




