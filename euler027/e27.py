"""
Problem 27
Euler discovered the remarkable quadratic formula:
n^2 + n + 41

It turns out that the formula will produce 40 primes for the consecutive integer values 0 <= n <= 39. However, when n=40,40 ^ 2 + 41 + 41 = 40(40+1)+ 41  + 41 is divisible by 41, and certainly when n=41,412+41+41n=41,412+41+41 is clearly divisible by 41.

The incredible formula, n ^ 2 - 79 * n + 1601 ws discovered, whic produces 80 primes for the onsecutive values 0 <=n <= 799. The product of hte coefficients, -79 and 1601, is -126479. 

Considering quadratics of the form:

n ^ 2 + an + bn2 where |a|<1000 and |b| <=1000

where |n| is the modulus/absolute value of nn
e.g. |11| = 11 and |-4| = 4
Find the product of the coefficients, a and b, for the quadratic expression that produces the maximum number of primes for consecutive values of n, starting with n=0.

Answer: -59231
RunTime: 0.44780540466308594 sec
"""
import time
start = time.time()
def return_set_of_primes(maximum):
    is_prime = [True for i in range(maximum + 1)]
    is_prime[0] = False
    is_prime[1] = False
    for i in range(2, int(maximum ** 0.5) + 1):
        for j in range(2*i, maximum + 1, i):
            is_prime[j] = False
    prime_list = []
    for i in range(maximum + 1):
        if is_prime[i] == True:
            prime_list.append(i)
    return prime_list
    
def eval_poly(x, poly_str):
    return poly_str[0] * x * x + poly_str[1] * x + poly_str[2]

class FindBestPoly():
    def __init__(self, maximum, prime_list):
        self.maximum = maximum
        self.prime_list = prime_list
        self.prime_set = set(i for i in prime_list)
    
    def __str__(self):
        print ("Maximum is " + self.maximum + ", Prime List is " + self.prime_list)
    
    def count_primes(self, poly_str):
        count = 0
        for i in range(self.maximum):
            if not eval_poly(i, poly_str) in self.prime_set:
                return count
            else:
                count += 1
        return count
    
    def best_coefficient_b(self, prime):
        """
        Returns the best polynomial string for the given prime
        """
        best_count = 0
        best_coefficient = 3
        for num in self.prime_list:
            b = num - prime - 1 #this ensures that x = 1 is a prime. 1**2 + 1*b + prime = 1 + num -1-prime + prime = num which is in prime_list
            poly_str = (1, b, prime)
            if self.count_primes(poly_str) > best_count:
                best_count = self.count_primes(poly_str)
                best_coefficient =  b
        
        return best_coefficient, best_count

    def best_poly_str(self):
        best_prime = 3
        best_coefficient = 1
        best_count = 0
        for prime in self.prime_list:
            if prime > 1000:
                return best_poly
            coefficient, count = self.best_coefficient_b(prime)
            if count > best_count:
                best_count = count
                best_poly = (1, coefficient, prime)
        for prime in self.prime_list:
            if prime > 1000:
                return best_poly
            coefficient, count = self.best_coefficient_b(-prime)
            if count > best_count:
                best_count = count
                best_poly = (1, coefficient, -prime)
        
        return best_poly
            
            
            
primes = return_set_of_primes(20000)
poly = FindBestPoly(1000, primes)
best_poly = poly.best_poly_str()
answer =  best_poly[1] * best_poly[2]
print(answer)
print(time.time() - start)