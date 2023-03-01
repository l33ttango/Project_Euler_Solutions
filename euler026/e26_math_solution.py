"""
Euler 26
A unit fraction contains 1 in the numerator. The decimal representation of the unit fractions with denominators 2 to 10 are given:

1/2	= 	0.5
1/3	= 	0.(3)
1/4	= 	0.25
1/5	= 	0.2
1/6	= 	0.1(6)
1/7	= 	0.(142857)
1/8	= 	0.125
1/9	= 	0.(1)
1/10	= 	0.1

Where 0.1(6) means 0.166666..., and has a 1-digit recurring cycle. It can be seen that 1/7 has a 6-digit recurring cycle.

Find the value of d < 1000 for which 1/d contains the longest recurring cycle in its decimal fraction part.

SOLVED

See https://proofwiki.org/wiki/Maximum_Period_of_Reciprocal_of_Prime

From Period of Reciprocal of Prime, the period of recurrence is the order of 10
 modulo p.
That is, it is the smallest integer d
 such that:
10**d ≡ 1(mod p)


Solution: 983
RunTime: 0.3918910026550293 sec

"""
import time

start = time.time()

def find_length_of_cycle(num):
    """
    returns length of the recurring cycle for 1/num
    See https://proofwiki.org/wiki/Maximum_Period_of_Reciprocal_of_Prime
    """
    for i in range(1, num + 1):
        if (10** i) % num == 1:
            return i 
    return 0

def find_largest_cycle(maximum):
    """
    the largest cycle  
    """
    best = 0
    best_period = 0
    for i in range(3, maximum, 2):  
        period = find_length_of_cycle(i)
        if period > best:
            best = period
            best_period = i
    return best_period

a = find_largest_cycle(1000)
print(a)
print (time.time() - start)