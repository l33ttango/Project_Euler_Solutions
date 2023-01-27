"""
The following iterative sequence is defined for the set of positive integers:

n -> n/2 (n is even)
n -> 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:

13 -> 40 -> 20 -> 10 -> 5 -> 16 -> 8 -> 4 -> 2 -> 1
It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.

Solution: 837799
Runtime: 1.8909242153167725
"""
import time
start = time.time()
def longest_collatz_sequence(t):
    cache = {1: 1}

    def collatz(n):
        if n not in cache:
            cache[n] = collatz(3 * n + 1 if n % 2 else n / 2) + 1

        return cache[n]  # Length of Collatz Chain

    return max(range(1, t), key=collatz)  # Greatest Chain


print (longest_collatz_sequence(1000000))
print (time.time() - start)
