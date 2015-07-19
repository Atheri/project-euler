#Brute force method for solving largest prime factor.

import math

        
def is_prime(num):
    i = 3
    result = 0
    while i < num:
        result = num / i
        if result % 1 == 0:
            return False
        i += 1
    return True

start_num = 600851475143

i = 3
while i < start_num/3:
    factor = start_num / i
    if factor % 1 == 0:
        if is_prime(factor):
            break
    i += 1;

print(factor)

