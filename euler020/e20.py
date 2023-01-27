"""n! means n x (n - 1) x . . . x 3 x 2 x 1

For example, 10! = 10 x 9 x ... x 3 x 2 x 1 = 3628800,and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

Find the sum of the digits in the number 100!

Solution: 648
Runtime: 0.995635986328125 milliseconds

"""
import math
import time
start = time.time()

def sum_of_factorial_digits(a):
    total = 0
    factorial = math.factorial(a)
    while factorial:
        total += factorial % 10
        factorial  //= 10
    
    return total
    
print (sum_of_factorial_digits(100))
print ((time.time() - start) * 1000)