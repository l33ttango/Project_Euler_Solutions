"""
Euler 7

By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10,001st prime number?

Answer = 104743
Run time = 0.364840984344
"""
import math
import time

start = time.time()

def is_prime(num):
    if num in [2, 3, 5]:
        return True
    
    if num % 2 == 0:
        return False
    if num % 3 == 0:
        return False
    if num % 5 == 0:
        return False
    
    else:
        for i in range(7, int(math.sqrt(num)) + 1, 2):
            if num % i == 0:
                return False
    return True

def find_nth_prime(nth_prime):
    i = 1 # referencing the prime 2
    num = 3
    while i < nth_prime:
        if is_prime(num):
            i += 1
            num += 2
        else:
            num += 2
    return num - 2


print find_nth_prime(10001)
end = time.time()

print end - start
