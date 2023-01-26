"""
Euler 9

A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

a^2 + b^2 = c^2
For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.

Solution: 
Runtime:  0.7755756378173828 seconds
"""
"""

METHOD:
Consider a triangle w/ legs a, b, c
Using Euclid's formula, there exist numbers m, n where m>n>0 s.t. 

a = m^2 - n^2
b = 2mn
c = m^2 + n^2

so a + b + c = 2m^2 + 2mn
We want to find m, n, st. 1000 = 2m^2 + 2mn, 
or, 500 = m^2 + mn

Since both m, n are whole numbers, we can also surmise that m divides 500 evenly. In fact, for any pythagorean triplet a, b, c, the sum SUM will be even. So it makes sense to talk about SUM/2 as a whole number 

Solution: 31875000
Runtime: 0.007364100078120828 seconds
"""
import timeit
import math
start = timeit.timeit()

def list_of_m_values(pythagorean_sum):
    """
    returns list of potential m values, where m divides the pythagorean sum
    """
    m_values = []
    for i in range(2, int(math.sqrt(pythagorean_sum))):
        if pythagorean_sum % i == 0:
            m_values.append(i)
    return m_values

def find_m_n(pythagorean_sum):
    """    
    returns m, n where m > n
    """
    if pythagorean_sum % 2 != 0 or pythagorean_sum <=0:
        raise ValueError("input must be positive even integer")

    potential_m_list = list_of_m_values(pythagorean_sum)
    for m in potential_m_list:
        potential_n = (pythagorean_sum - 2.0 * m * m) / (2 * m)
        if int(potential_n) == potential_n and potential_n < m:
            return m, potential_n
    print ("oops")

def find_a_b_c(pythagorean_sum):
    """
    Returns legs of right triangle; a, b, c, st a+b+c = pythagorean_sum
    """
    m, n = find_m_n(pythagorean_sum)
    a = m * m - n * n
    b = 2 * m * n
    c = m * m + n * n
    return a * b * c

print (find_a_b_c(1000))
end = timeit.timeit()
print (end  - start)
