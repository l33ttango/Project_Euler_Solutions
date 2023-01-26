"""
Euler 01

If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.

Solution: 233168
Runtime: 0.5791187286376953 milliseconds
"""
import time

start = time.time()
def return_sum_to_n(n):
	return (n* (n+1) /2)

def return_sum_of_multiples(n, maximum):
	limit = (maximum -1) // n
	return n * return_sum_to_n(limit)

def return_solution(n, m, maximum):
    """
    Adds all multiples of n under maximum, all multiples of m under maximum, then subtracts the duplicates
    """    
    sum_n = return_sum_of_multiples(n, maximum)
    sum_m = return_sum_of_multiples(m, maximum)
    sum_nm = return_sum_of_multiples(n*m, maximum)
    
    return (sum_n + sum_m - sum_nm)
    

n = 3
m = 5
maximum = 1000
print (return_solution(n, m, maximum))
end = time.time()
final_result = (end - start) * 1000

print ("Runtime equals ", final_result, "milliseconds")