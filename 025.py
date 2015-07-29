"""
runtime: 0.0317 seconds

Python generators are pretty cool. I wasn't sure what the pythonic way to
consume a generator until a condition is met, but this seemed to work alright.
"""
import time

start = time.time()

def fib():
    prev, cur = 0, 1
    while True:
        yield cur
        prev, cur = cur, prev + cur

n = 1000
fib_gen = fib()
for i, val in enumerate(fib_gen):
    if len(str(val)) < n:
        continue
    else:
        index = i
        break

print("result:", index+1)
end = time.time()
print("time:", end-start, "seconds")
