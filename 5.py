
def is_divisible(num):
    # The problem calls to test 1-20, but if a number is divisible by 4 then it
    # is by 2 as well. Apply that logic to the whole range only leaves the
    # following numbers, which reduces the testing significantly.
    tests = [11,12,13,14,15,16,17,18,19,20]

    for i in tests:
        if ((num/i) % 1) != 0:
            return False
    return True

# Main #
i = 20
while True:
    if is_divisible(i):
        break

    # No point in incrementing by 1 since the number needs to divisible by 2.
    i += 2;
  
print(i)

# Main - End #
