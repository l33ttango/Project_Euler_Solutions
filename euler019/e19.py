"""
1 Jan 1900 was a Monday.
Thirty days has September,
April, June and November.
All the rest have thirty-one,
Saving February alone,
Which has twenty-eight, rain or shine.
And on leap years, twenty-nine.
A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.
How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?

Solution: 171
Runtime: less than a millisecond
"""
import time
start = time.time()

def first_day_of_next_month(date_tuple):
    
    day = date_tuple[0]
    month = date_tuple[1]
    year = date_tuple[2]
    
    long_month = [1, 3, 5, 7, 8, 10]
    if month in long_month:
        day = (day + 31) % 7 
        month += 1
        return day, month, year
    elif month == 12:
        day = (day + 31) % 7
        month = 1
        year += 1
        return day, month, year
    elif month != 2:
        day = (day + 30) % 7
        month += 1
        return day, month, year
    else:
        if year % 4 == 0 and year != 1900:
            day = (day + 29) % 7
            month += 1
            return day, month, year
        else:
            day = (day + 28) % 7
            month += 1
            return day, month, year
        
def is_first_of_month(date_tuple):
    count = 0
    
    day = date_tuple[0]
    month = date_tuple[1]
    year = date_tuple[2]    
    while year < 2001:
        if day == 0:
            count += 1
            date_tuple = first_day_of_next_month(date_tuple)
            day = date_tuple[0]
            month = date_tuple[1]
            year = date_tuple[2]
        else:
            date_tuple = first_day_of_next_month(date_tuple)
            day = date_tuple[0]
            month = date_tuple[1]
            year = date_tuple[2]
    return count

date = (2, 1, 1901)
print (is_first_of_month(date)) 
print ((time.time() - start) * 1000)
