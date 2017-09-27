# CS 6505 HW2 problem 10

cnt_subinversions = 0

def count_significant_inversions(A = [1,2,3,6,11]):
	# goal is to COUNT the number of inversions;
	# in the example input array the inversions 
	#	are (2,3) and (6,11) => num inversions is 2
	# 
	# this is essentially a modified merge sort algo
	# running time: O(n lg n) 
	#

	n = len(A)
	# first, recursively partition the sequence of n elements into 
	# two subsequences with the same size until only one 
	# element is in each sub sequence

	# merging subarrays
	if len(A) > 1:
		midpoint = len(A)//2 
		array_left = A[ 0 : midpoint]
		array_right = A[ midpoint : n]
		count_significant_inversions(array_left)
		count_significant_inversions(array_right)

		i, j, k = 0
		while i < len(array_left) and j < len(array_right):
			if array_left[i] < array_right[j]:
				A[k] = array_left[j]
				i = i+1
			else: #elt from left side is bigger than elt from right side
				if array_left[i] > 2 * array_right[j]:#check for significant inversion
					cnt_subinversions += 1 #add to count of inversions
				A[k] = array_right[j]
				j = j+1
			k = k+ 1

		while i < len(array_left):
			A[k] = array_left[i]
			i= i + 1
			k = k+ 1

		while j < len(array_right):
			A[k] = array_right[j]
			j = j+1
			k = k+1




