"""
Euler 17

If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?


NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters and 115 (one hundred and fifteen) contains 20 letters. The use of "and" when writing out numbers is in compliance with British usage.

for numbers under 100, the word "one" will be used 9 times - 1, 21, 31, 41, 51, 61, 71, 81, 91
same for each other digit numbers

for numbers under 100, the "teen" numbers will each be used once

for numbers under 100, the word "twenty" will be used 10 times
    same for the other double digit number/names
    
for numbers from 100 -199:
the word "one" will be used 100 times, PLUS another 9 times. 
the word "hundred" will be used 100 times
the word "and" will be used 99 times

sum_of_letters_from_100_199 = above PLUS sum_of_letters_from_1-99

Solution: 21124
Runs in 9.8e-05 seconds
"""
import time
start = time.time()

ONES = [
    "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
TEENS = [
    "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", 
    "sixteen", "seventeen", "eighteen", "nineteen"]
TENS = [
    "twenty", "thirty", "forty", "fifty", "sixty", "seventy", 
    "eighty", "ninety"]
    
HUNDREDS = ["hundred"]

def letter_count(num_list):
    letter_count = []
    for num in num_list:
        letter_count.append(len(num))
    return letter_count

def first_99_letter_count():
    ones_list = letter_count(ONES)
    teens_list = letter_count(TEENS)
    tens_list = letter_count(TENS)

    ones_count = 0
    teens_count = 0
    for num in ones_list:
        ones_count += num
    for num in teens_list:
        teens_count += num
    
def count_letters_in_list(my_list):
    total_letters = 0
    for num in my_list:
        total_letters += len(num)
    return total_letters

def total_char_under_100():
    ones_digits = 9 * count_letters_in_list(ONES)
    teens = count_letters_in_list(TEENS)
    tens = 10 * count_letters_in_list(TENS)
    return ones_digits + teens + tens

def total_char_under_1000():
    hundred_ands = 99 * 9 * (3 + len("hundred"))
    under_100 = total_char_under_100()
    hundreds = 9 * 7
    return 10 * under_100 + hundred_ands + hundreds + 100 * count_letters_in_list(ONES) + len("onethousand")


print (total_char_under_1000())
print (time.time() - start)
