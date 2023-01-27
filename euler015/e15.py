"""
Starting in the top left corner of a 2x2 grid, and only being able to move to the right and down, there are exactly 6 routes to the bottom right corner.

How many such routes are there through a 20x20 grid?

"""

"""
This is a combinatorics problem. There are 20 moves down and 20 moves to the left, for a total of 40 moves. There are 20! moves horizontally and 20! moves vertically. 

The answer is 40!/(20!)^2 

Solution: 137846528820
Runtime: 0.0013377666473388672 sec

"""
import math
import time

n = 20

start = time.time()
print(math.factorial(2*n)/(math.factorial(n)*math.factorial(n)))
print (time.time() - start)