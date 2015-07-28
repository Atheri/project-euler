"""
runtime: 0.024189472198486328 seconds

Originally running at 0.7 secs by iterating over nth_permute generator,
switched to this suggested pythonic way of selecting the nth element of an
iterable. Pretty significant performance increase. 

Using python's permutations function we only calculate to the nth permutation
since the function is a generator, and if the arguments are in lexicographic
order then the results of the generator will be in lexicographic order.
"""

import itertools
import time

start = time.time()

# Problem variables
digits = '0123456789'
n = 1000000

permutes = itertools.permutations('0123456789')
nth_permute = next(itertools.islice(permutes, n-1, None))

result = ''.join(nth_permute)

print("result:", result)
end = time.time()
print("time:", end-start, "seconds")
