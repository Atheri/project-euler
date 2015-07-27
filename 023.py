"""
runtime: 4.093 seconds

Started out running at 8 seconds, tweak some things to hopefully get the
runtime down. The loop for creating the abundant number sums now short ciruits
if it goes over the limit provided in the problem. Changed from storing the
abundant sums to a list of bools (true if the index is an abundant sum). Still
not as fast as I hoped.
"""

import math
import time

def sum_of_factors(x):
    x_sqrt = int(math.sqrt(x))
    div_sum = 1

    if x_sqrt**2 == x:
        div_sum += x_sqrt
        x_sqrt -= 1

    for i in range(2, x_sqrt+1):
        if x % i == 0:
            div_sum += i + x/i

    return div_sum

n = 28123
abundant_nums = []
abundant_sums = [False for x in range(0,n+1)]

start = time.time()

for i in range(2, n+1):
    if i < sum_of_factors(i):
        abundant_nums.append(i)

for i in abundant_nums:
    for j in abundant_nums:
        if i+j <= n:
            abundant_sums[i+j] = True
        else:
            break

total = 0
for i in range(1, n+1):
    if abundant_sums[i] != True:
        total += i

print("result", total)
end = time.time()
print("time:", end-start, "seconds")
