# Since a < b < c, so 'a' can be 0 <= a < 1000/3, 
# and 'b' can be a < b < 1000/2.

import math
import time

def pythag_triplet():
    for a in range(0,333):
        for b in range(a+1,500):    # a+1 since a < b
            c  = math.sqrt(a**2 + b**2)
            if a + b + c == 1000:
                return a, b, c
# pythag_triplet - End #

# Main #
start = time.time()

a, b, c = pythag_triplet()
product = int(a*b*c)
print(" abc:", product)

end = time.time()
print ("time:", end-start, "seconds")
# Main - End #
