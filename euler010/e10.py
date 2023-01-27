"""
Euler 10

The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.

Solution: 142913828922
Runtime: 9.663866996765137 sec
"""
import math
import time

start = time.time()

def primes_sieve1(limit):
    limitn = limit + 1
    primes = dict()
    for i in range(2, limitn): primes[i] = True

    for i in primes:
        factors = range(i,limitn, i)
        for f in factors[1:]:
            primes[f] = False
    return [i for i in primes if primes[i]==True]

def sum_of_primes(maximum):
    return sum(primes_sieve1(maximum))
    
print (sum_of_primes(2000000))
end = time.time()
print (end - start)
