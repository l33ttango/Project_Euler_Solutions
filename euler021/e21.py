"""
Amicable numbers
Problem 21
Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
If d(a) = b and d(b) = a, where a != b, then a and b are an amicable pair and each of a and b are called amicable numbers.

For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10000.

Solution: 31626
Runtime: 0.031281232833862305 seconds
"""
import math
import time

start = time.time()

sum_of_divisors_dict = {}

def return_sum_of_divisors(x):
    """
    Returns the sum of the divisors of number
    """
    total = 1
    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0:
            total += i
            if x / i != i:
                total += x/i
    return total

for i in range(1, 10000):
    sum_of_divisors_dict[i] = return_sum_of_divisors(i)
    

total = 0
for key in sum_of_divisors_dict:
    if sum_of_divisors_dict[key] in sum_of_divisors_dict:
        if sum_of_divisors_dict[sum_of_divisors_dict[key]] == key:
            if key != sum_of_divisors_dict[key]:
                total += (key)

print (total) 
print (time.time() - start)

