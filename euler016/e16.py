"""
Euler 16
2 ^ 15 = 32768 and the sum of the digits is 
3 + 2 + 7 + 6 + 8 = 26.

What is the sum of the digits of the number 2 ^ 1000?

Solution = 1366
Run Time = 0.000738859176636
"""
exponent = 2 ** 1000

exponent_sum = 0
for i in str(exponent):
    if i.isdigit():
        exponent_sum += int(i)

print (exponent_sum)


