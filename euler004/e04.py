"""
Problem 4
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 x 99.

Find the largest palindrome made from the product of two 3-digit numbers.

"""
"""
(9, 9)
(9, 8) (8, 8)
(9, 7) (8, 7) (7, 7)
(9, 6) (8, 6) (7, 6) (6, 6)
(9, 5) (8, 5) (7, 5) ...
(9, 4) (8, 4) (7, 4) ...

Consider the tuples above. If we go diagonally across from upper right to bottom left, the slices will be
[(9,9,)]
[(9,8)]
[(8,8), (9,7)]
[(8,7), (9, 6)]
[(7, 7), ((8, 6), (9, 5)]

it can be shown that the product of each tuple in a slice is larger than the tuples below the slice. 
i.e. 8 * 8 > 9 * 7 > 8* 7 > 9 * 6

using this sequence, we can stop once we find the first palendrome

This process speeds up finding the largest palindrome product.

Answer 906609
Runtime: 15.622138977050781 milliseconds

"""
import time
start = time.time()

def is_palendrome(num):
    """
    returns True if num is palendrome
    """
    num_str = ""
    num_list = list(str(num))
    for i in range(1, len(str(num)) + 1):
        num_str += num_list[-i]
    return str(num) == num_str

def is_answer(num_digits):
    """
    num_digits refers to number of digits in the product
    i.e. num_digits = 3 if we are looking for the product of two 3-digit numbers 
    returns largest palandromic number made from the product of two num_digit numbers
    """
    maximum = int(str(9) * num_digits)
    return even_s(maximum, 0)

def even_s(maximum, s):
    if s % 2 != 0:
        raise ValueError("s must be even integer.")
    j = int(s / 2)
    i = int(s / 2)
    while i >= 0:
        product = (maximum - i) * (maximum - j)
        if is_palendrome(product):
            return  product
        else:
            i -= 1
            j += 1
    return odd_s(maximum, s + 1)

def odd_s(maximum, s):
    if s % 2 != 1:
        raise ValueError("s must be odd number.")
    i = s // 2
    j = s // 2  + 1 
    while i >= 0:
        product = (maximum - i) * (maximum - j)
        if is_palendrome(product):
            return  product
        else:
            i -= 1
            j += 1
    return even_s(maximum, s + 1)
    
print (is_answer(3))
end = time.time()
final_result = (end - start) * 1000

print ("Runtime equals ", final_result, "milliseconds")
