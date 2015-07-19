
first = 1
second = 2
temp = 0

sum = 0

while sum < 4000000:
    if second % 2 == 0:
        sum += second
    temp = first + second
    first = second
    second = temp

print(sum)

