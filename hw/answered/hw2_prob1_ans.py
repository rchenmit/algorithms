# CS 6505 HW2 problem 1

from numpy import max

def max_contig_sum_subsequence(S):
	# input: array S
	# output: max sum of subseq in S
	n = len(S) # n= length of S
	T = []
	T[0] = 0 
	max_sum = 0 # update max sum
	l_best_subseq = [S[0] ] #update max subseq; initialize at first element of S
	for j in range(1, n):
		T[j] = max( [ T[j-1] + S[j], S[j] ] ) 
	for j in range(0, n):
		if T[j] > max_sum:
			max_sum = T[j] # remember best sum
			l_best_subseq.append( S[j] )# remember best subseq
		else:
			l_best_subseq = [ S[j] ] # best subseq would be subseq starting with this s_j
	return max_sum, l_best_subseq

