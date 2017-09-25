## longest path, dynamic programming - pseudocode

## find length of longest path from v_1 to v_n
## in DAG G. 
## assume G is topological sorted already
##


def longest_path_v1_vn(G, v_1, v_n):
	length_to_this_vertex = []
	for i in range(n):
		length_to_this_vertex.append( infinity) ## initialize all lenghths to 
											    ## vertices from source 
											    ## to be infinity

	top_sorted_G = topolotical sort G ## O(|V| + |E|)

	## loop thru edges in topologically sorted order
	for i in range(len(top_sorted_G)):
		for j in range(i, len(top_sorted_G)): # it's an edge of v_j comes later than v_i
											  # in top_sorted_G
			## add the weight of edge v_i -> v_j if it's going to increase greatest length to v_j so far
			if length_to_this_vertex[top_sorted_G[j]] <= length_to_this_vertex[top_sorted_G[i]] + weight(G, i,j):
				length_to_this_vertex[top_sorted_G[j]] = length_to_this_vertex[top_sorted_G[i]] + weight(G, i,j)

	return max( length_to_this_vertex ) #returns the LENGTH of the longest path













