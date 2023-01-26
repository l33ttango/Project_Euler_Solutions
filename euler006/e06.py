"""
Euler 6

The sum of the squares of the first ten natural numbers is,

1**2 + 2**2 + ... + 10**2 = 385

The square of the sum of the first ten natural numbers is,

(1 + 2 + ... + 10)**2 = 552 = 3025

Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 - 385 = 2640.

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

Solution = 25164150
Run time = 0.000121831893921
"""
import time

start = time.time()

def sum_of_squares(maximum):
    new_sum = 0
    for i in range(maximum + 1):
        new_sum += i**2
        
    return new_sum

def square_of_sum(maximum):
    return (maximum * (maximum + 1) / 2) ** 2

print abs(square_of_sum(100) - sum_of_squares(100)) 
end = time.time()

print end - start
