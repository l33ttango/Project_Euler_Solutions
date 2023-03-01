"""
Euler 24    
A permutation is an ordered arrangement of objects. For example, 3124 is one possible permutation of the digits 1, 2, 3 and 4. If all of the permutations are listed numerically or alphabetically, we call it lexicographic order. The lexicographic permutations of 0, 1 and 2 are:

012   021   102   120   201   210

What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?

Solution: 2783915460
RunTime: 0.6699678897857666 sec
"""

import itertools
import time

start = time.time()

def list_to_number(permutation_list):
    """
    Changes a list of numbers in one number
    """
    return int(''.join(map(str, permutation_list)))


def find_permutation(number_length, nth_iteration):
    """
    this creates a list of all permutations, returns the nth iteration as an integer
    """
    list_permutation_lists = list(itertools.permutations(range(number_length)))
    the_answer_list = list_permutation_lists[nth_iteration - 1]
    return list_to_number(the_answer_list)

print (find_permutation(10, 1000000))
print (time.time() - start)