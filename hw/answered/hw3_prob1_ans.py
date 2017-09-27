## subset sum, dynamic programming - pseudocode

## given n items (each with increasing weight), and W upper bound
## compute the best set of items to put in the set S
## so that you get the highest weight thats still 
## less than the max weight W

## 1. build look-up table M
## 2. work backwards from max weight to find 
##    what items to put in the set S
## 

## n: number of items
## w: array with weight of each item ; n total items
## W: max weight the sum can be
##

w = array of weights 
def subset_sum(n, W):
	## initialize the look-up table
	for r = 0, ... ,W
		M[0,r] = 0
	for j = 1, ..., n
		M[j,0] = 0

	for j = 1, ... , n
		for r = 0 , ... , W
			if w[j] > r:
				M[j,r] = M[j-1, r] #if this item too heavy, cannot include; 
								   # therefore max sum is whatever it was 
								   # with the all items up to the last j
			M[j , r ] = max(  M[j-1, r], 
							  w[j] + M[ j-1, W-w[j] ] )  #find max of these two
	return M[n,W] ## after table has been filled, we simply look it up





