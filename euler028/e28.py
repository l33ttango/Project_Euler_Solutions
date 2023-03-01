"""
Euler 28

Starting with the number 1 and moving to the right in a clockwise direction a 5 by 5 spiral is formed as follows:

21 22 23 24 25 
20  7  8  9 10
19  6  1  2 11
18  5  4  3 12
17 16 15 14 13
             
It can be verified that the sum of the numbers on the diagonals is 101.

What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral formed in the same way?

Solution: 669171001
Runs in 0.00107 secs
"""

"""
Consider the corners of each layer in the spiral. 

layer(0) = 1

layer(1) has corners, 3, 5, 7, 9   -- each corner has difference of 2
layer(2) has corners 13, 17, 21, 25  --  difference of 4
layer(3) has corners 31, 37, 43, 49  -- difference of 6
layer(4) has corners 57, 65, 73, 81 -- difference of 8

"""
def returns_sum_of_spiral_corners(size_of_spiral):
	"""
	see instructions above
	"""
	spiral_sum = 1	# we start in the center with 1
	corner = 1	# each corner
	layer = 0	# the nth layer of the spiral
	difference = 0	# the difference between corners in the layer

	layers_in_spiral = (size_of_spiral - 1) / 2 #this will always return an integer as the size of the spiral must be odd
	
	while layer < layers_in_spiral:
		layer += 1
		difference += 2
		for i in range(4):
			corner += difference
			spiral_sum += corner
		
	return spiral_sum

print (returns_sum_of_spiral_corners(1001))
