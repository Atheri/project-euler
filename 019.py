"""
runtime: 0.0356 seconds

A thousand years of days isn't very much, so I just made a little simulation.
The advance function advances the calendar by 1 day, and makes adjustments to
weekday, month, year, and adjusts feb when needed for leap year. After every
advance it checks the date to see if its the first of the month and a sunday.
Continues until the year 2001 is reached. This way it's really easy to change
the start and end date, provided the dates are valid, to look in a different
range.
"""

import time
start = time.time()

weekday = 0 # 0-6 | Sun-Mon
d = 1       # 1 is the first day of the month
m = 0       # 0-11 | Jan-Dec
y = 1901    # Start year

days = ["sun", "mon", "tues", "wed", "thurs", "fri", "sat"]

month_len = {'jan':31, 'feb':28, 'mar':31, 'apr':30, 'may':31, 'jun':30,
             'jul':31, 'aug':31, 'sep':30, 'oct':31, 'nov':30, 'dec':31}

months = ['jan', 'feb', 'mar', 'apr', 'may', 'jun', 
          'jul', 'aug', 'sep', 'oct', 'nov', 'dec']

def is_leap_year(year):
    if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
        return True
    return False

def advance(d, m, y, weekday):
    weekday += 1
    if weekday > len(days)-1:
        weekday = 0
    
    d += 1
    if d > month_len[months[m]]:
        d = 1
        m +=1
    if m >= len(months):
        m = 0
        y += 1
    if is_leap_year(y):
        month_len['feb'] = 29
    else:
        month_len['feb'] = 28
    return d, m, y, weekday


count = 0
while y < 2001:
    if d == 1 and days[weekday] == "sun":
        count += 1
    d, m, y, weekday = advance(d, m, y, weekday)

print("result:", count)
end = time.time()
print("time:", end-start, "seconds")
