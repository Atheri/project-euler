"""
Time to complete: 4.1 sec

The naive brute force approach, calculating a completely new triangle number
for each number, and then calculating all divisors with 0 < n <= num, took
longer than I was hoping.

Two things were changed to significantly reduce time: 

1. The nature of the triangle number is you can keep a running total. Given a
    natural number x, the triangle number is sum from 1 to x. So the triangle
    number for x+1 is sum from 1 to x + x+1.

2. After doing some research, to find all the divisors of a number, x, it's not
    nessasry to look at all numbers <x. The divisors are duplicates after the
    sqrt of the number. I.E. for divisors of 28 done the naive way you have 
    1  28 
    2  14
    4  7 
    7  4 
    14 2 
    28 1 
    They are duplicates after the sqrt rounded down, 5. Reducing the
    calculations required from n to sqrt(n), a great improvement.

The sqrt thing is pretty cool, TIL.
"""

import time
import math

def calc_num_divisors(num):
    # When sqrt(num) is < 2 then the range in the for loop below doesn't work. 
    # Catch the base cases.
    if num == 1: return 1
    elif num < 4: return 2
    
    # Only need to look up to sqrt of num, since after the sqrt the divisors
    # are duplicated, so just add two.
    sqrt_num = int(math.sqrt(num))
    count = 0

    # divisors calculation
    for i in range(1, sqrt_num+1):
        if num % i == 0:
            count += 2 

    # If num is a perfect square, then it's sqrt is counted twice as a divisor
    # Correct count for the extra divisor
    if sqrt_num**2 == num:
        count -= 1
    return count
# calc_num_divisors - End #


# Main #
start = time.time()

cur_num = 0
triangle_num = 0
divisors = 0

while divisors < 500:
    cur_num += 1
    triangle_num += cur_num
    divisors = calc_num_divisors(triangle_num)
    
print("Triangle Number:", triangle_num)
print("Divisors:", divisors)   
end = time.time()
print("time:", end-start, "seconds")
# Main - End #
