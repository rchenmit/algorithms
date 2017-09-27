# CS 6505 HW2 problem 8
# give algo that does 2 things:
#   1. determing whether array has a strong majority 
#   2. if YES, then print the value $m$ of the strong majority
from numpy import floor


def strong_majority_finder(a = [1,2,3,3,3,3]):
	""" 
		Inputs: a is array
		In our example default for a, the value 3 would be the strong majority 
		because (floor(n/2) +1)  =  4 and the number 3 happens 4 times. 

		Running time: This is O(n). If there is to be a strong majority 
		then it should appear consecutively more often than any other
		number. It has to, in order for at least half the values
		to be equal to that.
	"""
	n = len(a) # n is the length of a
	## if theres 2 items in array and they're the same then return "YES" 
	## and value of the strong majority
	if n ==0:
		return "NO" # empty array --> no majority
	if n ==1: 
		return "YES" # if only 1 item in array then its the majority
	if n ==2:
		if a[0] = a[1]:
			return ("YES", a[1]) 
		else:
			return "NO"
	## if theres more than 2 items in array then create temporary array 
	## if any consecutive 2 numbers are the same then put that into the temp array
	temp = []
	for i in range(n-1): #compare every adjacent set of 2
		if a[i] = a[i+1]:
			temp.append(a[i]) # insert a[i] into temp array temp
		i = i + 1
	return strong_majority_finder(temp) 


