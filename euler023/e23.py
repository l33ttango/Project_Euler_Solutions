"""
A perfect number is a number for which the sum of its proper divisors is exactly equal to the number. For example, the sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.

A number n is called deficient if the sum of its proper divisors is less than n and it is called abundant if this sum exceeds n.

As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest number that can be written as the sum of two abundant numbers is 24. By mathematical analysis, it can be shown that all integers greater than 28123 can be written as the sum of two abundant numbers. However, this upper limit cannot be reduced any further by analysis even though it is known that the greatest number that cannot be expressed as the sum of two abundant numbers is less than this limit.

Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.


Answer: 4179871
RunTime: 2.248900890350342 sec

"""
import math
import time

start = time.time()

def is_abundant(num):
    """
    Input must be integer >= 2. Returns True if num is abundand, else False
    """
    if num < 2:
        raise ValueError("Input must be an integer >= 2")
    sum_of_divisors = 1
    sqrt = int(math.sqrt(num))
    for i in range(2, sqrt + 1):
        if num % i == 0:
            sum_of_divisors += i + num / i
    if sqrt * sqrt == num:
        sum_of_divisors -= sqrt
    if sum_of_divisors > num:
        return True
    return False    

def list_of_abundant_numbers(maximum):
    """
    Returns list of all abundant numbers <= maximum
    """
    abundant_list = []
    for num in range(2, maximum + 1):
        if is_abundant(num):
            abundant_list.append(num)
    return abundant_list

def set_of_abundant_sums(maximum):
    """
    returns a list of all abundant sums <= maximum
    """
    abundant_sums = set()
    abundant_numbers = list_of_abundant_numbers(maximum)
    for num1 in abundant_numbers:
        for num2 in abundant_numbers:
            s = num1 + num2
            if s <= maximum:
                abundant_sums.add(s)
    return abundant_sums


def sum_of_numbers_that_are_not_sum_of_2_abundants(maximum):
    """
    returns a list of numbers <= maximum that cannot be written as the sum of 2 abundant numbers
    """
    abundant_sums = set_of_abundant_sums(maximum)
    non_abundant_sums = []
    sum_of_nonabundants = 0
    for num in range(1, maximum ):
        if num not in abundant_sums:
            sum_of_nonabundants += num
    return sum_of_nonabundants


answer =sum_of_numbers_that_are_not_sum_of_2_abundants(28123)
print (answer)
print (time.time() - start)