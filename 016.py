"""
runtime: 0.00012 seconds

Pretty straight forward. Didn't do anything fancy, and it was still very quick
"""

import time

start = time.time()

exp = 2**1000

total = 0
digits = list(str(exp))
for c in digits:
    total += int(c)

end = time.time()
print("time:", end-start, "seconds")
print(" sum:", total)
