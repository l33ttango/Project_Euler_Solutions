"""
Euler 5

2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
"""

"""
The easist solution would be to notice that 20 is the first number to utilize 2^3, and every other number not represented by a product of the numbers 1 - 10 are prime numbers, i.e. 11, 13, 17, 19. 

Hence, the answer is 2520 * 11 * 13 * 17 * 19 * 2

A more generalized answer can be shown below. 

Solution = 232792560
Run time = 0.000140905380249

"""
import time
from fractions import gcd

start = time.time()

def find_solution(minimum, maximum):
    if minimum <= 0 or maximum <= minimum:
        raise ValueError("minimum must be greater than 0, maximum must be greater than minimum")
    product = minimum
    for i in range(minimum + 1, maximum + 1):
        if product % i == 0:
            i + 1
        else:
            gcd_i = gcd(i, product)
            product = product * i / gcd_i
    
    return product

print find_solution(1, 20)

end = time.time()
print end - start

