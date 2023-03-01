"""
Names scores
Problem 22
Using names.txt (right click and 'Save Link/Target As...'), a 46K text file containing over five-thousand first names, begin by sorting it into alphabetical order. Then working out the alphabetical value for each name, multiply this value by its alphabetical position in the list to obtain a name score.

For example, when the list is sorted into alphabetical order, COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list. So, COLIN would obtain a score of 938 * 53 = 49714.

What is the total of all the name scores in the file?

Answer: 871198282
RunTime: 0.0070629119873046875 sec
"""
# Create a list from the text file
import time

start = time.time()
list_of_names = []

with open("p022_names.txt") as inputfile:
    for line in inputfile:
        list_of_names.append(line.strip("").split(","))

list_of_names = list_of_names[0]

# Create a conversion from letters to numbers
lower_case_alphabet = "abcdefghijklmnopqrstuvwxyz"

# start dictionary for conversion
letters_to_numbers_dict = {'"': 0, "\n": 0, "\\" : 0}

# create dictionary
for letter in lower_case_alphabet:
    letters_to_numbers_dict[letter] = lower_case_alphabet.index(letter) + 1
letters_to_numbers_dict

#use dictionary to convert a word to it's sum
def find_sum(name):
    word_sum = 0
    for letter in name:
        word_sum += letters_to_numbers_dict[letter.lower()]
    return word_sum

# find sum of all words * index
def the_answer(name_list):
    name_sum = 0
    for i in range(len(name_list)):
        name_sum += find_sum(name_list[i]) * (i + 1)
    return name_sum

# sort the original list
sorted_list = sorted(list_of_names)

# Find the answer!
print (the_answer(sorted_list))
print (time.time() - start)