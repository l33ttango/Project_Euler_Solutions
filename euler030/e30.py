"""
Euler30

Surprisingly there are only three numbers that can be written as the sum of fourth powers of their digits:

1634 = 1^4 + 6^4 + 3^4 + 4^4
8208 = 8^4 + 2^4 + 0^4 + 8^4
9474 = 9^4 + 4^4 + 7^4 + 4^4
As 1 = 1^4 is not a sum it is not included.

The sum of these numbers is 1634 + 8208 + 9474 = 19316.

Find the sum of all the numbers that can be written as the sum of fifth powers of their digits.

Note: 9^5 * 7 <=500,000

Solution: 443839
RunTime: 0.5286657810211182 sec
"""
import time

start = time.time()
FIFTH_POWER_DICT = {i: i ** 5 for i in range(10)}

def sum_fifth_power_of_digits(num):
    total = 0
    for i in str(num):
        total += FIFTH_POWER_DICT[int(i)]
    if total == num:
        return True
    return False

def sum_of_fifth_power_sums(maximum):
    solution = 0
    for i in range(2, maximum + 1):
        if sum_fifth_power_of_digits(i):
            solution += i
    return solution

print (sum_of_fifth_power_sums(600000))
print(time.time() - start)