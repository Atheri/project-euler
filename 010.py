"""
    My first implementation was a trial by division brute force method. Turns
out it was going to take a long time. So in the spirit of Project Euler's 
'one-minute rule' I went looking for ways to generate prime numbers.

    This brought me to the implementation I use called "Sieve of Eratosthenes."
Essentially in the trial by division you test each number for primeness by
testing all divisions up to it, which quickly becomes expensive. Instead
generate a list of not primes as you go. When you come across a number in the
list, it's not prime and move on. If a number is found not in the list, then
add all multiples of that number to the list (up to the target n). The dominant
operation in this method is the time it takes to look up a number in the list, 
which a python set does very quickly even in large numbers.

    A thought about looking up ways to solve these problems. At first I was
hesitant because I'm basically looking up a solution. However, if I learn about
something new in the process, like the Sieve of Eratosthenes, then I'm alright
with it
"""

import time
import math
        
# Main #
start = time.time()

n = 2000000

multiples = set()
primes = list()

for i in range(2, n+1):
    if i not in multiples:
        primes.append(i)
        multiples.update(range(i*i, n+1, i))
sum = 0
for j in primes:
    sum += j
print(" sum:", sum)        

end = time.time()
print("time:", end-start, "seconds")
# Main - End #
