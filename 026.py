"""
runtime: 0.00203 seconds

A decimal recurring cycle can be found if the same remainder is come across
twice during the long division. The distance between the two occurances would
be the cycle length. A division 1/n has n-1 unique remainders. So the largest
recurring decimal is at most length n-1.

With this in mind it makes sense to start with the large n values, since they
have the possibility to make the longest chain. When a chain of length x is
found, then any n < x can be automatically excluded, which saves on runtime.
"""

import time

start = time.time()

n = 1000
max_seq = 0
value = 0

for i in range(n-1, 1, -1):
    if max_seq >= i:
        break
    remainders = [0 for x in range(0, i)]
    a = 1
    position = 1

    while remainders[a] == 0 and a != 0:
        remainders[a] = position
        a *= 10
        a %= i
        position += 1

    if (position - remainders[a]) > max_seq and a != 0:
        max_seq = position - remainders[a]
        value = i

print("result:", value, "with a cycle of", max_seq)
end = time.time()
print("time:", end-start, "seconds")
