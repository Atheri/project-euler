"""
Runtime: 3.4 seconds

Starting with the naive brute force solution, calculating the chain for every
number, it ran in 44 seconds. If my solution falls under the 1 min rule, I
generally don't look up ways for a better solution. However in this case I had
an idea right after finishing the first solution.

After looking up how to use a python dictionary, I implemented the below
solution. The idea is to store a calculated chain length in a dictionary. Then
if I ever come across that number again, instead of finishing the chain
calculation, I just add the current chain number to the one stored in the
dictionary. This lead to almost 13 times increase!

After finishing this solution, I was looking at other implementations, and
there is a further optimization of this implementation. I only stored the
starting number chain length, but ideally, when calculating an unknown chain,
you would record all the numbers in the chain that are new. You could have to
keep track of the order they appeard in and then add them to the dictionary at
the end of the iteration. Maybe I'll do that one in the future.
"""

import time

start = time.time()

largest_i = 0
largest_chain = 0
max_n = 999999
chain_dict = {}

for i in range(1, max_n+1):
    chain_n = 1
    n = i
    while n > 1:
        if n in chain_dict:
            chain_n += chain_dict[n] - 1
            n = 1;
        else:
            if n % 2 == 0:
                n = n/2
            else:
                n = 3*n+1
            chain_n += 1
    chain_dict[i] = chain_n
    if chain_n > largest_chain:
        largest_chain = chain_n
        largest_i = i

print("longest chain:", largest_chain)
print(" start number:", largest_i)
end = time.time()
print("time:", end-start, "seconds")
