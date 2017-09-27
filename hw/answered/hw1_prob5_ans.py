# hw1_prob5_ans.py

def find_min_max(a):
	## initialize new arrays
	l_smallers = []
	l_biggers = []


	## we are going to make n/2 comparisons (every set of 2 consecutive elements, 
	## put the smaller of each pair in l_smallers, put the bigger of
	## each pair in l_biggers)

	i=2
	while (i <= n):
		if a[i] > a[i-1]:
			l_smallers.append(a[i-1])
			l_biggers.append(a[i])
		else:
			l_smallers.append(a[i])
			l_biggers.append(a[i-1])

	## now, find the min, by simply finding the smallest in l_smallers
	## this will require n/2-1 comparisons
	curr_smallest = infinity
	for a_k in l_smallers: 
		if a_k < curr_smallest:
			curr_smallest = a_k


	## now, find the max, by simply finding the biggest in l_biggers
	## this will require n/2-1 comparisons
	curr_biggest = -infinity
	for a_k in l_biggers:
		if a_k > curr_biggest:
			curr_biggest = a_k

	return {'max': curr_biggest, 'min': curr_smallest}