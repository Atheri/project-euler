"""
runtime: 0.0083 seconds
"""

import time

def alphabet_value(string):
    total = 0
    for c in string:
        total += ord(c)-ord('A')+1
    return total
        
start = time.time()

f = open('p022_names.txt', 'r')
names = f.read().replace('"', '').split(',')
f.close()

names.sort()
total = 0
for i, name in enumerate(names):
    total += alphabet_value(name) * (i+1)

print("results:", total)
end = time.time()
print("time:", end-start, "seconds")
