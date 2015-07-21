import math
        
def is_prime(num):
    i = 2
    result = 0
    while i < num:
        result = num / i
        if result % 1 == 0:
            return False
        i += 1
    return True

# Main #

num_primes = 6
num = 13

while num_primes < 10001:
    num += 2 # All even after 2 are not prime
    if is_prime(num):
        num_primes += 1

print(num)

# Main - End #
