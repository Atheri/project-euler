"""
runtime: 0.000109 seconds

Nothing special.
"""

import time
import math

start = time.time()

n = 100
n = math.factorial(n)
total = sum(int(x) for x in str(n))

print("result:", total)
end = time.time()
print("time:", end-start, "seconds")

