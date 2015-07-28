import itertools
import time

start = time.time()

def fib():
    prev, cur = 0, 1
    while True:
        yield cur
        prev, cur = cur, prev + cur
        
fib_gen = fib()
print(list(itertools.islice(fib_gen, 0, 12)))
end = time.time()
print("time:", end-start, "seconds")
