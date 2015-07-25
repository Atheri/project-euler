"""
runtime: 0.127 seconds

I didn't try this one without optimization, so I don't really have a comparison point. Used the sqrt(num) trick to find divisors. Stored all numbers and their calculated divisor sums in a dictionary to avoid calculating them twice. Used a set to store the amicable numbers < 10000. Worked pretty well.
"""


import time
import math

def proper_divisors(x):
    if x < 2: return []
    d1 = [1]
    d2 = []
    x_sqrt = math.sqrt(x)
    for i in range(2, int(x_sqrt)):
        j = x/i
        if j % 1 == 0:
            d1.append(i)
            d2.insert(0, j)
    if x_sqrt % 1 == 0:
        d1.append(int(x_sqrt))
    divisors = d1 + list(map(int, d2))
    return divisors

# sum_of_divisors - End #

# Main #

start = time.time()
n = 10000
divisor_sums = {}


for i in range(1, n):
    if i not in divisor_sums:
        divisor_sums[i] = sum(proper_divisors(i))

amicable_set = set()

for a in range(1, n):
    if a in amicable_set: continue
    b = divisor_sums[a]
    if a == b: continue

    if b not in divisor_sums:
        divisor_sums[b] = sum(proper_divisors(b))
    if a != b:
        if divisor_sums[a] == b and a == divisor_sums[b]:
            amicable_set.add(a)
            if b < n: amicable_set.add(b)

result = sum(amicable_set)

print("result:", result)
end = time.time()
print("time:", end-start, "seconds")
